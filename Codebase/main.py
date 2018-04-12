import datetime
import getopt
import os
import pickle
import socket
import sys
import time
from _tkinter import TclError
from multiprocessing import Process
from multiprocessing.managers import BaseManager
from queue import LifoQueue

import colorama

import solvers.half_turn.table_generator as half_turn_generator
import solvers.half_turn.table_lookup as half_turn_lookup
import solvers.multiphase.table_generator as multiphase_generator
import solvers.multiphase.table_lookup as multiphase_lookup
from cube.cube_class import Cube, Color, Move, Face
from cube.moves import dyn_move
from database.database_manager import DatabaseManager
from solvers.tree.interface import Interface
from solvers.tree.tree_generator import generate_tree
from translator.move_converter import convert_sequence


def init_db(prints=True):
    """
    Create a Database Cursor object which can be passed around to for global access to database
    :param prints: Print flag
    :return: Database Cursor object
    """
    print('Initialising DB.', end='') if prints else None
    db = DatabaseManager('Codebase/database/db.sqlite')
    db.query("PRAGMA synchronous = off")  # Allows asynchronous writing for better multiprocessing write speed
    print('.', end='')
    db.query("BEGIN TRANSACTION")
    print('!') if prints else None
    return db


def multiphase_solve(db, position, phase_count):
    """
    Use the multiphase method of solving the Cube
    :param db: Database connection
    :param position: The position scanned in by the robot
    :param phase_count: The number of phases to check
    :return: The solve sequence for the Cube
    """
    def end_solve():
        """
        The method used to end the multiphase solve process, regardless of kociemba usage
        :return: the combined sequences from each phase
        """
        total_sequence = []
        for sequence in sequence_list:
            total_sequence.extend(sequence)

        print('- Final Sequence: ', end='')
        for end_move in total_sequence:
            print(end_move.name, end=' ')
        print()

        return total_sequence

    sequence_list = []
    phase_name = ['Zero', 'One', 'Two', 'Three', 'Four']
    cube_list = []
    position_list = [position]

    for phase in range(phase_count):
        print('- Phase %s: ' % phase_name[phase], end='')

        looked_up_sequence = multiphase_lookup.lookup_position(db, position_list[phase], phase)

        # If the position wasn't found in the table, option for fallback to kociemba
        if len(looked_up_sequence) > 0 and looked_up_sequence[0] == LookupError:
            print()
            kociemba_choice = ''
            while kociemba_choice != 'Y' and kociemba_choice != 'N':
                kociemba_choice = input('Solve with kociemba package? (y/n) ').upper()
            if kociemba_choice == 'Y':
                print('Converting Cube to kociemba notation.', end='')
                # Overwrite all previous sequences, kociemba uses a different method
                sequence_list = [multiphase_lookup.kociemba_fallback(position)]

                return end_solve()
            else:
                print('Exiting program, you got as far as this: \n%s\n' % Cube(looked_up_sequence[1]))
                transmit_choice = ''
                while transmit_choice != 'Y' and transmit_choice != 'N':
                    transmit_choice = input('Transmit to robot anyway? (y/n) ').upper()
                if transmit_choice == 'Y':
                    looked_up_sequence = []
                else:
                    print('Nice try, bye')
                    exit()

        sequence_list.append(looked_up_sequence)  # List of sequences from each phase
        cube_list.append(Cube(position_list[phase]))  # List of Cubes produced by each phase's sequence
        for move in sequence_list[phase]:
            dyn_move(cube_list[phase], move)
            print(move.name, end=' ')
        position_list.append(cube_list[phase].position)
        print()
    return end_solve()


def half_turn_solve(db, position):
    """
    Solve the Cube with half turns only, proof of concept for simple table
    :param db: Database connection
    :param position: The mixed position
    :return: The solve sequence from the table
    """
    print('- Table Lookup: ', end='')
    solve_sequence = half_turn_lookup.lookup_position(db, position)
    temp_cube = Cube(position)
    for move in solve_sequence:
        dyn_move(temp_cube, move)
        print(move.name, end=' ')
    print()
    return solve_sequence


