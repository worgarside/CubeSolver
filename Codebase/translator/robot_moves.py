import cube.moves as d_move

"""
These are the lowest level moves, and are the only ones the robot is capable of actuating.
They are run on a virtual cube, then appended to it's robot_solve_sequence for running through 
the robot upon completion
"""


def d(cube, verbose, append_flag=True):
    d_move.d(cube, verbose)
    cube.robot_solve_sequence.append('d') if append_flag else 0


def not_d(cube, verbose, append_flag=True):
    d_move.not_d(cube, verbose)
    cube.robot_solve_sequence.append('not_d') if append_flag else 0


def d2(cube, verbose, append_flag=True):
    d(cube, verbose, False)
    d(cube, verbose, False)
    cube.robot_solve_sequence.append('d2') if append_flag else 0


def x(cube, verbose, append_flag=True):
    d_move.x(cube, verbose)
    cube.robot_solve_sequence.append('x') if append_flag else 0


def x2(cube, verbose, append_flag=True):
    x(cube, verbose, False)
    x(cube, verbose, False)
    cube.robot_solve_sequence.append('x2') if append_flag else 0


def y(cube, verbose, append_flag=True):
    d_move.y(cube, verbose)
    cube.robot_solve_sequence.append('y') if append_flag else 0


def not_y(cube, verbose, append_flag=True):
    d_move.not_y(cube, verbose)
    cube.robot_solve_sequence.append('not_y') if append_flag else 0


def y2(cube, verbose, append_flag=True):
    y(cube, verbose, False)
    y(cube, verbose, False)
    cube.robot_solve_sequence.append('y2') if append_flag else 0
