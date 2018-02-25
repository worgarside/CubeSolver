from collections import Counter

from cube.color_class import Color
from cube.cube_class import Cube
from cube.move_class import Move
from cube.moves import dyn_move
from cube.position_class import Position  # (pos_id, position, depth, move_sequence)

FACELETS = [i for i in range(9)] + [i for i in range(45, 54)]

MOVE_GROUP = [Move.U, Move.D, Move.L, Move.R, Move.F2, Move.B2]
# MOVE_GROUP = [Move.U, Move.U2, Move.D, Move.D2, Move.L, Move.L2, Move.R, Move.R2, Move.F2, Move.B2]

OPPOSITE_MOVE_DICT = {
    Move.U: Move.D,
    Move.D: Move.U,
    Move.L: Move.R,
    Move.R: Move.L,
    Move.U2: Move.D2,
    Move.D2: Move.U2,
    Move.L2: Move.R2,
    Move.R2: Move.L2,
    Move.F2: Move.B2,
    Move.B2: Move.F2,
}


def gen_phase_two_sequence(position):
    count = 0
    print(' - Phase 2 - - - - - - -')
    position_set = set()
    positions = {}  # depth: set(position)
    depth = 0

    solved_facelets = []
    for f in FACELETS:
        solved_facelets.append(Cube(position).get_color_of_side(facelet=f))

    positions[depth] = [Position(depth, position, [Move.NONE])]
    if cube_is_good(position, solved_facelets):
        return [Move.NONE]

    while depth <= 10:
        print('%i... ' % depth, end='')
        positions[depth + 1] = []
        for p in positions[depth]:
            for m in MOVE_GROUP:
                # avoids Half Turns or Extended Half Turns
                # if p.move_sequence[-1] == m or \
                #         (p.move_sequence[-1] == OPPOSITE_MOVE_DICT[m] and p.move_sequence[-2] == m):
                #     continue

                c = Cube(p.position, True)
                dyn_move(c, m)

                if c.position not in position_set:
                    count += 1
                    if cube_is_good(c.position, solved_facelets):
                        print('Count: %i' % count)
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
