from copy import deepcopy

import robot.primary_moves as pr_move

from cube.color_class import Color
from cube.move_class import Move


def convert_sequence(cube, sequence):
    # runs solve functions to produce sequence of digital moves to generate_solve_sequences
    color_sequence = convert_digital_to_colors(cube, sequence)
    robot_sequence = create_robot_solve_sequence(cube, color_sequence)
    print(robot_sequence)

    return robot_sequence
    # Changes digital/human moves to account for frame of reference changes with M/E/S robot style moves


"""
Converts each of the SIDE based moves into COLOR based moves
This means that even though the robot rotates the cube in order to perform 
certain moves, the frame of reference remains unchanged
"""


def convert_digital_to_colors(cube, sequence):
    move_to_color_dict = {
        Move.U: [Color(cube.up[4]).name],
        Move.NOT_U: ['NOT_' + Color(cube.up[4]).name],
        Move.U2: [Color(cube.up[4]).name + '2'],
        Move.D: [Color(cube.down[4]).name],
        Move.NOT_D: ['NOT_' + Color(cube.down[4]).name],
        Move.D2: [Color(cube.down[4]).name + '2'],
        Move.L: [Color(cube.left[4]).name],
        Move.NOT_L: ['NOT_' + Color(cube.left[4]).name],
        Move.L2: [Color(cube.left[4]).name + '2'],
        Move.R: [Color(cube.right[4]).name],
        Move.NOT_R: ['NOT_' + Color(cube.right[4]).name],
        Move.R2: [Color(cube.right[4]).name + '2'],
        Move.F: [Color(cube.front[4]).name],
        Move.NOT_F: ['NOT_' + Color(cube.front[4]).name],
        Move.F2: [Color(cube.front[4]).name + '2'],
        Move.B: [Color(cube.back[4]).name],
        Move.NOT_B: ['NOT_' + Color(cube.back[4]).name],
        Move.B2: [Color(cube.back[4]).name + '2'],
    }

    temp_sequence = []
    for move in sequence:
        temp_sequence.extend(move_to_color_dict[move])

    return temp_sequence


# Uses the primary, secondary and tertiary move levels to create a robot-usable move sequence
def create_robot_solve_sequence(cube, color_sequence):
    temp_cube = deepcopy(cube)
    for pm in color_sequence:
        method = getattr(pr_move, pm.lower())
        method(temp_cube)
        robot_solve_sequence = temp_cube.robot_solve_sequence

    return robot_solve_sequence
