from cube_class import Cube
from rotation_class import Rotation
from side_class import Side


def u(self, print_flag=False):
    c = Cube(self._pos)
    self.set_left(c.front[:3] + c.left[3:])
    self.set_right(c.back[:3] + c.right[3:])
    self.set_front(c.right[:3] + c.front[3:])
    self.set_back(c.left[:3] + c.back[3:])
    self.rotate_side(Rotation.CLOCKWISE, Side.UP)
    print('u') if print_flag else 0


def not_u(self, print_flag=False):
    c = Cube(self._pos)
    self.set_left(c.back[:3] + c.left[3:])
    self.set_right(c.front[:3] + c.right[3:])
    self.set_front(c.left[:3] + c.front[3:])
    self.set_back(c.right[:3] + c.back[3:])
    self.rotate_side(Rotation.COUNTER_CLOCKWISE, Side.UP)
    print('u\'') if print_flag else 0


def u2(self, print_flag=False):
    u(self)
    u(self)
    print('u2') if print_flag else 0


def d(self, print_flag=False):
    c = Cube(self._pos)
    self.set_left(c.left[:6] + c.back[6:])
    self.set_right(c.right[:6] + c.front[6:])
    self.set_front(c.front[:6] + c.left[6:])
    self.set_back(c.back[:6] + c.right[6:])
    self.rotate_side(Rotation.CLOCKWISE, Side.DOWN)
    print('d') if print_flag else 0


def not_d(self, print_flag=False):
    c = Cube(self._pos)
    self.set_left(c.left[:6] + c.front[6:])
    self.set_right(c.right[:6] + c.back[6:])
    self.set_front(c.front[:6] + c.right[6:])
    self.set_back(c.back[:6] + c.left[6:])
    self.rotate_side(Rotation.COUNTER_CLOCKWISE, Side.DOWN)
    print('d\'') if print_flag else 0


def d2(self, print_flag=False):
    d(self)
    d(self)
    print('d2') if print_flag else 0


def l(self, print_flag=False):
    c = Cube(self._pos)
    self.set_up(c.back[8:9] + c.up[1:3] + c.back[5:6] + c.up[4:6] + c.back[2:3] + c.up[7:])
    self.set_down(c.front[0:1] + c.down[1:3] + c.front[3:4] + c.down[4:6] + c.front[6:7] + c.down[7:])
    self.set_front(c.up[0:1] + c.front[1:3] + c.up[3:4] + c.front[4:6] + c.up[6:7] + c.front[7:])
    self.set_back(c.back[0:2] + c.down[6:7] + c.back[3:5] + c.down[3:4] + c.back[6:8] + c.down[0:1])
    self.rotate_side(Rotation.CLOCKWISE, Side.LEFT)
    print('l') if print_flag else 0


def not_l(self, print_flag=False):
    c = Cube(self._pos)
    self.set_up(c.front[0:1] + c.up[1:3] + c.front[3:4] + c.up[4:6] + c.front[6:7] + c.up[7:])
    self.set_down(c.back[8:9] + c.down[1:3] + c.back[5:6] + c.down[4:6] + c.back[2:3] + c.down[7:])
    self.set_front(c.down[0:1] + c.front[1:3] + c.down[3:4] + c.front[4:6] + c.down[6:7] + c.front[7:])
    self.set_back(c.back[0:2] + c.up[6:7] + c.back[3:5] + c.up[3:4] + c.back[6:8] + c.up[0:1])
    self.rotate_side(Rotation.COUNTER_CLOCKWISE, Side.LEFT)
    print('l\'') if print_flag else 0


def l2(self, print_flag=False):
    l(self)
    l(self)
    print('l2') if print_flag else 0


def r(self, print_flag=False):
    c = Cube(self._pos)
    self.set_up(c.up[:2] + c.front[2:3] + c.up[3:5] + c.front[5:6] + c.up[6:8] + c.front[8:9])
    self.set_down(c.down[:2] + c.back[6:7] + c.down[3:5] + c.back[3:4] + c.down[6:8] + c.back[0:1])
    self.set_front(c.front[:2] + c.down[2:3] + c.front[3:5] + c.down[5:6] + c.front[6:8] + c.down[8:9])
    self.set_back(c.up[8:9] + c.back[1:3] + c.up[5:6] + c.back[4:6] + c.up[2:3] + c.back[7:])
    self.rotate_side(Rotation.CLOCKWISE, Side.RIGHT)
    print('r') if print_flag else 0


