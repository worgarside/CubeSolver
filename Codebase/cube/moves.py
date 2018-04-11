from copy import deepcopy

from cube.cube_class import Rotation, Face, Move

"""
All of the methods below have the same structure and are used to perform a Move on a Cube object

:param cube: the Cube being moved
:param print_flag: a flag to say if the move should be printed to the terminal, used mainly in testing to allow tracing
"""


def u(cube, print_flag=False):
    c = deepcopy(cube)
    cube.set_left(c.front[:3] + c.left[3:])
    cube.set_right(c.back[:3] + c.right[3:])
    cube.set_front(c.right[:3] + c.front[3:])
    cube.set_back(c.left[:3] + c.back[3:])
    cube.rotate_face(Rotation.CLOCKWISE, Face.UP)
    print('u') if print_flag else 0


def not_u(cube, print_flag=False):
    c = deepcopy(cube)
    cube.set_left(c.back[:3] + c.left[3:])
    cube.set_right(c.front[:3] + c.right[3:])
    cube.set_front(c.left[:3] + c.front[3:])
    cube.set_back(c.right[:3] + c.back[3:])
    cube.rotate_face(Rotation.COUNTER_CLOCKWISE, Face.UP)
    print('u\'') if print_flag else 0


def u2(cube, print_flag=False):
    u(cube)
    u(cube)
    print('u2') if print_flag else 0


def d(cube, print_flag=False):
    c = deepcopy(cube)
    cube.set_left(c.left[:6] + c.back[6:])
    cube.set_right(c.right[:6] + c.front[6:])
    cube.set_front(c.front[:6] + c.left[6:])
    cube.set_back(c.back[:6] + c.right[6:])
    cube.rotate_face(Rotation.CLOCKWISE, Face.DOWN)
    print('d') if print_flag else 0


def not_d(cube, print_flag=False):
    c = deepcopy(cube)
    cube.set_left(c.left[:6] + c.front[6:])
    cube.set_right(c.right[:6] + c.back[6:])
    cube.set_front(c.front[:6] + c.right[6:])
    cube.set_back(c.back[:6] + c.left[6:])
    cube.rotate_face(Rotation.COUNTER_CLOCKWISE, Face.DOWN)
    print('d\'') if print_flag else 0


def d2(cube, print_flag=False):
    d(cube)
    d(cube)
    print('d2') if print_flag else 0


def l(cube, print_flag=False):
    c = deepcopy(cube)
    cube.set_up(c.back[8:9] + c.up[1:3] + c.back[5:6] + c.up[4:6] + c.back[2:3] + c.up[7:])
    cube.set_down(c.front[0:1] + c.down[1:3] + c.front[3:4] + c.down[4:6] + c.front[6:7] + c.down[7:])
    cube.set_front(c.up[0:1] + c.front[1:3] + c.up[3:4] + c.front[4:6] + c.up[6:7] + c.front[7:])
    cube.set_back(c.back[0:2] + c.down[6:7] + c.back[3:5] + c.down[3:4] + c.back[6:8] + c.down[0:1])
    cube.rotate_face(Rotation.CLOCKWISE, Face.LEFT)
    print('l') if print_flag else 0


def not_l(cube, print_flag=False):
    c = deepcopy(cube)
    cube.set_up(c.front[0:1] + c.up[1:3] + c.front[3:4] + c.up[4:6] + c.front[6:7] + c.up[7:])
    cube.set_down(c.back[8:9] + c.down[1:3] + c.back[5:6] + c.down[4:6] + c.back[2:3] + c.down[7:])
    cube.set_front(c.down[0:1] + c.front[1:3] + c.down[3:4] + c.front[4:6] + c.down[6:7] + c.front[7:])
    cube.set_back(c.back[0:2] + c.up[6:7] + c.back[3:5] + c.up[3:4] + c.back[6:8] + c.up[0:1])
    cube.rotate_face(Rotation.COUNTER_CLOCKWISE, Face.LEFT)
    print('l\'') if print_flag else 0


