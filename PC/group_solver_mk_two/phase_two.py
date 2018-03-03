from multiprocessing import Pool
import json
from sqlite3 import IntegrityError
from cube.color_class import Color
from cube.cube_class import Cube
from cube.move_class import Move
from cube.moves import dyn_move
from cube.position_class import Position  # (pos_id, position, depth, move_sequence)
from cube.side_class import Side

FACELETS = [i for i in range(9)] + [i for i in range(45, 54)]

MOVE_GROUP = [Move.U, Move.D, Move.L, Move.R, Move.F2, Move.B2]
MOVE_GROUP_CCW = [Move.NOT_U, Move.NOT_D, Move.NOT_L, Move.NOT_R, Move.F2, Move.B2]

SOLVED_MONOCHROME = 'DDDDDDDDDNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNDDDDDDDDD'

OPPOSITE_MOVE_DICT = {Move.U: Move.D, Move.D: Move.U, Move.L: Move.R, Move.R: Move.L, Move.U2: Move.D2,
                      Move.D2: Move.U2, Move.L2: Move.R2, Move.R2: Move.L2, Move.F2: Move.B2, Move.B2: Move.F2, }


def find_sequence_in_table(db, position):
    inversion_dict = {Move.U: Move.NOT_U, Move.D: Move.NOT_D, Move.L: Move.NOT_L, Move.R: Move.NOT_R,
                      Move.NOT_U: Move.U, Move.NOT_D: Move.D, Move.NOT_L: Move.L, Move.NOT_R: Move.R}
    monochrome_pos = _color_to_monochrome(position)
    orig_sequence = json.loads(
        db.query("SELECT move_sequence FROM gs2p2 where position = '%s'" % monochrome_pos).fetchone()[0])

    reverse_sequence = orig_sequence[::-1]

    inverted_sequence = []
    for move in reverse_sequence:
        inverted_sequence.append(inversion_dict.get(move, move))

    return inverted_sequence


# def generate_lookup_table(db):
#     db.query('DROP TABLE IF EXISTS gs2p2')
#
#     db.query('''CREATE TABLE IF NOT EXISTS gs2p2 (
#                     depth INTEGER NOT NULL,
#                     position TEXT PRIMARY KEY,
#                     move_sequence BLOB NOT NULL)
#                 ''')
#
#     count = 0
#     print(' - Generating Table... -')
#     position_set = {SOLVED_MONOCHROME}
#     position_dict = {}  # depth: set(position)
#     depth = 0
#     position_dict[depth] = [Position(depth, SOLVED_MONOCHROME, [Move.NONE])]
#
#     while depth < 7: # 10
#         depth += 1
#         print(depth, end='... ')
#
#         position_dict[depth] = []
#         for p in position_dict[depth-1]:
#             for m in MOVE_GROUP_CCW:
#
#                 c = Cube(p.position, True)
#                 dyn_move(c, m)
#
#                 if c.position not in position_set:
#                     count += 1
#                     position_dict[depth].append(Position(depth, c.position, p.move_sequence + [m.value]))
#                     position_set.add(c.position)
#
#
#
#     for positions in position_dict.values():
#         for position in positions:
#             db.query('INSERT INTO gs2p2 VALUES (?, ?, ?)',
#                      (position.depth, position.position, json.dumps(position.move_sequence[1:])))
#     db.commit()
#     print()




def generate_lookup_table(db):
    db.query('DROP TABLE IF EXISTS gs2p2')

    db.query('''CREATE TABLE IF NOT EXISTS gs2p2 (
                    depth INTEGER NOT NULL,
                    position TEXT PRIMARY KEY,
                    move_sequence BLOB NOT NULL)
                ''')

    print(' - Generating Table... -')
    position_dict = {}  # depth: set(position)
    depth = 0
    position_dict[depth] = [(depth, SOLVED_MONOCHROME, [Move.NONE])]
    db.query('INSERT INTO gs2p2 VALUES (?, ?, ?)', (depth, SOLVED_MONOCHROME, json.dumps([])))

    p = Pool(processes=4)
    insert_count = 1

    while insert_count > 0:
        insert_count = 0
        depth += 1
        print(depth, end='.')
        pos_list = db.query('SELECT position, move_sequence FROM gs2p2 where depth = %i' % (depth - 1)).fetchall()
        pool_result = p.map(gen_next_level, pos_list)
        print('.', end='')
        for result in pool_result:
            for r in result:
                try:
                    db.query('INSERT INTO gs2p2 VALUES (?, ?, ?)', (depth, r[0], json.dumps(r[1])))
                    insert_count += 1
                except IntegrityError:
                    pass
                    # print('\n\nIntegrity Error inserting %s into database' % str(r))
                    # exit()
        print('.', end=' ')
        db.commit()
    print()
    p.close()







def gen_next_level(pos_tuple):
    result_list = []
    for m in MOVE_GROUP_CCW:
        c = Cube(pos_tuple[0], True)
        dyn_move(c, m)
        result_list.append((c.position, json.loads(pos_tuple[1]) + [m.value]))

    return result_list







def gen_phase_two_sequence(position):
    count = 0
    print(' - Phase 2 - - - - - - -')
    position_set = {SOLVED_MONOCHROME}
    positions = {}  # depth: set(position)
    depth = 0

    solved_facelets = []
    for f in FACELETS:
        solved_facelets.append(Cube(position).get_color_of_side(facelet=f))

    positions[depth] = [Position(depth, position, [Move.NONE])]
    if position == SOLVED_MONOCHROME:
        return []

    while depth <= 10:
        print('%i... ' % depth, end='')
        positions[depth + 1] = []
        for p in positions[depth]:
            for m in MOVE_GROUP:

                c = Cube(p.position, True)
                dyn_move(c, m)

                if c.position not in position_set:
                    count += 1
                    if c.position == SOLVED_MONOCHROME:
                        print('Count: %i' % count)
                        return p.move_sequence[1:] + [m]
                    positions[depth + 1].append(Position(depth, c.position, p.move_sequence + [m]))
                    position_set.add(c.position)

        depth += 1
    print('FAIL')


def _color_to_monochrome(position):
    color_dict = {
        Side.UP: Cube(position).get_color_of_side(side=Side.UP),
        Side.DOWN: Cube(position).get_color_of_side(side=Side.DOWN),
    }

    monochrome_pos = ''
    for index, facelet in enumerate(position):
        if Color(facelet) in {color_dict[Side.UP], color_dict[Side.DOWN]}:
            monochrome_pos += Color.DARK.value
        else:
            monochrome_pos += Color.NONE.value

    return monochrome_pos
