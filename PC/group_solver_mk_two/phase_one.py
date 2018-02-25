from collections import Counter

from cube.color_class import Color
from cube.cube_class import Cube
from cube.move_class import Move
from cube.moves import dyn_move
from cube.position_class import Position  # (pos_id, position, depth, move_sequence)
from cube.side_class import Side

FACELETS = [1, 3, 5, 7, 24, 26, 30, 32, 46, 48, 50, 52]

MOVE_GROUP = [Move.U, Move.D, Move.L, Move.R, Move.F, Move.B]
# MOVE_GROUP = [Move.U, Move.U2, Move.D, Move.D2, Move.L, Move.L2, Move.R, Move.R2, Move.F, Move.F2, Move.B, Move.B2]

SOLVED_MONOCHROME = 'NDNDNDNDNNNNNNNNNNNNNNNNDNDNNNDNDNNNNNNNNNNNNNDNDNDNDN'

OPPOSITE_MOVE_DICT = {
    Move.U: Move.D,
    Move.D: Move.U,
    Move.L: Move.R,
    Move.R: Move.L,
    Move.F: Move.B,
    Move.B: Move.F,
    Move.U2: Move.D2,
    Move.D2: Move.U2,
    Move.L2: Move.R2,
    Move.R2: Move.L2,
    Move.F2: Move.B2,
    Move.B2: Move.F2,
}


def color_to_monochrome(position):

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


def generate_phase_one_table(db):
    start_pos = 'NDNDNDNDNNNNNNNNNNNNNNNNDNDNNNDNDNNNNNNNNNNNNNDNDNDNDN'
    print(Cube(start_pos))

    # count = 0
    # print(' - Phase 1 - - - - - - -')
    # position_set = set()
    # positions = {}  # depth: set(position)
    # depth = 0
    #
    # solved_facelets = []
    # for f in FACELETS:
    #     solved_facelets.append(Cube(start_pos).get_color_of_side(facelet=f))
    #
    # positions[depth] = [Position(depth, start_pos, [Move.NONE])]
    #
    # while depth <= 7:
    #     print('%i... ' % depth, end='')
    #     positions[depth + 1] = []
    #     for p in positions[depth]:
    #         for m in MOVE_GROUP:
    #             # avoids Half Turns or Extended Half Turns
    #             # TODO: from basic tests, this seems to find a *larger* sequence but in a *shorter* time
    #             # if p.move_sequence[-1] == m or \
    #             #         (p.move_sequence[-1] == OPPOSITE_MOVE_DICT[m] and p.move_sequence[-2] == m):
    #             #     continue
    #
    #             c = Cube(p.position, True)
    #             dyn_move(c, m)
    #
    #             if c.position not in position_set:
    #                 count += 1
    #                 if cube_is_good(c.position, solved_facelets):
    #                     print('Count: %i' % count)
    #                     return p.move_sequence + [m]
    #                 positions[depth + 1].append(Position(depth, c.position, p.move_sequence + [m]))
    #                 position_set.add(c.position)
    #
    #     depth += 1
    # print('FAIL')


def gen_phase_one_sequence(position):
    count = 0
    print(' - Phase 1 - - - - - - -')
    position_set = set()
    positions = {}  # depth: set(position)
    depth = 0

    solved_facelets = []
    for f in FACELETS:
        solved_facelets.append(Cube(position).get_color_of_side(facelet=f))

    positions[depth] = [Position(depth, position, [Move.NONE])]
    if cube_is_good(position, solved_facelets):
        return [Move.NONE]

    while depth <= 7:
        print('%i... ' % depth, end='')
        positions[depth + 1] = []
        for p in positions[depth]:
            for m in MOVE_GROUP:
                # avoids Half Turns or Extended Half Turns
                # TODO: from basic tests, this seems to find a *larger* sequence but in a *shorter* time
                # if p.move_sequence[-1] == m or \
                #         (p.move_sequence[-1] == OPPOSITE_MOVE_DICT[m] and p.move_sequence[-2] == m):
                #     continue

                c = Cube(p.position, True)
                dyn_move(c, m)

                if c.position not in position_set:
                    count += 1
                    # if cube_is_good(c.position, solved_facelets):
                    if c.position == SOLVED_MONOCHROME:
                        print('Optimised Count: %i' % count)
                        return p.move_sequence + [m]
                    positions[depth + 1].append(Position(depth, c.position, p.move_sequence + [m]))
                    position_set.add(c.position)

        depth += 1
    print('FAIL')


def cube_is_good(position, solved_facelets):
    current_facelets = []
    for f in FACELETS:
        current_facelets.append(Color(position[f]))

    return compare(current_facelets, solved_facelets)


def compare(a, b):
    return Counter(a) == Counter(b)