def l2(cube, print_flag=False):
    l(cube)
    l(cube)
    print('l2') if print_flag else 0


def r(cube, print_flag=False):
    c = deepcopy(cube)
    cube.set_up(c.up[:2] + c.front[2:3] + c.up[3:5] + c.front[5:6] + c.up[6:8] + c.front[8:9])
    cube.set_down(c.down[:2] + c.back[6:7] + c.down[3:5] + c.back[3:4] + c.down[6:8] + c.back[0:1])
    cube.set_front(c.front[:2] + c.down[2:3] + c.front[3:5] + c.down[5:6] + c.front[6:8] + c.down[8:9])
    cube.set_back(c.up[8:9] + c.back[1:3] + c.up[5:6] + c.back[4:6] + c.up[2:3] + c.back[7:])
    cube.rotate_face(Rotation.CLOCKWISE, Face.RIGHT)
    print('r') if print_flag else 0


def not_r(cube, print_flag=False):
    c = deepcopy(cube)
    cube.set_up(c.up[:2] + c.back[6:7] + c.up[3:5] + c.back[3:4] + c.up[6:8] + c.back[0:1])
    cube.set_down(c.down[:2] + c.front[2:3] + c.down[3:5] + c.front[5:6] + c.down[6:8] + c.front[8:9])
    cube.set_front(c.front[:2] + c.up[2:3] + c.front[3:5] + c.up[5:6] + c.front[6:8] + c.up[8:9])
    cube.set_back(c.down[8:9] + c.back[1:3] + c.down[5:6] + c.back[4:6] + c.down[2:3] + c.back[7:])
    cube.rotate_face(Rotation.COUNTER_CLOCKWISE, Face.RIGHT)
    print('r\'') if print_flag else 0


def r2(cube, print_flag=False):
    r(cube)
    r(cube)
    print('r2') if print_flag else 0


def f(cube, print_flag=False):
    c = deepcopy(cube)
    cube.set_up(c.up[:6] + c.left[8:9] + c.left[5:6] + c.left[2:3])
    cube.set_down(c.right[6:7] + c.right[3:4] + c.right[0:1] + c.down[3:])
    cube.set_left(c.left[:2] + c.down[0:1] + c.left[3:5] + c.down[1:2] + c.left[6:8] + c.down[2:3])
    cube.set_right(c.up[6:7] + c.right[1:3] + c.up[7:8] + c.right[4:6] + c.up[8:9] + c.right[7:])
    cube.rotate_face(Rotation.CLOCKWISE, Face.FRONT)
    print('f') if print_flag else 0


def not_f(cube, print_flag=False):
    c = deepcopy(cube)
    cube.set_up(c.up[:6] + c.right[0:1] + c.right[3:4] + c.right[6:7])
    cube.set_down(c.left[2:3] + c.left[5:6] + c.left[8:9] + c.down[3:])
    cube.set_left(c.left[:2] + c.up[8:9] + c.left[3:5] + c.up[7:8] + c.left[6:8] + c.up[6:7])
    cube.set_right(c.down[2:3] + c.right[1:3] + c.down[1:2] + c.right[4:6] + c.down[0:1] + c.right[7:])
    cube.rotate_face(Rotation.COUNTER_CLOCKWISE, Face.FRONT)
    print('f\'') if print_flag else 0


def f2(cube, print_flag=False):
    f(cube)
    f(cube)
    print('f2') if print_flag else 0


def b(cube, print_flag=False):
    c = deepcopy(cube)
    cube.set_up(c.right[2:3] + c.right[5:6] + c.right[8:9] + c.up[3:])
    cube.set_down(c.down[:6] + c.left[0:1] + c.left[3:4] + c.left[6:7])
    cube.set_left(c.up[2:3] + c.left[1:3] + c.up[1:2] + c.left[4:6] + c.up[0:1] + c.left[7:])
    cube.set_right(c.right[:2] + c.down[8:9] + c.right[3:5] + c.down[7:8] + c.right[6:8] + c.down[6:7])
    cube.rotate_face(Rotation.CLOCKWISE, Face.BACK)
    print('b') if print_flag else 0


