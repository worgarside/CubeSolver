from group_theory.position_generator import generate_positions
from position_tree.tree_generator import TreeGenerator
import time
from cube.moves import *
from data.database_manager import DatabaseManager
from cube.cube_class import Cube
from gui.interface import Interface
import queue
from processor_thread import ProcessThread

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


def thistlethwaite(db):
    pos = time_function(generate_positions, Cube(), GROUP_THREE)

    for p in pos:
        for q in p:
            db.query("INSERT INTO positions VALUES (?, ?, ?, ?, ?)",
                     (q.id, q.position, q.depth, q.parent_id, str(q.parent_move)))


def korf():
    position_queue = queue.Queue(0)

    cube = Cube()
    u(cube)
    r(cube)
    l(cube)

    tree_gen = TreeGenerator(cube, GROUP_COMPLETE)
    generation_thread = ProcessThread('generation_thread', position_queue, tree_gen.generate_tree)

    window = Interface()

    generation_thread.start()

    generation_thread.join()
    window.update_position(position_queue)

def time_function(func, *args):
    start = int(round(time.time() * 1000))
    result = func(*args)
    end = int(round(time.time() * 1000))
    total = (end - start) / 1000
    print("Time: " + str(total))

    return result


def main():
    korf()

if __name__ == "__main__":
    main()