def tree_solve(position):
    """
    Solve the Cube by creating a tree for breadth-first search
    :param position: Mixed position scanned by robot
    :return: The solve sequence
    """
    move_group = [Move.U, Move.NOT_U, Move.U2, Move.D, Move.NOT_D, Move.D2,
                  Move.L, Move.NOT_L, Move.L2, Move.R, Move.NOT_R, Move.R2,
                  Move.F, Move.NOT_F, Move.F2, Move.B, Move.NOT_B, Move.B2]

    # Create an instance of a LifoQueue for passing positions to the GUI
    BaseManager.register('LifoQueue', LifoQueue)
    manager = BaseManager()
    manager.start()
    position_queue = manager.LifoQueue()

    cube = Cube(position)

    # Create a separate process for generating the tree
    tree_process = Process(target=time_method,
                           args=(generate_tree, cube, move_group, position_queue,),
                           name='tree_process')

    tree_process.start()

    try:
        window = Interface(position_queue)
        window.root.after(0, window.update_cube_net)
        window.root.mainloop()
    except TclError as err:
        print(err)

    tree_process.terminate()  # kill process when window is closed

    # Retrieve the solve sequence and delete the file
    with open('Codebase/solvers/tree/solution.pickle', 'rb') as solution_file:
        pickled_sequence = pickle.load(solution_file)
    os.remove('Codebase/solvers/tree/solution.pickle')

    solve_sequence = []
    print('\n- Solve Sequence: ', end='')
    for move in pickled_sequence:
        solve_sequence.append(move)
        print(move.name, end=' ')
    print()
    return solve_sequence


def time_method(method, *arguments):
    """
    Simple utility method to run a method and return the time elapsed
    :param method: The method to be run
    :param arguments: Any arguments to be passed to the method
    :return:
    """
    start = int(round(time.time() * 1000))
    result = method(*arguments)
    end = int(round(time.time() * 1000))
    total = (end - start) / 1000
    print('Time: %0.03fs' % total)
    return result


def create_socket():
    """
    Create a socket object to connect to the EV3 robot
    :return: a connection object which can be used for sending and receiving data
    """
    sock = socket.socket()
    sock.bind(('0.0.0.0', 3000))
    print('Listening for connection...')
    sock.listen(1)
    conn, client_address = sock.accept()
    print('EV3 connected @ %s:%s\n' % (client_address[0], client_address[1]))
    return conn


def get_robot_scan(conn):
    """
    Receive the scanned data from the robot
    :param conn: socket connection
    :return: the Cube's position
    """
    pos_received = False
    position = ''
    while not pos_received:
        position = conn.recv(1024).decode()
        if position != '':
            pos_received = True
    return position


def orient_cube(cube):
    """
    A lot of the tables work with the Cube being oriented in a specific manner. Rather than recreating the tables for
    all 24 orientations, it's much simpler to just orient the Cube to match the expected orientation
    :param cube: the scanned Cube
    :return: the oriented Cube
    """
    orient_sequence = []

    white_face = cube.get_face_with_color(color=Color.WHITE)
    if white_face != Face.UP:
        white_to_up = {
            Face.DOWN: [Move.X2],
            Face.LEFT: [Move.NOT_Y, Move.X],
            Face.RIGHT: [Move.Y, Move.X],
            Face.FRONT: [Move.X],
            Face.BACK: [Move.Y2, Move.X]
        }
        orient_sequence.extend(white_to_up[white_face])
        for move in orient_sequence:
            dyn_move(cube, move)

    green_face = cube.get_face_with_color(color=Color.GREEN)
    if green_face != Face.FRONT:
        green_to_front = {
            Face.LEFT: [Move.NOT_Y],
            Face.RIGHT: [Move.Y],
            Face.BACK: [Move.Y2]
        }
        orient_sequence.extend(green_to_front[green_face])
        dyn_move(cube, green_to_front[green_face][0])

    if len(orient_sequence) > 0:
        print('- Orient Sequence: ', end='')
        for move in orient_sequence:
            print(move.name, end=' ')
        print()
        return orient_sequence

    return []


