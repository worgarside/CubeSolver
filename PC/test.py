import pickle

from cube.cube_class import Cube
from cube.move_class import Move
from cube.moves import dyn_move
from cube.position_class import Position  # (pos_id, position, depth, move_sequence)
from data.database_manager import DatabaseManager

MOVE_GROUP = [Move.U, Move.D, Move.L2, Move.R2, Move.F2, Move.B2]
MOVE_GROUP_CCW = [Move.NOT_U, Move.NOT_D, Move.L2, Move.R2, Move.F2, Move.B2]

SOLVED_REDUCED = 'WWWWWWWWWRRRBBBRRRBBBRRRBBBRRRBBBRRRBBBRRRBBBWWWWWWWWW'
SOLVED_POS = 'WWWWWWWWWOOOGGGRRRBBBOOOGGGRRRBBBOOOGGGRRRBBBYYYYYYYYY'

OPPOSITE_MOVE_DICT = {Move.U: Move.D, Move.D: Move.U, Move.L: Move.R, Move.R: Move.L, Move.U2: Move.D2,
                      Move.D2: Move.U2, Move.L2: Move.R2, Move.R2: Move.L2, Move.F2: Move.B2, Move.B2: Move.F2, }


def generate_lookup_table(db):
    db.query('DROP TABLE IF EXISTS gs2p4')

    db.query('''CREATE TABLE IF NOT EXISTS gs2p4 (
                    depth INTEGER NOT NULL,
                    position TEXT PRIMARY KEY,
                    move_sequence BLOB NOT NULL)
                ''')

    count = 0
    print(' - Generating Table... -')
    position_set = {SOLVED_POS}
    position_dict = {}  # depth: set(position)
    depth = 0
    position_dict[depth] = [Position(depth, SOLVED_POS, [Move.NONE])]

    while depth <= 2:
        depth += 1
        print(depth, end='.')

        position_dict[depth] = []
        for p in position_dict[depth - 1]:
            for m in MOVE_GROUP_CCW:

                c = Cube(p.position, True)
                dyn_move(c, m)

                if c.position not in position_set:
                    count += 1
                    position_dict[depth].append(Position(depth, c.position, p.move_sequence + [m]))
                    position_set.add(c.position)

        print('.', end='')
        for position in position_dict[depth]:
            db.query('INSERT INTO gs2p4 VALUES (?, ?, ?)',
                     (position.depth, position.position, pickle.dumps(position.move_sequence[1:])))
        db.commit()
        print('. ', end='')


if __name__ == '__main__':
    db = DatabaseManager('PC/data/db.sqlite')
    generate_lookup_table(db)