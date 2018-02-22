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
    position_set = set()
    positions = {}  # depth: set(position)
    depth = 0

    l_r_colors = (Cube(position).get_color_of_side(side=Side.LEFT), Cube(position).get_color_of_side(side=Side.RIGHT))

    positions[depth] = [Position(position, [Move.NONE])]
    if cube_is_good(position, l_r_colors):
        return Position(position, [])

    while depth < 11:
        print('D%i' % depth)
        positions[depth + 1] = []
        for p in positions[depth]:
            for m in MOVE_GROUP:
                # avoids Half Turns or Extended Half Turns
                if p.move_sequence[-1] == m or (p.move_sequence[-1] == OPPOSITE_MOVE_DICT[m] and p.move_sequence[-2] == m):
                    continue

                c = Cube(p.position, True)
                dyn_move(c, m)

                if c.position not in position_set:
                    if cube_is_good(c.position, l_r_colors):
                        return Position(c.position, p.move_sequence + [m])
                    positions[depth + 1].append(Position(c.position, p.move_sequence + [m]))
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


def on_correct_face(position, facelet, location):
    face_color = Cube.get_color_of_side(Cube(position), facelet=location)

    return facelet == face_color


def on_opposite_face(position, facelet, location):
    current_side = Cube().facelet_side_dict[location]
    opposite_side = Cube().opposite_sides_dict[current_side]
    opposite_color = Cube.get_color_of_side(Cube(position), side=opposite_side)

    return facelet == opposite_color


def on_adjacent_slice(position, facelet, location):
    # Ignoring UP and DOWN face for now, hopefully these will be automatically rectified
    adj_dict = {Side.FRONT: [3, 5, 48, 50], Side.BACK: [3, 5, 48, 50],
                Side.LEFT: [1, 7, 46, 52], Side.RIGHT: [1, 7, 46, 52],
                Side.UP: [], Side.DOWN: []}

    current_side = Cube(position).get_side_with_color(color=facelet)

    return location in adj_dict[current_side]
