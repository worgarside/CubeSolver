from move_translator import tertiary_moves as tmove

"""
These methods all split down the human-readable moves into moves that the robot can perform.
This entire file is an alternative to using a really big, complicated dictionary. This is a move 'active'
 solution than a 'passive' dictionary
"""


def u(cube):
    tmove.x2(cube)
    tmove.d(cube)


def not_u(cube):
    tmove.x2(cube)
    tmove.not_d(cube)


def u2(cube):
    tmove.x2(cube)
    tmove.d2(cube)


def d(cube):
    tmove.d(cube)


def not_d(cube):
    tmove.not_d(cube)


def d2(cube):
    tmove.d2(cube)


def l(cube):
    tmove.y(cube)
    tmove.x(cube)
    tmove.d(cube)


def not_l(cube):
    tmove.y(cube)
    tmove.x(cube)
    tmove.not_d(cube)


def l2(cube):
    tmove.y(cube)
    tmove.x(cube)
    tmove.d2(cube)


def r(cube):
    tmove.not_y(cube)
    tmove.x(cube)
    tmove.d(cube)


def not_r(cube):
    tmove.not_y(cube)
    tmove.x(cube)
    tmove.not_d(cube)


def r2(cube):
    tmove.not_y(cube)
    tmove.x(cube)
    tmove.d2(cube)


def f(cube):
    tmove.x2(cube)
    tmove.x(cube)
    tmove.d(cube)


def not_f(cube):
    tmove.x2(cube)
    tmove.x(cube)
    tmove.not_d(cube)


def f2(cube):
    tmove.x2(cube)
    tmove.x(cube)
    tmove.d2(cube)


def b(cube):
    tmove.x(cube)
    tmove.d(cube)


def not_b(cube):
    tmove.x(cube)
    tmove.not_d(cube)


def b2(cube):
    tmove.x(cube)
    tmove.d2(cube)

def x(cube):
    tmove.x(cube)


def not_x(cube):
    tmove.x2(cube)
    tmove.x(cube)

def x2(cube):
    tmove.x2(cube)


def y(cube):
    tmove.y(cube)


def not_y(cube):
    tmove.not_y(cube)


def y2(cube):
    tmove.y2(cube)


def z(cube):
    tmove.not_y(cube)
    tmove.x(cube)


def not_z(cube):
    tmove.y(cube)
    tmove.x(cube)


def z2(cube):
    tmove.y(cube)
    tmove.x2(cube)
    tmove.not_y(cube)