def not_b(cube, print_flag=False):
    c = deepcopy(cube)
    cube.set_up(c.left[6:7] + c.left[3:4] + c.left[0:1] + c.up[3:])
    cube.set_down(c.down[:6] + c.right[8:9] + c.right[5:6] + c.right[2:3])
    cube.set_left(c.down[6:7] + c.left[1:3] + c.down[7:8] + c.left[4:6] + c.down[8:9] + c.left[7:])
    cube.set_right(c.right[:2] + c.up[0:1] + c.right[3:5] + c.up[1:2] + c.right[6:8] + c.up[2:3])
    cube.rotate_face(Rotation.COUNTER_CLOCKWISE, Face.BACK)
    print('b\'') if print_flag else 0


def b2(cube, print_flag=False):
    b(cube)
    b(cube)
    print('b2') if print_flag else 0


def m(cube, print_flag=False):
    r(cube)
    not_l(cube)
    not_x(cube)
    print('m') if print_flag else 0


def not_m(cube, print_flag=False):
    not_r(cube)
    l(cube)
    x(cube)
    print('m\'') if print_flag else 0


def m2(cube, print_flag=False):
    m(cube)
    m(cube)
    print('m2') if print_flag else 0


def e(cube, print_flag=False):
    u(cube)
    not_d(cube)
    not_y(cube)
    print('e') if print_flag else 0


def not_e(cube, print_flag=False):
    not_u(cube)
    d(cube)
    y(cube)
    print('e\'') if print_flag else 0


def e2(cube, print_flag=False):
    e(cube)
    e(cube)
    print('e2') if print_flag else 0


def s(cube, print_flag=False):
    not_f(cube)
    b(cube)
    z(cube)
    print('s') if print_flag else 0


def not_s(cube, print_flag=False):
    f(cube)
    not_b(cube)
    not_z(cube)
    print('s\'') if print_flag else 0


def s2(cube, print_flag=False):
    s(cube)
    s(cube)
    print('s2') if print_flag else 0


def x(cube, print_flag=False):
    c = deepcopy(cube)
    cube.set_up(c.front)
    cube.set_down(c.back[::-1])  # [::-1] reverses the string
    cube.set_front(c.down)
    cube.set_back(c.up[::-1])  # [::-1] reverses the string
    cube.rotate_face(Rotation.COUNTER_CLOCKWISE, Face.LEFT)
    cube.rotate_face(Rotation.CLOCKWISE, Face.RIGHT)
    print('x') if print_flag else 0


def not_x(cube, print_flag=False):
    c = deepcopy(cube)
    cube.set_up(c.back[::-1])  # [::-1] reverses the string
    cube.set_down(c.front)
    cube.set_front(c.up)
    cube.set_back(c.down[::-1])  # [::-1] reverses the string
    cube.rotate_face(Rotation.CLOCKWISE, Face.LEFT)
    cube.rotate_face(Rotation.COUNTER_CLOCKWISE, Face.RIGHT)
    print('x\'') if print_flag else 0


def x2(cube, print_flag=False):
    x(cube)
    x(cube)
    print('x2') if print_flag else 0


def y(cube, print_flag=False):
    c = deepcopy(cube)
    cube.set_left(c.front)
    cube.set_right(c.back)
    cube.set_front(c.right)
    cube.set_back(c.left)
    cube.rotate_face(Rotation.CLOCKWISE, Face.UP)
    cube.rotate_face(Rotation.COUNTER_CLOCKWISE, Face.DOWN)
    print('y') if print_flag else 0


def not_y(cube, print_flag=False):
    c = deepcopy(cube)
    cube.set_left(c.back)
    cube.set_right(c.front)
    cube.set_front(c.left)
    cube.set_back(c.right)
    cube.rotate_face(Rotation.COUNTER_CLOCKWISE, Face.UP)
    cube.rotate_face(Rotation.CLOCKWISE, Face.DOWN)
    print('y\'') if print_flag else 0


