from cube.color_class import Color
from robot import secondary_moves as s_move


# Returns a tertiary method mainly based on color
def get_tertiary_method(self, color, negative_flag=False, double_flag=False):
    method = self.get_side_with_color(color=color).name[0].lower()

    if double_flag:
        method += '2'
        return method
    
    if negative_flag:
        method = 'not_' + method
    return method


# Runs a secondary move on a virtual cube to split it down into its composite tertiary moves
def run_s_move(self, color, method):
    try:
        move_method = getattr(s_move, method)
        move_method(self)
    except AttributeError as e:
        print('s_move.' + color.name.lower() + ' failed: \'' + method + '\' | ' + str(e))
        exit()


"""
The following methods are for moving a side nominated by its color, regardless of that sides current location.
This allows the cube to be rotated to match the robot's needs but still have the correct sequence performed on it.
"""


def white(self):
    method = get_tertiary_method(self, Color.WHITE)
    run_s_move(self, Color.WHITE, method)


def not_white(self):
    method = get_tertiary_method(self, Color.WHITE, True)
    run_s_move(self, Color.WHITE, method)


def white2(self):
    method = get_tertiary_method(self, Color.WHITE, True, True)
    run_s_move(self, Color.WHITE, method)


def yellow(self):
    method = get_tertiary_method(self, Color.YELLOW)
    run_s_move(self, Color.YELLOW, method)


def not_yellow(self):
    method = get_tertiary_method(self, Color.YELLOW, True)
    run_s_move(self, Color.YELLOW, method)


def yellow2(self):
    method = get_tertiary_method(self, Color.YELLOW, True, True)
    run_s_move(self, Color.YELLOW, method)


def green(self):
    method = get_tertiary_method(self, Color.GREEN)
    run_s_move(self, Color.GREEN, method)


def not_green(self):
    method = get_tertiary_method(self, Color.GREEN, True)
    run_s_move(self, Color.GREEN, method)


def green2(self):
    method = get_tertiary_method(self, Color.GREEN, True, True)
    run_s_move(self, Color.GREEN, method)


def blue(self):
    method = get_tertiary_method(self, Color.BLUE)
    run_s_move(self, Color.BLUE, method)


def not_blue(self):
    method = get_tertiary_method(self, Color.BLUE, True)
    run_s_move(self, Color.BLUE, method)


def blue2(self):
    method = get_tertiary_method(self, Color.BLUE, True, True)
    run_s_move(self, Color.BLUE, method)


def red(self):
    method = get_tertiary_method(self, Color.RED)
    run_s_move(self, Color.RED, method)


def not_red(self):
    method = get_tertiary_method(self, Color.RED, True)
    run_s_move(self, Color.RED, method)


def red2(self):
    method = get_tertiary_method(self, Color.RED, True, True)
    run_s_move(self, Color.RED, method)


def orange(self):
    method = get_tertiary_method(self, Color.ORANGE)
    run_s_move(self, Color.ORANGE, method)


def not_orange(self):
    method = get_tertiary_method(self, Color.ORANGE, True)
    run_s_move(self, Color.ORANGE, method)


def orange2(self):
    method = get_tertiary_method(self, Color.ORANGE, True, True)
    run_s_move(self, Color.ORANGE, method)


def x(self):
    run_s_move(self, Color.NONE, 'x')


def x2(self):
    run_s_move(self, Color.NONE, 'x2')


def y(self):
    run_s_move(self, Color.NONE, 'y')


def y2(self):
    run_s_move(self, Color.NONE, 'y2')


def not_y(self):
    run_s_move(self, Color.NONE, 'not_y')
