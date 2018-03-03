import json
import pickle
from multiprocessing import Pool
from sqlite3 import IntegrityError

from cube.cube_class import Cube
from cube.move_class import Move
from cube.moves import dyn_move
from cube.position_class import Position  # (pos_id, position, depth, move_sequence)

MOVE_GROUP = [Move.U, Move.D, Move.L2, Move.R2, Move.F2, Move.B2]
MOVE_GROUP_CCW = [Move.NOT_U, Move.NOT_D, Move.L2, Move.R2, Move.F2, Move.B2]

SOLVED_REDUCED = 'WWWWWWWWWRRRBBBRRRBBBRRRBBBRRRBBBRRRBBBRRRBBBWWWWWWWWW'
SOLVED_POS = 'WWWWWWWWWOOOGGGRRRBBBOOOGGGRRRBBBOOOGGGRRRBBBYYYYYYYYY'

OPPOSITE_MOVE_DICT = {Move.U: Move.D, Move.D: Move.U, Move.L: Move.R, Move.R: Move.L, Move.U2: Move.D2,
                      Move.D2: Move.U2, Move.L2: Move.R2, Move.R2: Move.L2, Move.F2: Move.B2, Move.B2: Move.F2, }


def find_sequence_in_table(db, position):
    inversion_dict = {Move.U: Move.NOT_U, Move.D: Move.NOT_D, Move.NOT_U: Move.U, Move.NOT_D: Move.D}

    reduced_position = Cube(position).position_reduced
    orig_sequence = pickle.loads(
        db.query("SELECT move_sequence FROM gs2p4 where position = '%s'" % reduced_position).fetchone()[0])

    reverse_sequence = orig_sequence[::-1]

    inverted_sequence = []
    for move in reverse_sequence:
        inverted_sequence.append(inversion_dict.get(move, move))

    return inverted_sequence


def generate_lookup_table(db):
    db.query('DROP TABLE IF EXISTS gs2p4')

    db.query('''CREATE TABLE IF NOT EXISTS gs2p4 (
                    depth INTEGER NOT NULL,
                    position TEXT PRIMARY KEY,
                    move_sequence BLOB NOT NULL)
                ''')

    print(' - Generating Table... -')
    position_dict = {}  # depth: set(position)
    depth = 0
    position_dict[depth] = [(depth, SOLVED_POS, [Move.NONE])]
    db.query('INSERT INTO gs2p4 VALUES (?, ?, ?)', (depth, SOLVED_POS, json.dumps([])))

    p = Pool(processes=4)


    while depth < 5:
        depth += 1
        print(depth, end='.')
        pos_list = db.query('SELECT position, move_sequence FROM gs2p4 where depth = %i' % (depth - 1)).fetchall()
        pool_result = p.map(gen_next_level, pos_list)
        print('.', end='')
        for result in pool_result:
            for r in result:
                try:
                    db.query('INSERT INTO gs2p4 VALUES (?, ?, ?)', (depth, r[0], json.dumps(r[1])))
                except IntegrityError:
                    pass

        print('.', end=' ')

        db.commit()
    print()
    p.close()


def gen_next_level(n):
    result_list = []
    for m in MOVE_GROUP_CCW:
        c = Cube(n[0], True)
        dyn_move(c, m)
        result_list.append((c.position, json.loads(n[1]) + [m.value]))

    return result_list


def gen_phase_four_sequence(position):
    reduced_position = Cube(position).position_reduced
    count = 0
    print(' - Phase 4 - - - - - - -')
    position_set = {SOLVED_REDUCED}
    positions = {}  # depth: set(position)
    depth = 0

    positions[depth] = [Position(depth, reduced_position, [Move.NONE])]
    if reduced_position == SOLVED_REDUCED:
        return []

    while depth <= 8:
        print('%i... ' % depth, end='')
        positions[depth + 1] = []
        for p in positions[depth]:
            for m in MOVE_GROUP:

                c = Cube(p.position, True)
                dyn_move(c, m)

                if c.position not in position_set:
                    count += 1
                    if c.position == SOLVED_REDUCED:
                        print('Count: %i' % count)
                        return p.move_sequence[1:] + [m]
                    positions[depth + 1].append(Position(depth, c.position, p.move_sequence + [m]))
                    position_set.add(c.position)

        depth += 1
    print('FAIL')
