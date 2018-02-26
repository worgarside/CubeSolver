import pickle

from cube.cube_class import Cube
from cube.move_class import Move
from cube.moves import dyn_move
from cube.position_class import Position  # (pos_id, position, depth, move_sequence)

MOVE_GROUP = [Move.U, Move.D, Move.L2, Move.R2, Move.F2, Move.B2]
MOVE_GROUP_CCW = [Move.NOT_U, Move.NOT_D, Move.L2, Move.R2, Move.F2, Move.B2]

SOLVED_POS = 'WWWWWWWWWOOOGGGRRRBBBOOOGGGRRRBBBOOOGGGRRRBBBYYYYYYYYY'

OPPOSITE_MOVE_DICT = {Move.U: Move.D, Move.D: Move.U, Move.L: Move.R, Move.R: Move.L, Move.U2: Move.D2,
                      Move.D2: Move.U2, Move.L2: Move.R2, Move.R2: Move.L2, Move.F2: Move.B2, Move.B2: Move.F2, }


def find_sequence_in_table(db, position):
    inversion_dict = {Move.U: Move.NOT_U, Move.D: Move.NOT_D, Move.NOT_U: Move.U, Move.NOT_D: Move.D}

    reduced_position = Cube(position).position_reduced
    orig_sequence = pickle.loads(
        db.query("SELECT move_sequence FROM gs2p5 where position = '%s'" % reduced_position).fetchone()[0])

    reverse_sequence = orig_sequence[::-1]

    inverted_sequence = []
    for move in reverse_sequence:
        inverted_sequence.append(inversion_dict.get(move, move))

    return inverted_sequence


def generate_lookup_table(db):
    db.query('DROP TABLE IF EXISTS gs2p5')

    db.query('''CREATE TABLE IF NOT EXISTS gs2p5 (
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
    tree_width = 1

    while tree_width > 0:
        tree_width = 0
        print(depth, end='... ')

        position_dict[depth + 1] = []
        for p in position_dict[depth]:
            for m in MOVE_GROUP_CCW:

                c = Cube(p.position, True)
                dyn_move(c, m)

                if c.position not in position_set:
                    count += 1
                    position_dict[depth + 1].append(Position(depth, c.position, p.move_sequence + [m]))
                    position_set.add(c.position)
                    tree_width += 1

        depth += 1

    for positions in position_dict.values():
        for position in positions:
            db.query('INSERT INTO gs2p5 VALUES (?, ?, ?)',
                     (position.depth, position.position, pickle.dumps(position.move_sequence[1:])))
    db.commit()


def generate_sequence(position):
    reduced_position = Cube(position).position_reduced
    count = 0
    print(' - Phase 5 - - - - - - -')
    position_set = {SOLVED_POS}
    positions = {}  # depth: set(position)
    depth = 0

    positions[depth] = [Position(depth, reduced_position, [Move.NONE])]
    if reduced_position == SOLVED_POS:
        return []

    while depth <= 18:
        print('%i... ' % depth, end='')
        positions[depth + 1] = []
        for p in positions[depth]:
            for m in MOVE_GROUP:

                c = Cube(p.position, True)
                dyn_move(c, m)

                if c.position not in position_set:
                    count += 1
                    if c.position == SOLVED_POS:
                        print('Count: %i' % count)
                        return p.move_sequence[1:] + [m]
                    positions[depth + 1].append(Position(depth, c.position, p.move_sequence + [m]))
                    position_set.add(c.position)

        depth += 1
    print('FAIL')