def main():
    # Set all the booleans based on the opts and args
    robot_on = '-r' in opts
    db_generation = '-d' in opts
    db_clear = '-c' in opts
    half_turn = '-h' in opts
    multiphase = '-m' in opts
    tree = '-t' in opts
    verbose = '-v' in opts

    conn = None
    position = None

    db = init_db()

    if robot_on:
        conn = create_socket()
        position = get_robot_scan(conn)
        print('Scanned position: %s' % position)
    elif not db_generation and (half_turn or multiphase or tree):  # Solving without robot
        position = ''
        while len(position) != 54:
            position = input('Enter a position: ').upper()
        print()

    if db_clear:
        confirm = ''
        while confirm != 'Y' and confirm != 'N':
            confirm = input('Are you sure you want to wipe the database? (y/n) ').upper()
        if confirm == 'Y':
            print('Deleting Database.', end='')
            try:
                os.remove('%s/Codebase/database/db.sqlite' % os.getcwd())
                print('.', end='')
                db = init_db(False)  # Re-make db file to avoid errors
                print('!')
            except PermissionError as err:
                print(err)
        else:
            print('Aborted')

    if db_generation:
        if multiphase:
            for phase in range(5):
                multiphase_generator.generate_lookup_table(db, phase, verbose)
        elif half_turn:
            half_turn_generator.generate_lookup_table(db)
        else:
            confirm = ''
            while confirm != 'Y' and confirm != 'N':
                confirm = input('Are you sure you want to generate the entire database?\n'
                                'This will take a considerable amount of time (y/n) ').upper()
            if confirm == 'Y':
                for phase in range(5):
                    multiphase_generator.generate_lookup_table(db, phase, verbose)
                half_turn_generator.generate_lookup_table(db, verbose)
    elif multiphase or half_turn or tree:
        solve_sequence = []
        cube = Cube(position)
        print('Cube: \n%s' % cube)

        orient_sequence = orient_cube(cube)

        if multiphase:
            solve_sequence = multiphase_solve(db, cube.position, 5)
        if half_turn:
            # Check that the Cube is valid by reducing colors
            if cube.position_reduced != Cube().position_reduced:
                print("Invalid Half Turn Cube, reduced Cube should be 'solved' but looks like this: \n%s" % Cube(
                    cube.position_reduced))
                exit()
            solve_sequence = half_turn_solve(db, cube.position)
        if tree:
            solve_sequence = tree_solve(cube.position)

        # Print all the sequences for analysis

        robot_sequence = []
        for move in orient_sequence:
            robot_sequence.append(move.name.lower())
        robot_sequence.extend(convert_sequence(cube, solve_sequence, verbose))
        print('\n- Robot Sequence: ', end='')
        for move in robot_sequence:
            print(move.upper(), end=' ')

        print('\n- Final Cube -')
        for move in solve_sequence:
            dyn_move(cube, move)
        print(cube)

        # And then send the solve to the robot if possible
        if robot_on:
            conn.send(pickle.dumps(robot_sequence))
            conn.close()


if __name__ == '__main__':
    # Colorama allows for colored printing
    colorama.init()
    print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

    opts, args = getopt.getopt(sys.argv[1:], 'rdchmtv')
    opts = dict(opts)

    if len(opts) == 0:
        print("""
------------------------------------
  OPTIONS:
    -r : Connect to Robot
    -d : Generate Database, can also choose a method to refine generation
    -c : Clear the entire database
    -h : half-turn generation/solve method
    -m : multiphase generation/solve method
    -t : tree solve
    -v : verbose outputs
------------------------------------
        """)
    else:
        # Check only one method is declared
        if ('-h' in opts and '-m' in opts) or ('-h' in opts and '-t' in opts) or ('-m' in opts and '-t' in opts):
            print('Please choose ONE method')
            exit()

        main()