def y2(cube, print_flag=False):
    y(cube)
    y(cube)
    print('y2') if print_flag else 0


def z(cube, print_flag=False):
    c = deepcopy(cube)
    cube.set_up(c.left[6:7] + c.left[3:4] + c.left[0:1] + c.left[7:8] + c.left[4:5]
                + c.left[1:2] + c.left[8:9] + c.left[5:6] + c.left[2:3])
    cube.set_down(c.right[6:7] + c.right[3:4] + c.right[0:1] + c.right[7:8] + c.right[4:5]
                  + c.right[1:2] + c.right[8:9] + c.right[5:6] + c.right[2:3])
    cube.set_left(c.down[6:7] + c.down[3:4] + c.down[0:1] + c.down[7:8] + c.down[4:5]
                  + c.down[1:2] + c.down[8:9] + c.down[5:6] + c.down[2:3])
    cube.set_right(c.up[6:7] + c.up[3:4] + c.up[0:1] + c.up[7:8] +
                   c.up[4:5] + c.up[1:2] + c.up[8:9] + c.up[5:6] + c.up[2:3])
    cube.rotate_face(Rotation.CLOCKWISE, Face.FRONT)
    cube.rotate_face(Rotation.COUNTER_CLOCKWISE, Face.BACK)
    print('z') if print_flag else 0


def not_z(cube, print_flag=False):
    c = deepcopy(cube)
    cube.set_up(c.right[2:3] + c.right[5:6] + c.right[8:9] + c.right[1:2]
                + c.right[4:5] + c.right[7:8] + c.right[0:1] + c.right[3:4] + c.right[6:7])
    cube.set_down(c.left[2:3] + c.left[5:6] + c.left[8:9] + c.left[1:2]
                  + c.left[4:5] + c.left[7:8] + c.left[0:1] + c.left[3:4] + c.left[6:7])
    cube.set_left(c.up[2:3] + c.up[5:6] + c.up[8:9] + c.up[1:2] + c.up[4:5] +
                  c.up[7:8] + c.up[0:1] + c.up[3:4] + c.up[6:7])
    cube.set_right(c.down[2:3] + c.down[5:6] + c.down[8:9] + c.down[1:2]
                   + c.down[4:5] + c.down[7:8] + c.down[0:1] + c.down[3:4] + c.down[6:7])
    cube.rotate_face(Rotation.COUNTER_CLOCKWISE, Face.FRONT)
    cube.rotate_face(Rotation.CLOCKWISE, Face.BACK)
    print('z\'') if print_flag else 0


def z2(cube, print_flag=False):
    z(cube)
    z(cube)
    print('z2') if print_flag else 0


def dyn_move(cube, move):
    """
    Allows any move to be performed without having to call that specific method, e.g. when iterating through a sequence
    :param cube: the Cube being moved
    :param move: a Move object, which will be evaluated and then used to find the desired method from above
    """
    move_dict = {
        Move.U: u,
        Move.NOT_U: not_u,
        Move.U2: u2,
        Move.D: d,
        Move.NOT_D: not_d,
        Move.D2: d2,
        Move.L: l,
        Move.NOT_L: not_l,
        Move.L2: l2,
        Move.R: r,
        Move.NOT_R: not_r,
        Move.R2: r2,
        Move.F: f,
        Move.NOT_F: not_f,
        Move.F2: f2,
        Move.B: b,
        Move.NOT_B: not_b,
        Move.B2: b2,
        Move.X: x,
        Move.NOT_X: not_x,
        Move.X2: x2,
        Move.Y: y,
        Move.NOT_Y: not_y,
        Move.Y2: y2,
        Move.Z: z,
        Move.NOT_Z: not_z,
        Move.Z2: z2
    }

    move_dict[move](cube)