def not_r(self, print_flag=False):
    c = Cube(self._pos)
    self.set_up(c.up[:2] + c.back[6:7] + c.up[3:5] + c.back[3:4] + c.up[6:8] + c.back[0:1])
    self.set_down(c.down[:2] + c.front[2:3] + c.down[3:5] + c.front[5:6] + c.down[6:8] + c.front[8:9])
    self.set_front(c.front[:2] + c.up[2:3] + c.front[3:5] + c.up[5:6] + c.front[6:8] + c.up[8:9])
    self.set_back(c.down[8:9] + c.back[1:3] + c.down[5:6] + c.back[4:6] + c.down[2:3] + c.back[7:])
    self.rotate_side(Rotation.COUNTER_CLOCKWISE, Side.RIGHT)
    print('r\'') if print_flag else 0


def r2(self, print_flag=False):
    r(self)
    r(self)
    print('r2') if print_flag else 0


def f(self, print_flag=False):
    c = Cube(self._pos)
    self.set_up(c.up[:6] + c.left[8:9] + c.left[5:6] + c.left[2:3])
    self.set_down(c.right[6:7] + c.right[3:4] + c.right[0:1] + c.down[3:])
    self.set_left(c.left[:2] + c.down[0:1] + c.left[3:5] + c.down[1:2] + c.left[6:8] + c.down[2:3])
    self.set_right(c.up[6:7] + c.right[1:3] + c.up[7:8] + c.right[4:6] + c.up[8:9] + c.right[7:])
    self.rotate_side(Rotation.CLOCKWISE, Side.FRONT)
    print('f') if print_flag else 0


def not_f(self, print_flag=False):
    c = Cube(self._pos)
    self.set_up(c.up[:6] + c.right[0:1] + c.right[3:4] + c.right[6:7])
    self.set_down(c.left[2:3] + c.left[5:6] + c.left[8:9] + c.down[3:])
    self.set_left(c.left[:2] + c.up[8:9] + c.left[3:5] + c.up[7:8] + c.left[6:8] + c.up[6:7])
    self.set_right(c.down[2:3] + c.right[1:3] + c.down[1:2] + c.right[4:6] + c.down[0:1] + c.right[7:])
    self.rotate_side(Rotation.COUNTER_CLOCKWISE, Side.FRONT)
    print('f\'') if print_flag else 0


def f2(self, print_flag=False):
    f(self)
    f(self)
    print('f2') if print_flag else 0


def b(self, print_flag=False):
    c = Cube(self._pos)
    self.set_up(c.right[2:3] + c.right[5:6] + c.right[8:9] + c.up[3:])
    self.set_down(c.down[:6] + c.left[0:1] + c.left[3:4] + c.left[6:7])
    self.set_left(c.up[2:3] + c.left[1:3] + c.up[1:2] + c.left[4:6] + c.up[0:1] + c.left[7:])
    self.set_right(c.right[:2] + c.down[8:9] + c.right[3:5] + c.down[7:8] + c.right[6:8] + c.down[6:7])
    self.rotate_side(Rotation.CLOCKWISE, Side.BACK)
    print('b') if print_flag else 0


def not_b(self, print_flag=False):
    c = Cube(self._pos)
    self.set_up(c.left[6:7] + c.left[3:4] + c.left[0:1] + c.up[3:])
    self.set_down(c.down[:6] + c.right[8:9] + c.right[5:6] + c.right[2:3])
    self.set_left(c.down[6:7] + c.left[1:3] + c.down[7:8] + c.left[4:6] + c.down[8:9] + c.left[7:])
    self.set_right(c.right[:2] + c.up[0:1] + c.right[3:5] + c.up[1:2] + c.right[6:8] + c.up[2:3])
    self.rotate_side(Rotation.COUNTER_CLOCKWISE, Side.BACK)
    print('b\'') if print_flag else 0


def b2(self, print_flag=False):
    b(self)
    b(self)
    print('b2') if print_flag else 0


def m(self, print_flag=False):
    r(self)
    not_l(self)
    not_x(self)
    print('m') if print_flag else 0


def not_m(self, print_flag=False):
    not_r(self)
    l(self)
    x(self)
    print('m\'') if print_flag else 0


def m2(self, print_flag=False):
    m(self)
    m(self)
    print('m2') if print_flag else 0


def e(self, print_flag=False):
    u(self)
    not_d(self)
    not_y(self)
    print('e') if print_flag else 0


def not_e(self, print_flag=False):
    not_u(self)
    d(self)
    y(self)
    print('e\'') if print_flag else 0


def e2(self, print_flag=False):
    e(self)
    e(self)
    print('e2') if print_flag else 0


def s(self, print_flag=False):
    not_f(self)
    b(self)
    z(self)
    print('s') if print_flag else 0


