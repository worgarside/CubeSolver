from group_solver.position_generator import generate_positions
import time
from cube.moves import *
from data.database_manager import DatabaseManager
from cube.cube_class import Cube
from gui.interface import Interface
from multiprocessing import Process, Queue
from tree_solver.tree_generator import generate_tree
from sys import  exit
from _tkinter import TclError

GROUP_THREE = [MOVE.U2, MOVE.D2, MOVE.L2, MOVE.R2, MOVE.F2, MOVE.B2]
GROUP_TWO = [MOVE.U2, MOVE.D2, MOVE.L, MOVE.R, MOVE.F2, MOVE.B2]
GROUP_ONE = [MOVE.U2, MOVE.D2, MOVE.L, MOVE.R, MOVE.F, MOVE.B]
GROUP_ZERO = [MOVE.U, MOVE.D, MOVE.L, MOVE.R, MOVE.F, MOVE.B]

GROUP_TEST = [MOVE.U2, MOVE.D2, MOVE.L2, MOVE.R2, MOVE.F2, MOVE.B2]

GROUP_COMPLETE = [MOVE.U, MOVE.NOT_U, MOVE.U2, MOVE.D, MOVE.NOT_D, MOVE.D2,
                  MOVE.L, MOVE.NOT_L, MOVE.L2, MOVE.R, MOVE.NOT_R, MOVE.R2,
                  MOVE.F, MOVE.NOT_F, MOVE.F2, MOVE.B, MOVE.NOT_B, MOVE.B2]


def init_db():
    db = DatabaseManager('data/db.sqlite3')

    db.query("DROP TABLE IF EXISTS positions")

    db.query("""CREATE TABLE IF NOT EXISTS positions (
                    id INTEGER PRIMARY KEY,
                    position TEXT NOT NULL,
                    depth INTEGER NOT NULL,
                    parent_id INTEGER NOT NULL,
                    parent_move TEXT NOT NULL)
                """)

    return db


def group_solve(db):
    pos = time_function(generate_positions, Cube(), GROUP_THREE)

    for p in pos:
        for q in p:
            db.query("INSERT INTO positions VALUES (?, ?, ?, ?, ?)",
                     (q.id, q.position, q.depth, q.parent_id, str(q.parent_move)))


def tree_solve():
    process_list = []

    cube = Cube()
    u(cube)
    r(cube)
    l(cube)

    position_queue = Queue()

    tree_process = Process(target=time_function, args=(generate_tree, cube, GROUP_COMPLETE, position_queue,), name='tree_process')
    process_list.append(tree_process)

    for p in process_list:
        p.start()

    window = Interface(position_queue)
    window.root.after(500, window.update_position)
    window.root.mainloop()

    for p in process_list:
        print('Terminating %s' % p.name)
        p.terminate() # kill process when window is closed


def time_function(func, *args):
    start = int(round(time.time() * 1000))
    result = func(*args)
    end = int(round(time.time() * 1000))
    total = (end - start) / 1000
    print("Time: %0.2fs" % total)

    return result


def main():
    tree_solve()


if __name__ == "__main__":
    main()
