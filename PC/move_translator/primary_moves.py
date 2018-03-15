from cube.color_class import Color
from move_translator import secondary_moves as s_move


# Returns a tertiary method mainly based on color
def get_side_method(cube, color, negative_flag=False, double_flag=False):
    method = cube.get_side_with_color(color=color).name[0].lower()

    if double_flag:
        method += '2'
        return method
    
    if negative_flag:
        method = 'not_' + method
    return method


# Runs a secondary move on a virtual cube to split it down into its composite tertiary moves
def run_s_move(cube, color, method):
    try:
        move_method = getattr(s_move, method)
        move_method(cube)
    except AttributeError as e:
        print('s_move.' + color.name.lower() + ' failed: \'' + method + '\' | ' + str(e))
        exit()


"""
The following methods are for moving a side nominated by its color, regardless of that sides current location.
This allows the cube to be rotated to match the robot's needs but still have the correct sequence performed on it.
"""


def white(cube):
    method = get_side_method(cube, Color.WHITE)
    run_s_move(cube, Color.WHITE, method)


def not_white(cube):
    method = get_side_method(cube, Color.WHITE, True)
    run_s_move(cube, Color.WHITE, method)


def white2(cube):
    method = get_side_method(cube, Color.WHITE, True, True)
    run_s_move(cube, Color.WHITE, method)


def yellow(cube):
    method = get_side_method(cube, Color.YELLOW)
    run_s_move(cube, Color.YELLOW, method)


def not_yellow(cube):
    method = get_side_method(cube, Color.YELLOW, True)
    run_s_move(cube, Color.YELLOW, method)


def yellow2(cube):
    method = get_side_method(cube, Color.YELLOW, True, True)
    run_s_move(cube, Color.YELLOW, method)


def green(cube):
    method = get_side_method(cube, Color.GREEN)
    run_s_move(cube, Color.GREEN, method)


def not_green(cube):
    method = get_side_method(cube, Color.GREEN, True)
    run_s_move(cube, Color.GREEN, method)


def green2(cube):
    method = get_side_method(cube, Color.GREEN, True, True)
    run_s_move(cube, Color.GREEN, method)


def blue(cube):
    method = get_side_method(cube, Color.BLUE)
    run_s_move(cube, Color.BLUE, method)


def not_blue(cube):
    method = get_side_method(cube, Color.BLUE, True)
    run_s_move(cube, Color.BLUE, method)


def blue2(cube):
    method = get_side_method(cube, Color.BLUE, True, True)
    run_s_move(cube, Color.BLUE, method)


def red(cube):
    method = get_side_method(cube, Color.RED)
    run_s_move(cube, Color.RED, method)


def not_red(cube):
    method = get_side_method(cube, Color.RED, True)
    run_s_move(cube, Color.RED, method)


def red2(cube):
    method = get_side_method(cube, Color.RED, True, True)
    run_s_move(cube, Color.RED, method)


def orange(cube):
    method = get_side_method(cube, Color.ORANGE)
    run_s_move(cube, Color.ORANGE, method)


def not_orange(cube):
    method = get_side_method(cube, Color.ORANGE, True)
    run_s_move(cube, Color.ORANGE, method)


def orange2(cube):
    method = get_side_method(cube, Color.ORANGE, True, True)
    run_s_move(cube, Color.ORANGE, method)


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
