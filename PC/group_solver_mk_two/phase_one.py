import pickle

from cube.color_class import Color
from cube.cube_class import Cube
from cube.move_class import Move
from cube.moves import dyn_move
from cube.position_class import Position  # (position, depth, move_sequence)
from cube.side_class import Side

MOVE_GROUP_CW = [Move.U, Move.D, Move.L, Move.R, Move.F, Move.B]
MOVE_GROUP_CCW = [Move.NOT_U, Move.NOT_D, Move.NOT_L, Move.NOT_R, Move.NOT_F, Move.NOT_B]

SOLVED_MONOCHROME = 'NDNDNDNDNNNNNNNNNNNNNNNNDNDNNNDNDNNNNNNNNNNNNNDNDNDNDN'

OPPOSITE_MOVE_DICT = {Move.U: Move.D, Move.D: Move.U, Move.L: Move.R, Move.R: Move.L, Move.F: Move.B, Move.B: Move.F,
                      Move.U2: Move.D2, Move.D2: Move.U2, Move.L2: Move.R2, Move.R2: Move.L2, Move.F2: Move.B2,
                      Move.B2: Move.F2, }


def find_sequence_in_table(db, position):
    inversion_dict = {
        Move.U: Move.NOT_U, Move.D: Move.NOT_D, Move.L: Move.NOT_L, Move.R: Move.NOT_R, Move.F: Move.NOT_F,
        Move.B: Move.NOT_B, Move.NOT_U: Move.U, Move.NOT_D: Move.D, Move.NOT_L: Move.L, Move.NOT_R: Move.R,
        Move.NOT_F: Move.F, Move.NOT_B: Move.B, }
    monochrome_pos = _color_to_monochrome(position)
    orig_sequence = pickle.loads(
        db.query("SELECT move_sequence FROM gs2p1 where position = '%s'" % monochrome_pos).fetchone()[0])

    reverse_sequence = orig_sequence[::-1]

    inverted_sequence = []
    for move in reverse_sequence:
        inverted_sequence.append(inversion_dict[move])

    return inverted_sequence


def generate_phase_one_table(db):
    db.query('DROP TABLE IF EXISTS gs2p1')

    db.query('''CREATE TABLE IF NOT EXISTS gs2p1 (
                    depth INTEGER NOT NULL,
                    position TEXT PRIMARY KEY,
                    move_sequence BLOB NOT NULL)
                ''')

    count = 0
    print(' - Generating Table... -')
    position_set = {SOLVED_MONOCHROME}
    position_dict = {}  # depth: set(position)
    depth = 0
    position_dict[depth] = [Position(depth, SOLVED_MONOCHROME, [Move.NONE])]

    while depth <= 7:
        print('%i... ' % depth, end='')

        position_dict[depth + 1] = []
        for p in position_dict[depth]:
            for m in MOVE_GROUP_CCW:

                c = Cube(p.position, True)
                dyn_move(c, m)

                if c.position not in position_set:
                    count += 1
                    position_dict[depth + 1].append(Position(depth, c.position, p.move_sequence + [m]))
                    position_set.add(c.position)

        depth += 1

    for positions in position_dict.values():
        for position in positions:
            db.query('INSERT INTO gs2p1 VALUES (?, ?, ?)',
                     (position.depth, position.position, pickle.dumps(position.move_sequence[1:])))
    db.commit()


def gen_phase_one_sequence(color_pos):
    position = _color_to_monochrome(color_pos)
    count = 0
    print(' - Phase 1 - - - - - - -')
    position_set = {SOLVED_MONOCHROME}
    positions = {}  # depth: set(position)
    depth = 0

    positions[depth] = [Position(depth, position, [Move.NONE])]
    if position == SOLVED_MONOCHROME:
        return []

    while depth <= 7:
        print('%i... ' % depth, end='')
        positions[depth + 1] = []
        for p in positions[depth]:
            for m in MOVE_GROUP_CW:
                # avoids Half Turns or Extended Half Turns
                # TODO: from basic tests, this seems to find a *larger* sequence but in a *shorter* time
                # if p.move_sequence[-1] == m or \
                #         (p.move_sequence[-1] == OPPOSITE_MOVE_DICT[m] and p.move_sequence[-2] == m):
                #     continue

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
        Side.FRONT: Cube(position).get_color_of_side(side=Side.FRONT),
        Side.BACK: Cube(position).get_color_of_side(side=Side.BACK),
    }

    adjacent = {1: 19, 3: 10, 5: 16, 7: 13, 10: 3, 13: 7, 16: 5, 19: 1, 21: 32, 23: 24, 24: 23, 26: 27, 27: 26,
                29: 30, 30: 29, 32: 21, 34: 48, 37: 46, 40: 50, 43: 52, 46: 37, 48: 34, 50: 40, 52: 43, }

    monochrome_pos = ''
    for index, facelet in enumerate(position):
        if index in adjacent:
            if Color(facelet) in {color_dict[Side.UP], color_dict[Side.DOWN]}:
                monochrome_pos += Color.DARK.value
            elif Color(facelet) in {color_dict[Side.FRONT], color_dict[Side.BACK]} \
                    and Color(position[adjacent[index]]) not in {color_dict[Side.UP], color_dict[Side.DOWN]}:
                monochrome_pos += Color.DARK.value
            else:
                monochrome_pos += Color.NONE.value
        else:
            monochrome_pos += Color.NONE.value

    return monochrome_pos
