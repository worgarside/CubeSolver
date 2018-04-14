from translator import robot_moves as r_move

"""
These methods all split down the human-readable moves into moves that the robot can perform.
This entire file is an alternative to using a really big, complicated dictionary. This is a move 'active'
 solution than a 'passive' dictionary
"""


def u(cube, verbose):
    r_move.x2(cube, verbose)
    r_move.d(cube, verbose)


def not_u(cube, verbose):
    r_move.x2(cube, verbose)
    r_move.not_d(cube, verbose)


def u2(cube, verbose):
    r_move.x2(cube, verbose)
    r_move.d2(cube, verbose)


def d(cube, verbose):
    r_move.d(cube, verbose)


def not_d(cube, verbose):
    r_move.not_d(cube, verbose)


def d2(cube, verbose):
    r_move.d2(cube, verbose)


def l(cube, verbose):
    r_move.y(cube, verbose)
    r_move.x(cube, verbose)
    r_move.d(cube, verbose)


def not_l(cube, verbose):
    r_move.y(cube, verbose)
    r_move.x(cube, verbose)
    r_move.not_d(cube, verbose)


def l2(cube, verbose):
    r_move.y(cube, verbose)
    r_move.x(cube, verbose)
    r_move.d2(cube, verbose)


def r(cube, verbose):
    r_move.not_y(cube, verbose)
    r_move.x(cube, verbose)
    r_move.d(cube, verbose)


def not_r(cube, verbose):
    r_move.not_y(cube, verbose)
    r_move.x(cube, verbose)
    r_move.not_d(cube, verbose)


def r2(cube, verbose):
    r_move.not_y(cube, verbose)
    r_move.x(cube, verbose)
    r_move.d2(cube, verbose)


def f(cube, verbose):
    r_move.x2(cube, verbose)
    r_move.x(cube, verbose)
    r_move.d(cube, verbose)


def not_f(cube, verbose):
    r_move.x2(cube, verbose)
    r_move.x(cube, verbose)
    r_move.not_d(cube, verbose)


def f2(cube, verbose):
    r_move.x2(cube, verbose)
    r_move.x(cube, verbose)
    r_move.d2(cube, verbose)


def b(cube, verbose):
    r_move.x(cube, verbose)
    r_move.d(cube, verbose)


def not_b(cube, verbose):
    r_move.x(cube, verbose)
    r_move.not_d(cube, verbose)


def b2(cube, verbose):
    r_move.x(cube, verbose)
    r_move.d2(cube, verbose)


def x(cube, verbose):
    r_move.x(cube, verbose)


def not_x(cube, verbose):
    r_move.x2(cube, verbose)
    r_move.x(cube, verbose)


def x2(cube, verbose):
    r_move.x2(cube, verbose)


def y(cube, verbose):
    r_move.y(cube, verbose)


def not_y(cube, verbose):
    r_move.not_y(cube, verbose)


def y2(cube, verbose):
    r_move.y2(cube, verbose)


def z(cube, verbose):
    r_move.not_y(cube, verbose)
    r_move.x(cube, verbose)


def not_z(cube, verbose):
    r_move.y(cube, verbose)
    r_move.x(cube, verbose)


def z2(cube, verbose):
    r_move.y(cube, verbose)
    r_move.x2(cube, verbose)
    r_move.not_y(cube, verbose)
