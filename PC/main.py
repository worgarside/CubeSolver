import socket
import time
from _tkinter import TclError
from multiprocessing import Process
from multiprocessing.managers import BaseManager
from queue import LifoQueue

import colorama

import group_solver_mk_one as gs1
import group_solver_mk_two.phase_one as gs2p1
import group_solver_mk_two.phase_two as gs2p2
import group_solver_mk_two.phase_three as gs2p3
from cube.cube_class import Cube
from cube.moves import *
from data.database_manager import DatabaseManager
from gui.interface import Interface
from tree_solver.tree_generator import generate_tree

GROUP_COMPLETE = [MOVE.U, MOVE.NOT_U, MOVE.U2, MOVE.D, MOVE.NOT_D, MOVE.D2,
                  MOVE.L, MOVE.NOT_L, MOVE.L2, MOVE.R, MOVE.NOT_R, MOVE.R2,
                  MOVE.F, MOVE.NOT_F, MOVE.F2, MOVE.B, MOVE.NOT_B, MOVE.B2]


def init_db(clear=False):
    db = DatabaseManager('PC/data/db.sqlite')

    if clear:
        # db.query('DROP TABLE IF EXISTS g_solve_mk1_p4')
        db.query('''CREATE TABLE IF NOT EXISTS g_solve_mk1_p4 (
                        depth INTEGER NOT NULL,
                        position TEXT PRIMARY KEY,
                        move_sequence BLOB NOT NULL)
                    ''')

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

    print('- Phase One -')
    phase_one_sequence = gs2p1.find_sequence_in_table(db, position)
    sequence_list.append(phase_one_sequence)

    phase_one_cube = Cube(position)
    for move in phase_one_sequence:
        dyn_move(phase_one_cube, move)
        print(move.name, end=' ')

    print('\n\n- Phase Two -')

    phase_two_sequence = gs2p2.find_sequence_in_table(db, phase_one_cube.position)
    sequence_list.append(phase_two_sequence)

    phase_two_cube = Cube(phase_one_cube.position)
    for move in phase_two_sequence:
        dyn_move(phase_two_cube, move)
        print(move.name, end=' ')

    print('\n\n- Phase Three -')

    phase_three_sequence = gs2p3.find_sequence_in_table(db, phase_two_cube.position)
    sequence_list.append(phase_three_sequence)

    phase_three_cube = Cube(phase_two_cube.position)
    for move in phase_three_sequence:
        dyn_move(phase_three_cube, move)
        print(move.name, end=' ')

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


def time_function(func, *args):
    start = int(round(time.time() * 1000))
    result = func(*args)
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


def get_current_position(conn):
    pos_received = False
    position = ''
    while not pos_received:
        position = conn.recv(1024).decode()
        if position != '':
            pos_received = True
    return position


def main():

    # conn = create_socket()
    # position = get_current_position(conn)
    db = init_db()

    # position = 'OBROWROGRWWWBRBWWWGOGWOYGGGWRYBBBYYYBOBYYYGRGOGROYROBR'
    # position = 'WBWWWWWGWOOOGWGRRRBWBBOGOGRGRBRBOOOOGYGRRRBYBYGYYYYYBY'
    # position = 'YWRBWYOOWOOBYYOGBYBRGGOGWGWBRYGBOWRRGWBRRYGRBWOWYYBOGR'
    # position = 'OGOYWYRBRWOWGOBWRWBRGGOBWGYBRGWBYYOYBRGYRYGOBOBOWYWRGR'
    position = 'GYWBWRBOYWRWRWRGWBOGRBORYGRGRBOBWWGBYYOYOOGYORBBWYGGOY'
    print('Scanned position: %s' % position)

    cube = Cube(position)
    print(cube)

    solve_sequence = group_solve_mk_two(db, position)
    # print(solve_sequence)

    print('\n\n- Final Cube -')
    for move in solve_sequence:
        dyn_move(cube, move)
    print(cube)


    # robot_sequence = convert_sequence(cube, solve_sequence)
    # print(robot_sequence)

    # conn.send(pickle.dumps(robot_sequence))
    # conn.close()


if __name__ == '__main__':
    colorama.init()
    main()
