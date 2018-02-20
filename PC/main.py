import colorama
import time
from _tkinter import TclError
from multiprocessing import Process
from multiprocessing.managers import BaseManager
from queue import LifoQueue

from cube.cube_class import Cube
from cube.moves import *
from data.database_manager import DatabaseManager
from group_solver.position_generator import generate_positions
from group_solver.good_bad_edges import make_all_edges_good
from gui.interface import Interface
from tree_solver.tree_generator import generate_tree

GROUP_THREE = [MOVE.U2, MOVE.D2, MOVE.L2, MOVE.R2, MOVE.F2, MOVE.B2]
GROUP_TWO = [MOVE.U2, MOVE.D2, MOVE.L, MOVE.R, MOVE.F2, MOVE.B2]
GROUP_ONE = [MOVE.U2, MOVE.D2, MOVE.L, MOVE.R, MOVE.F, MOVE.B]
GROUP_ZERO = [MOVE.U, MOVE.D, MOVE.L, MOVE.R, MOVE.F, MOVE.B]

GROUP_COMPLETE = [MOVE.U, MOVE.NOT_U, MOVE.U2, MOVE.D, MOVE.NOT_D, MOVE.D2,
                  MOVE.L, MOVE.NOT_L, MOVE.L2, MOVE.R, MOVE.NOT_R, MOVE.R2,
                  MOVE.F, MOVE.NOT_F, MOVE.F2, MOVE.B, MOVE.NOT_B, MOVE.B2]

GROUP_QUARTERS = [MOVE.U, MOVE.NOT_U, MOVE.D, MOVE.NOT_D,
                  MOVE.L, MOVE.NOT_L, MOVE.R, MOVE.NOT_R,
                  MOVE.F, MOVE.NOT_F, MOVE.B, MOVE.NOT_B, ]


def init_db():
    db = DatabaseManager('PC/data/db.sqlite')

    db.query('DROP TABLE IF EXISTS positions')
    db.query('''CREATE TABLE IF NOT EXISTS positions (
                    id INTEGER PRIMARY KEY,
                    position TEXT NOT NULL,
                    depth INTEGER NOT NULL,
                    move_chain TEXT NOT NULL)
                ''')

    return db


def group_solve(db):
    # pos_dict = time_function(generate_positions, GROUP_ZERO)
    #
    # for depth in pos_dict:
    #     for position in depth:
    #         db.query('INSERT INTO positions VALUES (?, ?, ?, ?)',
    #                  (position.pos_id, position.position, position.depth, str(position.move_chain)))
    # db.commit()

    cube = Cube()
    u(cube)
    d(cube)
    l(cube)
    r(cube)
    b(cube)
    u(cube)
    l(cube)
    r(cube)
    f(cube)
    u(cube)
    d(cube)
    l(cube)
    d(cube)
    r(cube)
    b(cube)
    u(cube)
    d(cube)
    good_pos = make_all_edges_good(cube.position_reduced)
    print(good_pos)


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
    print('Time: %0.2fs' % total)
    return result


def main():
    db = init_db()
    # group_solve(db)
    # tree_solve()
    time_function(group_solve, db)


if __name__ == '__main__':
    colorama.init()
    main()
