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
import solvers.multiphase.table_generator as mphase_generator
import solvers.multiphase.table_lookup as mphase_lookup
from cube.cube_class import Cube, Color, Move, Face, SOLVED_POS
from cube.moves import dyn_move
from database.database_manager import DatabaseManager
from solvers.tree.interface import Interface
from solvers.tree.tree_generator import generate_tree
from translator.move_converter import convert_sequence


def init_db(prints=True):
    print('Initialising DB.', end='') if prints else None
    db = DatabaseManager('Codebase/database/db.sqlite')
    db.query("PRAGMA synchronous = off")
    print('.', end='')
    db.query("BEGIN TRANSACTION")
    print('!') if prints else None
    return db


def multiphase_solve(db, position, phase_count):
    def end_solve():
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

        looked_up_sequence = mphase_lookup.lookup_position(db, position_list[phase], phase)
        if len(looked_up_sequence) > 0 and looked_up_sequence[0] == LookupError:
            print()
            kociemba_choice = ''
            while kociemba_choice != 'Y' and kociemba_choice != 'N':
                kociemba_choice = input('Solve with kociemba package? (y/n) ').upper()
            if kociemba_choice == 'Y':
                print('Converting Cube to kociemba notation.', end='')
                sequence_list = [mphase_lookup.kociemba_convert(position)]

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

        sequence_list.append(looked_up_sequence)
        cube_list.append(Cube(position_list[phase]))
        for move in sequence_list[phase]:
            dyn_move(cube_list[phase], move)
            print(move.name, end=' ')
        position_list.append(cube_list[phase].position)
        print()
    return end_solve()


def half_turn_solve(db, position):
    print('- Table Lookup: ', end='')
    solve_sequence = half_turn_lookup.lookup_position(db, position)
    temp_cube = Cube(position)
    for move in solve_sequence:
        dyn_move(temp_cube, move)
        print(move.name, end=' ')

    return solve_sequence


def tree_solve(position):
    move_group = [Move.U, Move.NOT_U, Move.U2, Move.D, Move.NOT_D, Move.D2,
                  Move.L, Move.NOT_L, Move.L2, Move.R, Move.NOT_R, Move.R2,
                  Move.F, Move.NOT_F, Move.F2, Move.B, Move.NOT_B, Move.B2]

    BaseManager.register('LifoQueue', LifoQueue)
    manager = BaseManager()
    manager.start()
    position_queue = manager.LifoQueue()

    cube = Cube(position)

    tree_process = Process(target=time_function,
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

    with open('Codebase/solvers/tree/solution.pickle', 'rb') as solution_file:
        pickled_sequence = pickle.load(solution_file)

    solve_sequence = []
    print('\n- Solve Sequence: ', end='')
    for move in pickled_sequence:
        solve_sequence.append(move)
        print(move.name, end=' ')

    return solve_sequence


def time_function(func, *arguments):
    start = int(round(time.time() * 1000))
    result = func(*arguments)
    end = int(round(time.time() * 1000))
    total = (end - start) / 1000
    print('Time: %0.03fs' % total)
    return result


def create_socket():
    conn = socket.socket()
    conn.bind(('0.0.0.0', 3000))
    print('Listening for connection...')
    conn.listen(1)
    c, client_address = conn.accept()
    print('EV3 connected @ %s:%s\n' % (client_address[0], client_address[1]))
    return c


def get_robot_scan(conn):
    pos_received = False
    position = ''
    while not pos_received:
        position = conn.recv(1024).decode()
        if position != '':
            pos_received = True
    return position


def orient_cube(cube):
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
        print('Orienting Cube: \n%s' % cube)
        return_sequence = []
        for move in orient_sequence:
            return_sequence.append(move.name.lower())

        return return_sequence

    return []


def main():
    robot_on = '-r' in opts
    db_generation = '-d' in opts
    db_clear = '-c' in opts
    half_turn = '-h' in opts
    multiphase = '-m' in opts
    tree = '-t' in opts

    conn = None
    position = None

    db = init_db()

    if robot_on:
        conn = create_socket()
        position = get_robot_scan(conn)
        print('Scanned position: %s' % position)

    if not robot_on and not db_generation and (half_turn or multiphase or tree):  # Solving without robot
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
            os.remove('%s/Codebase/database/db.sqlite' % os.getcwd())
            print('.', end='')
            db = init_db(False)  # Re-make db file to avoid errors
            print('!')
        else:
            print('Aborted')

    if db_generation:
        if multiphase:
            for phase in range(5):
                mphase_generator.generate_lookup_table(db, phase)
        elif half_turn:
            half_turn_generator.generate_lookup_table(db)
        else:
            confirm = ''
            while confirm != 'Y' and confirm != 'N':
                confirm = input('Are you sure you want to generate the entire database? (y/n) ').upper()
            if confirm == 'Y':
                for phase in range(5):
                    mphase_generator.generate_lookup_table(db, phase)
                half_turn_generator.generate_lookup_table(db)

    if multiphase or half_turn or tree:
        solve_sequence = []
        cube = Cube(position)
        print('Cube: \n%s' % cube)

        orient_sequence = orient_cube(cube)

        if multiphase:
            solve_sequence = multiphase_solve(db, cube.position, 5)
        if half_turn:
            if cube.position_reduced != SOLVED_POS:
                print('Invalid Half Turn Cube, reduced Cube should be solved but looks like this: \n%s' % Cube(
                    cube.position_reduced))
                exit()
            solve_sequence = half_turn_solve(db, cube.position)
        if tree:
            solve_sequence = tree_solve(position)

        print('\n- Final Cube -')
        for move in solve_sequence:
            dyn_move(cube, move)
        print(cube)

        if robot_on:
            robot_sequence = convert_sequence(cube, solve_sequence)
            total_sequence = orient_sequence + robot_sequence
            print(total_sequence)

            conn.send(pickle.dumps(robot_sequence))
            conn.close()


if __name__ == '__main__':
    colorama.init()
    print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

    opts, args = getopt.getopt(sys.argv[1:], 'rdchmt')
    opts = dict(opts)

    if len(opts) == 0:
        print("""
------------------------------------
  OPTIONS:
    -r : run with robot connection
    -d : (continue) database generation
    -c : clear the database
    -h : half-turn generation/solve
    -m : multiphase generation/solve
    -t : tree solve
------------------------------------
        """)
    else:
        if ('-h' in opts and '-m' in opts) or ('-h' in opts and '-t' in opts) or ('-m' in opts and '-t' in opts):
            print('Please choose ONE method')
            exit()

        main()
