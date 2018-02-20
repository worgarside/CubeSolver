from robot import tertiary_moves as tmove

"""
These methods all split down the human-readable moves into moves that the robot can perform.
This entire file is an alternative to using a really big, complicated dictionary. This is a move 'active'
 solution than a 'passive' dictionary
"""


def u(self):
    tmove.x2(self)
    tmove.d(self)


def not_u(self):
    tmove.x2(self)
    tmove.not_d(self)


def u2(self):
    tmove.x2(self)
    tmove.d2(self)


def d(self):
    tmove.d(self)


def not_d(self):
    tmove.not_d(self)


def d2(self):
    tmove.d2(self)


def l(self):
    tmove.y(self)
    tmove.x(self)
    tmove.d(self)


def not_l(self):
    tmove.y(self)
    tmove.x(self)
    tmove.not_d(self)


def l2(self):
    tmove.y(self)
    tmove.x(self)
    tmove.d2(self)


def r(self):
    tmove.not_y(self)
    tmove.x(self)
    tmove.d(self)


def not_r(self):
    tmove.not_y(self)
    tmove.x(self)
    tmove.not_d(self)


def r2(self):
    tmove.not_y(self)
    tmove.x(self)
    tmove.d2(self)


def f(self):
    tmove.x2(self)
    tmove.x(self)
    tmove.d(self)


def not_f(self):
    tmove.x2(self)
    tmove.x(self)
    tmove.not_d(self)


def f2(self):
    tmove.x2(self)
    tmove.x(self)
    tmove.d2(self)


def b(self):
    tmove.x(self)
    tmove.d(self)


def not_b(self):
    tmove.x(self)
    tmove.not_d(self)


def b2(self):
    tmove.x(self)
    tmove.d2(self)


def m(self):
    tmove.y(self)
    tmove.x(self)
    tmove.not_d(self)
    tmove.x2(self)
    tmove.d(self)

def not_m(self):
    tmove.y(self)
    tmove.x(self)
    tmove.d(self)
    tmove.x2(self)
    tmove.not_d(self)


def m2(self):
    tmove.y(self)
    tmove.x(self)
    tmove.d2(self)
    tmove.x2(self)
    tmove.d2(self)


def e(self):
    tmove.not_d(self)
    tmove.x2(self)
    tmove.d(self)


def not_e(self):
    tmove.d(self)
    tmove.x2(self)
    tmove.not_d(self)


def e2(self):
    tmove.d2(self)
    tmove.x2(self)
    tmove.d2(self)


def s(self):
    tmove.y2(self)
    tmove.x(self)
    tmove.not_d(self)
    tmove.x2(self)
    tmove.d(self)


def not_s(self):
    tmove.y2(self)
    tmove.x(self)
    tmove.d(self)
    tmove.x2(self)
    tmove.not_d(self)


def s2(self):
    tmove.y2(self)
    tmove.x(self)
    tmove.d2(self)
    tmove.x2(self)
    tmove.d2(self)


def x(self):
    tmove.x(self)


def not_x(self):
    tmove.x2(self)
    tmove.x(self)

def x2(self):
    tmove.x2(self)


def y(self):
    tmove.y(self)


def not_y(self):
    tmove.not_y(self)


def y2(self):
    tmove.y2(self)


def z(self):
    tmove.not_y(self)
    tmove.x(self)


def not_z(self):
    tmove.y(self)
    tmove.x(self)


def z2(self):
    tmove.y(self)
    tmove.x2(self)
    tmove.not_y(self)
