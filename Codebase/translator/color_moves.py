from cube.cube_class import Color
from translator import translator_moves


"""
The following methods are for moving a face nominated by its color, regardless of that faces current location.
This allows the cube to be rotated to match the robot's needs but still have the correct sequence performed on it.
:param cube: The temporary Cube
"""


def white(cube, verbose):
    method_id = get_face_method_id(cube, Color.WHITE)
    translate_move(cube, method_id, verbose)


def not_white(cube, verbose):
    method_id = get_face_method_id(cube, Color.WHITE, True)
    translate_move(cube, method_id, verbose)


def white2(cube, verbose):
    method_id = get_face_method_id(cube, Color.WHITE, True, True)
    translate_move(cube, method_id, verbose)


def yellow(cube, verbose):
    method_id = get_face_method_id(cube, Color.YELLOW)
    translate_move(cube, method_id, verbose)


def not_yellow(cube, verbose):
    method_id = get_face_method_id(cube, Color.YELLOW, True)
    translate_move(cube, method_id, verbose)


def yellow2(cube, verbose):
    method_id = get_face_method_id(cube, Color.YELLOW, True, True)
    translate_move(cube, method_id, verbose)


def green(cube, verbose):
    method_id = get_face_method_id(cube, Color.GREEN)
    translate_move(cube, method_id, verbose)


def not_green(cube, verbose):
    method_id = get_face_method_id(cube, Color.GREEN, True)
    translate_move(cube, method_id, verbose)


def green2(cube, verbose):
    method_id = get_face_method_id(cube, Color.GREEN, True, True)
    translate_move(cube, method_id, verbose)


def blue(cube, verbose):
    method_id = get_face_method_id(cube, Color.BLUE)
    translate_move(cube, method_id, verbose)


def not_blue(cube, verbose):
    method_id = get_face_method_id(cube, Color.BLUE, True)
    translate_move(cube, method_id, verbose)


def blue2(cube, verbose):
    method_id = get_face_method_id(cube, Color.BLUE, True, True)
    translate_move(cube, method_id, verbose)


def red(cube, verbose):
    method_id = get_face_method_id(cube, Color.RED)
    translate_move(cube, method_id, verbose)


def not_red(cube, verbose):
    method_id = get_face_method_id(cube, Color.RED, True)
    translate_move(cube, method_id, verbose)


def red2(cube, verbose):
    method_id = get_face_method_id(cube, Color.RED, True, True)
    translate_move(cube, method_id, verbose)


def orange(cube, verbose):
    method_id = get_face_method_id(cube, Color.ORANGE)
    translate_move(cube, method_id, verbose)


def not_orange(cube, verbose):
    method_id = get_face_method_id(cube, Color.ORANGE, True)
    translate_move(cube, method_id, verbose)


def orange2(cube, verbose):
    method_id = get_face_method_id(cube, Color.ORANGE, True, True)
    translate_move(cube, method_id, verbose)


def x(cube, verbose):
    translate_move(cube, 'x', verbose)


def x2(cube, verbose):
    translate_move(cube, 'x2', verbose)


def y(cube, verbose):
    translate_move(cube, 'y', verbose)


def y2(cube, verbose):
    translate_move(cube, 'y2', verbose)


def not_y(cube, verbose):
    translate_move(cube, 'not_y', verbose)


"""
These methods are used in determining which face should be moved, and actuating that movement
"""


def get_face_method_id(cube, color, negative_flag=False, double_flag=False):
    """
    Turns the color back into the face for movement
    :param cube: Temporary Cube being used to generate the robot sequence
    :param color: The color used to find the face
    :param negative_flag: Boolean to say if it's a counterclockwise turn
    :param double_flag: Boolean to say if its a half turn
    :return: the ID of the method in the translate_moves file (e.g. u, d, not_r, l2)
    """
    method_id = cube.get_face_with_color(color=color).name[0].lower()

    if double_flag:
        method_id += '2'
        return method_id

    if negative_flag:
        method_id = 'not_' + method_id
    return method_id


def translate_move(cube, method_id, verbose):
    """
    Translates a human move (UDLRFB etc.) into robot-compatible sequences
    :param cube: Temporary Cube being used to generate the robot sequence
    :param method_id: The ID
    """
    move_method = getattr(translator_moves, method_id)
    move_method(cube, verbose)
