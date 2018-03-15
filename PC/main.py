import datetime
import getopt
import pickle
import socket
import sys
import time
from _tkinter import TclError
from multiprocessing import Process
from multiprocessing.managers import BaseManager
from queue import LifoQueue

import colorama

import group_solver_mk_one as gs1
import group_solver_mk_two.table_generator as gs2generator
import group_solver_mk_two.table_lookup as gs2lookup
from cube.cube_class import Cube
from cube.moves import *
from data.database_manager import DatabaseManager
from gui.interface import Interface
from move_translator.move_converter import convert_sequence
from tree_solver.tree_generator import generate_tree

GROUP_COMPLETE = [MOVE.U, MOVE.NOT_U, MOVE.U2, MOVE.D, MOVE.NOT_D, MOVE.D2,
                  MOVE.L, MOVE.NOT_L, MOVE.L2, MOVE.R, MOVE.NOT_R, MOVE.R2,
                  MOVE.F, MOVE.NOT_F, MOVE.F2, MOVE.B, MOVE.NOT_B, MOVE.B2]


def init_db(clear=False):
    print('Initialising DB')
    db = DatabaseManager('PC/data/db.sqlite')
    print('Vacuuming')
    db.query('VACUUM')
    db.query("PRAGMA synchronous = off")
    db.query("BEGIN TRANSACTION")
    print('DB Initialised')
    return db


def group_solve_mk_one(db, cube):
    sequence_list = []

    good_edge_pos = gs1.phase_one.make_all_edges_good(cube.position_reduced)
    good_edge_sequence = good_edge_pos.move_sequence[1:]
    sequence_list.append(good_edge_sequence)

    good_edge_cube = deepcopy(cube)
    for move in good_edge_sequence:
        dyn_move(good_edge_cube, move)

    print()
    print(good_edge_cube)

    good_corner_pos = gs1.phase_two.make_all_corners_good(good_edge_cube.position_reduced)
    good_corner_sequence = good_corner_pos.move_sequence[1:]
    sequence_list.append(good_corner_sequence)

    good_corner_cube = deepcopy(good_edge_cube)
    for move in good_corner_sequence:
        dyn_move(good_corner_cube, move)

    print()
    print(good_corner_cube)

    good_face_pos = gs1.phase_three.make_all_faces_good(good_corner_cube.position_reduced)
    good_face_sequence = good_face_pos.move_sequence[1:]
    sequence_list.append(good_face_sequence)

    good_face_cube = deepcopy(good_corner_cube)
    for move in good_face_sequence:
        dyn_move(good_face_cube, move)

    print()
    print(good_face_cube)

    final_sequence = gs1.phase_four.solve_cube(good_face_cube.position, db)
    sequence_list.append(final_sequence)

    solved_cube = deepcopy(good_face_cube)
    for move in final_sequence:
        dyn_move(solved_cube, move)

    print()
    print(solved_cube)

    total_sequence = []
    for sequence in sequence_list:
        print(sequence)
        total_sequence.extend(sequence)
    print(len(total_sequence))
    return total_sequence


def group_solve_mk_two(db, position):
    sequence_list = []

    phase_name = ['One', 'Two', 'Three', 'Four']
    cube_list = []
    position_list = [position]

    for phase in range(3):
        print(' - Phase %s -' % phase_name[phase])
        sequence_list.append(gs2lookup.lookup_position(db, position_list[phase], phase))
        cube_list.append(Cube(position_list[phase]))
        for move in sequence_list[phase]:
            dyn_move(cube_list[phase], move)
            print(move.name, end=' ')
        position_list.append(cube_list[phase].position)
        print('\n')

    total_sequence = []
    for sequence in sequence_list:
        total_sequence.extend(sequence)
    return total_sequence


def tree_solve():
    BaseManager.register('LifoQueue', LifoQueue)
    manager = BaseManager()
    manager.start()
    position_queue = manager.LifoQueue()

    process_list = []

    cube = Cube()
    u(cube)
    not_r(cube)
    not_b(cube)

    tree_process = Process(target=time_function, args=(generate_tree, cube, GROUP_COMPLETE, position_queue,),
                           name='tree_process')
    process_list.append(tree_process)

    for p in process_list:
        p.start()

    try:
        window = Interface(position_queue)
        window.root.after(0, window.update_cube_net)
        window.root.mainloop()
    except TclError as err:
        print(err)

    for p in process_list:
        print('Terminating %s' % p.name)
        p.terminate()  # kill process when window is closed


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


def main():
    robot_on = '-r' in opts
    db_generation = '-d' in opts
    db_clear = '-c' in opts
    solving = '-s' in opts

    conn = None
    position = None
    phase_count = 5


    db = init_db(True)

    if robot_on:
        conn = create_socket()
        position = get_robot_scan(conn)
        print('Scanned position: %s' % position)
    elif solving:
        # position = 'OBROWROGRWWWBRBWWWGOGWOYGGGWRYBBBYYYBOBYYYGRGOGROYROBR'
        # position = 'WBWWWWWGWOOOGWGRRRBWBBOGOGRGRBRBOOOOGYGRRRBYBYGYYYYYBY'
        # position = 'YWRBWYOOWOOBYYOGBYBRGGOGWGWBRYGBOWRRGWBRRYGRBWOWYYBOGR'
        # position = 'OGOYWYRBRWOWGOBWRWBRGGOBWGYBRGWBYYOYBRGYRYGOBOBOWYWRGR'
        position = 'GYWBWRBOYWRWRWRGWBOGRBORYGRGRBOBWWGBYYOYOOGYORBBWYGGOY'
        print('Scanned position: %s' % position)

    if db_clear:
        print('Clearing Database', end='')
        for table in range(phase_count):
            db.query('DROP TABLE IF EXISTS gs2p%i' % table)
            print('.', end='')
        db.commit()
        print('   Vacuuming...', end='')
        db.query('VACUUM');
        print('  Done!')

    if db_generation:
        for phase in range(phase_count):
            gs2generator.generate_lookup_table(db, phase)

    if solving:
        cube = Cube(position)
        print(cube)

        solve_sequence = group_solve_mk_two(db, position)

        print(' - Final Cube -')
        for move in solve_sequence:
            dyn_move(cube, move)
        print(cube)

        if robot_on:
            robot_sequence = convert_sequence(cube, solve_sequence)
            print(robot_sequence)

            conn.send(pickle.dumps(robot_sequence))
            conn.close()


if __name__ == '__main__':
    colorama.init()
    print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

    opts, args = getopt.getopt(sys.argv[1:], 'rdsc')  # eventually s:[algorithm]
    opts = dict(opts)

    if len(opts) == 0:
        print("""
------------------------------------
  OPTIONS:
    -r : run with robot connection
    -d : continue database generation
    -c : clear the database
    -s : solve the Cube
------------------------------------
        """)

    main()
