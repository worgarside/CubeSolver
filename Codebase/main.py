from position_generator import generate_positions
import time
from cube.moves import *
import datetime
from database_manager import DatabaseManager
import sqlite3
from cube.cube_class import Cube

GROUP_THREE = [MOVE.U2, MOVE.D2, MOVE.L2, MOVE.R2, MOVE.F2, MOVE.B2]
GROUP_TWO = [MOVE.U2, MOVE.D2, MOVE.L, MOVE.R, MOVE.F2, MOVE.B2]
GROUP_ONE = [MOVE.U2, MOVE.D2, MOVE.L, MOVE.R, MOVE.F, MOVE.B]
GROUP_ZERO = [MOVE.U, MOVE.D, MOVE.L, MOVE.R, MOVE.F, MOVE.B]

GROUP_TEST = [MOVE.U, MOVE.D, MOVE.L, MOVE.R, MOVE.F, MOVE.B, MOVE.X, MOVE.Y, MOVE.Z]

conn = None


def main():
    db = DatabaseManager('data/db.sqlite3')

    print("Start: " + datetime.datetime.now().strftime("%H:%M"))

    db.query("""CREATE TABLE IF NOT EXISTS positions (
                id integer PRIMARY KEY,
                position text NOT NULL,
                depth integer NOT NULL,
                parent_id integer NOT NULL,
                parent_move text NOT NULL)
            """)

    start = int(round(time.time() * 1000))
    pos_vals = generate_positions(Cube(), GROUP_TEST)
    end = int(round(time.time() * 1000))

    total = (end - start)/1000
    print("Total Time: " + str(total))

    print("Inserting...")

    for value in pos_vals:
        print(len(value))
        for p in value:
            db.query("INSERT INTO positions VALUES (?, ?, ?, ?, ?)", (p.id, p.position, p.depth, p.parent_id, str(p.parent_move)))

    db.commit()

    end = int(round(time.time() * 1000))

    total = (end - start)/1000
    print("Total Time: " + str(total))

    # from symmetry_checker import check_symmetry
    #
    # cube1 = Cube()
    # r2(cube1)
    # not_d(cube1)
    #
    # cube2 = Cube()
    # x2(cube2)
    # r2(cube2)
    # not_d(cube2)
    #
    # check_symmetry(cube1.position, cube2.position)


if __name__ == "__main__":
    main()