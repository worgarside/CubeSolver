from cube.color_class import Color
from cube.cube_class import Cube
from cube.move_class import Move
from cube.moves import dyn_move
from cube.position_class import Position  # (pos_id, position, depth, move_sequence)
from cube.side_class import Side

L_R_CORNERS = ([9,11,33,35],[15,17,39,41])

MOVE_GROUP = [Move.U2, Move.D2, Move.L, Move.R, Move.F, Move.B]

OPPOSITE_MOVE_DICT = {
    Move.U2: Move.D2,
    Move.D2: Move.U2,
    Move.L: Move.R,
    Move.R: Move.L,
    Move.F: Move.B,
    Move.B: Move.F,
}


def make_all_corners_good(position):
    print(' - Phase 2 - - - - - - -')
    position_set = set()
    positions = {}  # depth: set(position)
    depth = 0

    l_r_colors = (Cube(position).get_color_of_side(side=Side.LEFT), Cube(position).get_color_of_side(side=Side.RIGHT))

    positions[depth] = [Position(depth, position, [Move.NONE])]
    if cube_is_good(position, l_r_colors):
        return Position(depth, position, [])

    while depth < 11:
        print('%i... ' % depth, end='')
        positions[depth + 1] = []
        for p in positions[depth]:
            for m in MOVE_GROUP:
                # avoids Half Turns or Extended Half Turns
                if p.move_sequence[-1] == m or \
                        (p.move_sequence[-1] == OPPOSITE_MOVE_DICT[m] and p.move_sequence[-2] == m):
                    continue

                c = Cube(p.position, True)
                dyn_move(c, m)

                if c.position not in position_set:
                    if cube_is_good(c.position, l_r_colors):
                        return Position(depth, c.position, p.move_sequence + [m])
                    positions[depth + 1].append(Position(depth, c.position, p.move_sequence + [m]))
                    position_set.add(c.position)

        depth += 1
    print('FAIL')


def cube_is_good(position, l_r_colors):

    for side_num, facelets in enumerate(L_R_CORNERS):
        for facelet in facelets:
            facelet_color = Color(position[facelet])
            if facelet_color != l_r_colors[side_num]:
                return False
    return True
