from cube.cube_class import Cube, Color, Side
from cube.moves import dyn_move
from cube.position_class import Position  # (pos_id, position, depth, move_chain)

EDGES_NO_UP_DOWN = [(19, 19), (10, 10), (16, 16), (13, 13),
                    (21, 32), (23, 24), (26, 27), (29, 30),
                    (34, 34), (37, 37), (40, 40), (43, 43)]


def make_all_edges_good(position, group):
    positions = {}  # depth: set(position)
    position_set = set()
    depth = 0
    id = 0

    positions[depth] = {Position(0, position, depth, [])}

    if cube_is_good(position):
        return Position(0, position, depth, [])

    while depth < 8:
        positions[depth + 1] = set()
        for p in positions[depth]:
            for m in group:
                c = Cube(p.position)
                dyn_move(c, m)

                if cube_is_good(c.position):
                    return Position(id, c.position, depth + 1, p.move_chain + [str(m)])

                if c.position not in position_set:
                    id += 1
                    positions[depth + 1].add(Position(id, c.position, depth + 1, p.move_chain + [str(m)]))
                    position_set.add(c.position)

        depth += 1
        print(depth)

    print('here now')


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
