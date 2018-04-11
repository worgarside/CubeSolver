from cube.cube_class import Color
from translator import all_moves as s_move


# Returns a tertiary method_id mainly based on color
def get_face(cube, color, negative_flag=False, double_flag=False):
    method_id = cube.get_face_with_color(color=color).name[0].lower()

    if double_flag:
        method_id += '2'
        return method_id

    if negative_flag:
        method_id = 'not_' + method_id
    return method_id


# Runs a secondary move on a virtual cube to split it down into its composite tertiary moves
def run_s_move(cube, color, method_id):
    try:
        move_method = getattr(s_move, method_id)
        move_method(cube)
    except AttributeError as e:
        print('s_move.' + color.name.lower() + ' failed: \'' + method_id + '\' | ' + str(e))
        exit()


"""
The following methods are for moving a face nominated by its color, regardless of that faces current location.
This allows the cube to be rotated to match the robot's needs but still have the correct sequence performed on it.
"""


def white(cube):
    method_id = get_face(cube, Color.WHITE)
    run_s_move(cube, Color.WHITE, method_id)


def not_white(cube):
    method_id = get_face(cube, Color.WHITE, True)
    run_s_move(cube, Color.WHITE, method_id)


def white2(cube):
    method_id = get_face(cube, Color.WHITE, True, True)
    run_s_move(cube, Color.WHITE, method_id)


def yellow(cube):
    method_id = get_face(cube, Color.YELLOW)
    run_s_move(cube, Color.YELLOW, method_id)


def not_yellow(cube):
    method_id = get_face(cube, Color.YELLOW, True)
    run_s_move(cube, Color.YELLOW, method_id)


def yellow2(cube):
    method_id = get_face(cube, Color.YELLOW, True, True)
    run_s_move(cube, Color.YELLOW, method_id)


def green(cube):
    method_id = get_face(cube, Color.GREEN)
    run_s_move(cube, Color.GREEN, method_id)


def not_green(cube):
    method_id = get_face(cube, Color.GREEN, True)
    run_s_move(cube, Color.GREEN, method_id)


def green2(cube):
    method_id = get_face(cube, Color.GREEN, True, True)
    run_s_move(cube, Color.GREEN, method_id)


def blue(cube):
    method_id = get_face(cube, Color.BLUE)
    run_s_move(cube, Color.BLUE, method_id)


def not_blue(cube):
    method_id = get_face(cube, Color.BLUE, True)
    run_s_move(cube, Color.BLUE, method_id)


def blue2(cube):
    method_id = get_face(cube, Color.BLUE, True, True)
    run_s_move(cube, Color.BLUE, method_id)


def red(cube):
    method_id = get_face(cube, Color.RED)
    run_s_move(cube, Color.RED, method_id)


def not_red(cube):
    method_id = get_face(cube, Color.RED, True)
    run_s_move(cube, Color.RED, method_id)


def red2(cube):
    method_id = get_face(cube, Color.RED, True, True)
    run_s_move(cube, Color.RED, method_id)


def orange(cube):
    method_id = get_face(cube, Color.ORANGE)
    run_s_move(cube, Color.ORANGE, method_id)


def not_orange(cube):
    method_id = get_face(cube, Color.ORANGE, True)
    run_s_move(cube, Color.ORANGE, method_id)


def orange2(cube):
    method_id = get_face(cube, Color.ORANGE, True, True)
    run_s_move(cube, Color.ORANGE, method_id)


def x(cube):
    run_s_move(cube, Color.NONE, 'x')


def x2(cube):
    run_s_move(cube, Color.NONE, 'x2')


def y(cube):
    run_s_move(cube, Color.NONE, 'y')


def y2(cube):
    run_s_move(cube, Color.NONE, 'y2')


def not_y(cube):
    run_s_move(cube, Color.NONE, 'not_y')
