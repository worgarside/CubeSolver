from thistlethwaite.position_generator import generate_positions
import time
from cube.moves import *
import datetime
from data.database_manager import DatabaseManager
from cube.cube_class import Cube
import winsound


GROUP_THREE = [MOVE.U2, MOVE.D2, MOVE.L2, MOVE.R2, MOVE.F2, MOVE.B2]
GROUP_TWO = [MOVE.U2, MOVE.D2, MOVE.L, MOVE.R, MOVE.F2, MOVE.B2]
GROUP_ONE = [MOVE.U2, MOVE.D2, MOVE.L, MOVE.R, MOVE.F, MOVE.B]
GROUP_ZERO = [MOVE.U, MOVE.D, MOVE.L, MOVE.R, MOVE.F, MOVE.B]

GROUP_TEST = [MOVE.U2, MOVE.D2, MOVE.L2, MOVE.R2, MOVE.F2, MOVE.B2]


def init_db():
    db = DatabaseManager('data/db.sqlite3')

    db.query("DROP TABLE IF EXISTS positions")

    db.query("""CREATE TABLE IF NOT EXISTS positions (
                    id integer PRIMARY KEY,
                    position text NOT NULL,
                    depth integer NOT NULL,
                    parent_id integer NOT NULL,
                    parent_move text NOT NULL)
                """)

    return db

def main():
    db = init_db()

    print("Start: " + datetime.datetime.now().strftime("%H:%M"))
    start = int(round(time.time() * 1000))
    pos = generate_positions(Cube(), GROUP_THREE)
    end = int(round(time.time() * 1000))
    total = (end - start)/1000
    print("Time: " + str(total))

    for p in pos:
        for q in p:
            db.query("INSERT INTO positions VALUES (?, ?, ?, ?, ?)", (q.id, q.position, q.depth, q.parent_id, str(q.parent_move)))

    db.commit()

    for i in range(1, 15):
        winsound.Beep(i*100, 100)


if __name__ == "__main__":
    main()