def not_s(self, print_flag=False):
    f(self)
    not_b(self)
    not_z(self)
    print('s\'') if print_flag else 0


def s2(self, print_flag=False):
    s(self)
    s(self)
    print('s2') if print_flag else 0


def x(self, print_flag=False):
    c = Cube(self._pos)
    self.set_up(c.front)
    self.set_down(c.back[::-1])  # [::-1] reverses the string
    self.set_front(c.down)
    self.set_back(c.up[::-1])  # [::-1] reverses the string
    self.rotate_side(Rotation.COUNTER_CLOCKWISE, Side.LEFT)
    self.rotate_side(Rotation.CLOCKWISE, Side.RIGHT)
    print('x') if print_flag else 0


def not_x(self, print_flag=False):
    c = Cube(self._pos)
    self.set_up(c.back[::-1])  # [::-1] reverses the string
    self.set_down(c.front)
    self.set_front(c.up)
    self.set_back(c.down[::-1])  # [::-1] reverses the string
    self.rotate_side(Rotation.CLOCKWISE, Side.LEFT)
    self.rotate_side(Rotation.COUNTER_CLOCKWISE, Side.RIGHT)
    print('x\'') if print_flag else 0


def x2(self, print_flag=False):
    x(self)
    x(self)
    print('x2') if print_flag else 0


def y(self, print_flag=False):
    c = Cube(self._pos)
    self.set_left(c.front)
    self.set_right(c.back)
    self.set_front(c.right)
    self.set_back(c.left)
    self.rotate_side(Rotation.CLOCKWISE, Side.UP)
    self.rotate_side(Rotation.COUNTER_CLOCKWISE, Side.DOWN)
    print('y') if print_flag else 0


def not_y(self, print_flag=False):
    c = Cube(self._pos)
    self.set_left(c.back)
    self.set_right(c.front)
    self.set_front(c.left)
    self.set_back(c.right)
    self.rotate_side(Rotation.COUNTER_CLOCKWISE, Side.UP)
    self.rotate_side(Rotation.CLOCKWISE, Side.DOWN)
    print('y\'') if print_flag else 0


def y2(self, print_flag=False):
    y(self)
    y(self)
    print('y2') if print_flag else 0


def z(self, print_flag=False):
    c = Cube(self._pos)
    self.set_up(c.left[6:7] + c.left[3:4] + c.left[0:1] + c.left[7:8] + c.left[4:5]
                + c.left[1:2] + c.left[8:9] + c.left[5:6] + c.left[2:3])
    self.set_down(c.right[6:7] + c.right[3:4] + c.right[0:1] + c.right[7:8] + c.right[4:5]
                  + c.right[1:2] + c.right[8:9] + c.right[5:6] + c.right[2:3])
    self.set_left(c.down[6:7] + c.down[3:4] + c.down[0:1] + c.down[7:8] + c.down[4:5]
                  + c.down[1:2] + c.down[8:9] + c.down[5:6] + c.down[2:3])
    self.set_right(c.up[6:7] + c.up[3:4] + c.up[0:1] + c.up[7:8] +
                   c.up[4:5] + c.up[1:2] + c.up[8:9] + c.up[5:6] + c.up[2:3])
    self.rotate_side(Rotation.CLOCKWISE, Side.FRONT)
    self.rotate_side(Rotation.COUNTER_CLOCKWISE, Side.BACK)
    print('z') if print_flag else 0


def not_z(self, print_flag=False):
    c = Cube(self._pos)
    self.set_up(c.right[2:3] + c.right[5:6] + c.right[8:9] + c.right[1:2]
                + c.right[4:5] + c.right[7:8] + c.right[0:1] + c.right[3:4] + c.right[6:7])
    self.set_down(c.left[2:3] + c.left[5:6] + c.left[8:9] + c.left[1:2]
                  + c.left[4:5] + c.left[7:8] + c.left[0:1] + c.left[3:4] + c.left[6:7])
    self.set_left(c.up[2:3] + c.up[5:6] + c.up[8:9] + c.up[1:2] + c.up[4:5] +
                  c.up[7:8] + c.up[0:1] + c.up[3:4] + c.up[6:7])
    self.set_right(c.down[2:3] + c.down[5:6] + c.down[8:9] + c.down[1:2]
                   + c.down[4:5] + c.down[7:8] + c.down[0:1] + c.down[3:4] + c.down[6:7])
    self.rotate_side(Rotation.COUNTER_CLOCKWISE, Side.FRONT)
    self.rotate_side(Rotation.CLOCKWISE, Side.BACK)
    print('z\'') if print_flag else 0


def z2(self, print_flag=False):
    z(self)
    z(self)
    print('z2') if print_flag else 0
