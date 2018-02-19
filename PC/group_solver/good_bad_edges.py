from cube.cube_class import Cube, EDGES, Color, Side


def detect_bad_cubies(position):
    for e, f in EDGES:
        cubie_color = [Color(position[c]) for c in (e, f)]

        good = on_correct_face(position, cubie_color[0], e) or \
               on_correct_face(position, cubie_color[1], f) or \
               on_opposite_face(position, cubie_color[0], e) or \
               on_opposite_face(position, cubie_color[1], f) or \
               on_adjacent_slice(position, cubie_color[0], e) or \
               on_adjacent_slice(position, cubie_color[1], f)

        if not good:
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
