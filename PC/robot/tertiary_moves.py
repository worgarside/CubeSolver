from robot import digital_moves as d_move

"""
These are the lowest level moves, and are the only ones the robot is capable of actuating.
They are run on a virtual cube, then appended to it's robot_solve_sequence for running through 
the robot upon completion
"""


def d(self, append_flag=True):
    d_move.d(self)
    self.robot_solve_sequence.append('d') if append_flag else 0


def not_d(self, append_flag=True):
    d_move.not_d(self)
    self.robot_solve_sequence.append('not_d') if append_flag else 0


def d2(self, append_flag=True):
    d(self, False)
    d(self, False)
    self.robot_solve_sequence.append('d2') if append_flag else 0


def x(self, append_flag=True):
    d_move.x(self)
    self.robot_solve_sequence.append('x') if append_flag else 0


def x2(self, append_flag=True):
    x(self, False)
    x(self, False)
    self.robot_solve_sequence.append('x2') if append_flag else 0


def y(self, append_flag=True):
    d_move.y(self)
    self.robot_solve_sequence.append('y') if append_flag else 0


def not_y(self, append_flag=True):
    d_move.not_y(self)
    self.robot_solve_sequence.append('not_y') if append_flag else 0


def y2(self, append_flag=True):
    y(self, False)
    y(self, False)
    self.robot_solve_sequence.append('y2') if append_flag else 0
