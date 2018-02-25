from collections import Counter

from cube.color_class import Color
from cube.cube_class import Cube
from cube.move_class import Move
from cube.moves import dyn_move
from cube.position_class import Position  # (pos_id, position, depth, move_sequence)

EDGES_NO_UP_DOWN = [(19, 19), (10, 10), (16, 16), (13, 13),
                    (21, 32), (23, 24), (26, 27), (29, 30),
                    (34, 34), (37, 37), (40, 40), (43, 43)]

FACELETS = [1, 3, 5, 7, 24, 26, 30, 32, 46, 48, 50, 52]

MOVE_GROUP = [Move.U, Move.D, Move.L, Move.R, Move.F, Move.B]

OPPOSITE_MOVE_DICT = {
    Move.U: Move.D,
    Move.D: Move.U,
    Move.L: Move.R,
    Move.R: Move.L,
    Move.F: Move.B,
    Move.B: Move.F,
}


def gen_phase_one_sequence(position):
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
                    if cube_is_good(c.position, solved_facelets):
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
