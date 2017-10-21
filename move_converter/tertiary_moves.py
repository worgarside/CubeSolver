from move_converter import digital_moves as dmove

"""
These are the lowest level moves, and are the only ones the robot is capable of actuating.
They are run on a virtual cube, then appended to it's robot_solve_sequence for running through 
the robot upon completion
"""


def d(self, append_flag=True):
    dmove.d(self)
    # c = deepcopy(self)
    # self.set_left(c.left[:6] + c.back[6:])
    # self.set_right(c.right[:6] + c.front[6:])
    # self.set_front(c.front[:6] + c.left[6:])
    # self.set_back(c.back[:6] + c.right[6:])
    # self.rotate_side(Rotation.CLOCKWISE, Side.DOWN)
    self.robot_solve_sequence.append('d') if append_flag else 0


def not_d(self, append_flag=True):
    dmove.not_d(self)
    # c = deepcopy(self)
    # self.set_left(c.left[:6] + c.front[6:])
    # self.set_right(c.right[:6] + c.back[6:])
    # self.set_front(c.front[:6] + c.right[6:])
    # self.set_back(c.back[:6] + c.left[6:])
    # self.rotate_side(Rotation.COUNTER_CLOCKWISE, Side.DOWN)
    self.robot_solve_sequence.append('not_d') if append_flag else 0


def d2(self, append_flag=True):
    d(self, False)
    d(self, False)
    self.robot_solve_sequence.append('d2') if append_flag else 0


def x(self, append_flag=True):
    dmove.x(self)
    # c = deepcopy(self)
    # self.set_up(c.front)
    # self.set_down(c.back[::-1])  # [::-1] reverses the string
    # self.set_front(c.down)
    # self.set_back(c.up[::-1])  # [::-1] reverses the string
    # self.rotate_side(Rotation.COUNTER_CLOCKWISE, Side.LEFT)
    # self.rotate_side(Rotation.CLOCKWISE, Side.RIGHT)
    self.robot_solve_sequence.append('x') if append_flag else 0


def x2(self, append_flag=True):
    x(self, False)
    x(self, False)
    self.robot_solve_sequence.append('x2') if append_flag else 0


def y(self, append_flag=True):
    dmove.y(self)
    # c = deepcopy(self)
    # self.set_left(c.front)
    # self.set_right(c.back)
    # self.set_front(c.right)
    # self.set_back(c.left)
    # self.rotate_side(Rotation.CLOCKWISE, Side.UP)
    # self.rotate_side(Rotation.COUNTER_CLOCKWISE, Side.DOWN)
    self.robot_solve_sequence.append('y') if append_flag else 0


def not_y(self, append_flag=True):
    dmove.not_y(self)
    # c = deepcopy(self)
    # self.set_left(c.back)
    # self.set_right(c.front)
    # self.set_front(c.left)
    # self.set_back(c.right)
    # self.rotate_side(Rotation.COUNTER_CLOCKWISE, Side.UP)
    # self.rotate_side(Rotation.CLOCKWISE, Side.DOWN)
    self.robot_solve_sequence.append('not_y') if append_flag else 0


def y2(self, append_flag=True):
    y(self, False)
    y(self, False)
    self.robot_solve_sequence.append('y2') if append_flag else 0
