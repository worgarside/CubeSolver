import cube.moves as d_move

"""
These are the lowest level moves, and are the only ones the robot is capable of actuating.
They are run on a virtual cube, then appended to it's robot_solve_sequence for running through 
the robot upon completion
"""


def d(cube, append_flag=True):
    d_move.d(cube)
    cube.robot_solve_sequence.append('d') if append_flag else 0


def not_d(cube, append_flag=True):
    d_move.not_d(cube)
    cube.robot_solve_sequence.append('not_d') if append_flag else 0


def d2(cube, append_flag=True):
    d(cube, False)
    d(cube, False)
    cube.robot_solve_sequence.append('d2') if append_flag else 0


def x(cube, append_flag=True):
    d_move.x(cube)
    cube.robot_solve_sequence.append('x') if append_flag else 0


def x2(cube, append_flag=True):
    x(cube, False)
    x(cube, False)
    cube.robot_solve_sequence.append('x2') if append_flag else 0


def y(cube, append_flag=True):
    d_move.y(cube)
    cube.robot_solve_sequence.append('y') if append_flag else 0


def not_y(cube, append_flag=True):
    d_move.not_y(cube)
    cube.robot_solve_sequence.append('not_y') if append_flag else 0


def y2(cube, append_flag=True):
    y(cube, False)
    y(cube, False)
    cube.robot_solve_sequence.append('y2') if append_flag else 0
