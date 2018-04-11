from move_translator import tertiary_moves as t_move

"""
These methods all split down the human-readable moves into moves that the robot can perform.
This entire file is an alternative to using a really big, complicated dictionary. This is a move 'active'
 solution than a 'passive' dictionary
"""


def u(cube):
    t_move.x2(cube)
    t_move.d(cube)


def not_u(cube):
    t_move.x2(cube)
    t_move.not_d(cube)


def u2(cube):
    t_move.x2(cube)
    t_move.d2(cube)


def d(cube):
    t_move.d(cube)


def not_d(cube):
    t_move.not_d(cube)


def d2(cube):
    t_move.d2(cube)


def l(cube):
    t_move.y(cube)
    t_move.x(cube)
    t_move.d(cube)


def not_l(cube):
    t_move.y(cube)
    t_move.x(cube)
    t_move.not_d(cube)


def l2(cube):
    t_move.y(cube)
    t_move.x(cube)
    t_move.d2(cube)


def r(cube):
    t_move.not_y(cube)
    t_move.x(cube)
    t_move.d(cube)


def not_r(cube):
    t_move.not_y(cube)
    t_move.x(cube)
    t_move.not_d(cube)


def r2(cube):
    t_move.not_y(cube)
    t_move.x(cube)
    t_move.d2(cube)


def f(cube):
    t_move.x2(cube)
    t_move.x(cube)
    t_move.d(cube)


def not_f(cube):
    t_move.x2(cube)
    t_move.x(cube)
    t_move.not_d(cube)


def f2(cube):
    t_move.x2(cube)
    t_move.x(cube)
    t_move.d2(cube)


def b(cube):
    t_move.x(cube)
    t_move.d(cube)


def not_b(cube):
    t_move.x(cube)
    t_move.not_d(cube)


def b2(cube):
    t_move.x(cube)
    t_move.d2(cube)


def x(cube):
    t_move.x(cube)


def not_x(cube):
    t_move.x2(cube)
    t_move.x(cube)


def x2(cube):
    t_move.x2(cube)


def y(cube):
    t_move.y(cube)


def not_y(cube):
    t_move.not_y(cube)


def y2(cube):
    t_move.y2(cube)


def z(cube):
    t_move.not_y(cube)
    t_move.x(cube)


def not_z(cube):
    t_move.y(cube)
    t_move.x(cube)


def z2(cube):
    t_move.y(cube)
    t_move.x2(cube)
    t_move.not_y(cube)
