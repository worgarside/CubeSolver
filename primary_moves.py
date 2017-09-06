from color_class import Color
import secondary_moves as smove


def get_tertiary_method(self, color, negative_flag=False, double_flag=False):
    values = self.color_side_dict.values()
    color_pos = list(values).index(color.name)
    keys = self.color_side_dict.keys()
    face_pos = list(keys)[color_pos]
    method = face_pos[0].lower()

    if double_flag:
        method = method + '2'
        return method

    if negative_flag:
        method = 'not_' + method
    return method


def run_smove_method(self, color, method):
    try:
        move_method = getattr(smove, method)
        move_method(self)
    except AttributeError as e:
        print('smove.' + color.name.lower() + ' failed: \'' + method + '\' | ' + str(e))
        exit()


def white(self):
    method = get_tertiary_method(self, Color.WHITE)
    run_smove_method(self, Color.WHITE, method)


def not_white(self):
    method = get_tertiary_method(self, Color.WHITE, True)
    run_smove_method(self, Color.WHITE, method)


def white2(self):
    method = get_tertiary_method(self, Color.WHITE, True, True)
    run_smove_method(self, Color.WHITE, method)


def yellow(self):
    method = get_tertiary_method(self, Color.YELLOW)
    run_smove_method(self, Color.YELLOW, method)


def not_yellow(self):
    method = get_tertiary_method(self, Color.YELLOW, True)
    run_smove_method(self, Color.YELLOW, method)


def yellow2(self):
    method = get_tertiary_method(self, Color.YELLOW, True, True)
    run_smove_method(self, Color.YELLOW, method)


def green(self):
    method = get_tertiary_method(self, Color.GREEN)
    run_smove_method(self, Color.GREEN, method)


def not_green(self):
    method = get_tertiary_method(self, Color.GREEN, True)
    run_smove_method(self, Color.GREEN, method)


def green2(self):
    method = get_tertiary_method(self, Color.GREEN, True, True)
    run_smove_method(self, Color.GREEN, method)


def blue(self):
    method = get_tertiary_method(self, Color.BLUE)
    run_smove_method(self, Color.BLUE, method)


def not_blue(self):
    method = get_tertiary_method(self, Color.BLUE, True)
    run_smove_method(self, Color.BLUE, method)


def blue2(self):
    method = get_tertiary_method(self, Color.BLUE, True, True)
    run_smove_method(self, Color.BLUE, method)


def red(self):
    method = get_tertiary_method(self, Color.RED)
    run_smove_method(self, Color.RED, method)


def not_red(self):
    method = get_tertiary_method(self, Color.RED, True)
    run_smove_method(self, Color.RED, method)


def red2(self):
    method = get_tertiary_method(self, Color.RED, True, True)
    run_smove_method(self, Color.RED, method)


def orange(self):
    method = get_tertiary_method(self, Color.ORANGE)
    run_smove_method(self, Color.ORANGE, method)


def not_orange(self):
    method = get_tertiary_method(self, Color.ORANGE, True)
    run_smove_method(self, Color.ORANGE, method)


def orange2(self):
    method = get_tertiary_method(self, Color.ORANGE, True, True)
    run_smove_method(self, Color.ORANGE, method)


def x(self):
    run_smove_method(self, Color.NONE, 'x')


def x2(self):
    run_smove_method(self, Color.NONE, 'x2')


def y(self):
    run_smove_method(self, Color.NONE, 'y')


def y2(self):
    run_smove_method(self, Color.NONE, 'y2')


def not_y(self):
    run_smove_method(self, Color.NONE, 'not_y')
