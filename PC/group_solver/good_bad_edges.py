from multiprocessing import Pool

from cube.color_class import Color
from cube.cube_class import Cube
from cube.move_class import Move
from cube.moves import dyn_move
from cube.position_class import Position  # (pos_id, position, depth, move_chain)
from cube.side_class import Side

EDGES_NO_UP_DOWN = [(19, 19), (10, 10), (16, 16), (13, 13),
                    (21, 32), (23, 24), (26, 27), (29, 30),
                    (34, 34), (37, 37), (40, 40), (43, 43)]

MOVE_GROUP = [Move.U, Move.D, Move.L, Move.R, Move.F, Move.B, Move.NOT_L, Move.NOT_R, Move.NOT_F, Move.NOT_B]

OPPOSITE_MOVE_DICT = {
    Move.U: Move.D,
    Move.NOT_U: Move.NOT_D,
    Move.D: Move.U,
    Move.NOT_D: Move.NOT_U,
    Move.L: Move.R,
    Move.NOT_L: Move.NOT_R,
    Move.R: Move.L,
    Move.NOT_R: Move.NOT_L,
    Move.F: Move.B,
    Move.NOT_F: Move.NOT_B,
    Move.B: Move.F,
    Move.NOT_B: Move.NOT_F,
}


position_set = set()

def make_all_edges_good(position):
    global position_set

    positions = {}  # depth: set(position)

    pos_id = 0
    depth = 0

    positions[depth] = [Position(0, position, depth, [Move.NONE])]

    if cube_is_good(position):
        return Position(0, position, depth, [])

    while depth < 8:
        positions[depth + 1] = []
        for p in positions[depth]:
            # POOL HERE
            # pool = Pool()
            for m in MOVE_GROUP:
                try:
                    pos_id, new_pos_obj, new_pos_str, good_flag = process_move(p, m, depth, pos_id)
                    if not good_flag:
                        positions[depth + 1].append(new_pos_obj)
                        position_set.add(new_pos_str)
                    else:
                        return new_pos_obj
                except TypeError:
                    pass


        depth += 1
        print(depth)

    print('FAIL')


def process_move(p, m, depth, pos_id):
    global position_set

    c = Cube(p.position)
    dyn_move(c, m)

    # avoids Half Turns or Extended Half Turns
    if p.move_chain[-1] == m or (p.move_chain[-1] == OPPOSITE_MOVE_DICT[m] and p.move_chain[-2] == m):
        return

    if cube_is_good(c.position):
        new_id = pos_id + 1
        return new_id, Position(new_id, c.position, depth + 1, p.move_chain + [m]), c.position, True

    if c.position not in position_set:
        new_id = pos_id + 1
        return new_id, Position(new_id, c.position, depth + 1, p.move_chain + [m]), c.position, False


def cube_is_good(position):
    """
    Return whether or not all edge cubies are GOOD
    All 3 variables are checked out of necessity, however the continues reduce computational time
    :param position:
    :return:
    """
    for e, f in EDGES_NO_UP_DOWN:
        cubie_color = [Color(position[c]) for c in (e, f)]

        good_correct_face = on_correct_face(position, cubie_color[0], e) or \
                            on_correct_face(position, cubie_color[1], f)

        if good_correct_face:
            continue

        good_opposite_face = on_opposite_face(position, cubie_color[0], e) or \
                             on_opposite_face(position, cubie_color[1], f)

        if good_opposite_face:
            continue

        good_adjacent_slice = on_adjacent_slice(position, cubie_color[0], e) or \
                              on_adjacent_slice(position, cubie_color[1], f)

        if not good_adjacent_slice:
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
