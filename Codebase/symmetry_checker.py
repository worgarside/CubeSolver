from cube.color_class import Color as COLOR
from cube.cube_class import Cube

OPPOSITE_FACE_DICT = {
    COLOR.WHITE: COLOR.YELLOW,
    COLOR.YELLOW: COLOR.WHITE,
    COLOR.ORANGE: COLOR.RED,
    COLOR.RED: COLOR.ORANGE,
    COLOR.GREEN: COLOR.BLUE,
    COLOR.BLUE: COLOR.GREEN
}


def check_symmetry(orig_position, second_position):
    check_colour_rotation(orig_position,second_position)
    check_reflection(orig_position, second_position)
    check_cube_rotation(orig_position, second_position)


def check_colour_rotation(orig_position, second_position):
    print(Cube(orig_position).color_position)
    print(Cube(second_position).color_position)

    orig_colors = []
    orig_pos_coded = ""
    second_colors = []
    second_pos_coded = ""

    for orig, second in zip(orig_position, second_position):
        if orig not in orig_colors:
            orig_colors.append(orig)
        if second not in second_colors:
            second_colors.append(second)

        orig_pos_coded += str(orig_colors.index(orig))
        second_pos_coded += str(second_colors.index(second))


def check_reflection(orig_position, second_position):
    pass


def check_cube_rotation(orig_position, second_position):
    pass