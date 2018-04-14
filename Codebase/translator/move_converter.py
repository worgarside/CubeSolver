from copy import deepcopy

import translator.color_moves as pr_move
from cube.cube_class import Color, Move


def convert_sequence(cube, sequence):
    # runs solve functions to produce sequence of digital moves to generate_solve_sequences
    color_sequence = convert_digital_to_colors(cube, sequence)
    robot_sequence = create_robot_solve_sequence(cube, color_sequence)

    optimise_sequence(robot_sequence)

    return robot_sequence
    # Changes digital/human moves to account for frame of reference changes with M/E/S robot style moves


"""
Converts each of the FACE based moves into COLOR based moves
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
    for color in color_sequence:
        method = getattr(pr_move, color.lower())
        method(temp_cube)

    return temp_cube.robot_solve_sequence


def optimise_sequence(sequence):
    print('\n')
    for index, move in enumerate(sequence):
        print(move, end=' ')
    print()

    for index, move in enumerate(sequence):
        if index < len(sequence) - 1:
            # Single move (d, y)
            if len(move) == 1:
                if move.lower() != 'x':
                    # d d2 -> not_d
                    if sequence[index + 1] == move + '2':
                        sequence[index] = 'not_' + move
                        del sequence[index + 1]

                    # d not_d -> []
                    elif sequence[index + 1].lower() == 'not_' + move.lower():
                        del sequence[index]
                        del sequence[index + 1]

                    # d d -> d2
                    elif sequence[index + 1].lower() == move.lower():
                        sequence[index] = move + '2'
                        del sequence[index + 1]

            # Double move (d2, x2 y2)
            elif len(move) == 2:
                # d2, d -> not_d (not x)
                if len(sequence[index + 1]) == 1 \
                        and sequence[index + 1].lower() == move[0].lower() \
                        and move[0].lower() != 'x':
                    sequence[index] = 'not_' + move[0]
                    del sequence[index + 1]

                # d2, d2 -> []
                elif sequence[index + 1] == move:
                    del sequence[index]
                    del sequence[index + 1]

                # d2, not_d -> d
                elif sequence[index + 1] == 'not_' + move[0]:
                    sequence[index] = move[0]
                    del sequence[index + 1]

            # Not move (not_d, not_y)
            elif len(move) == 5:
                # not_d, d -> []
                if sequence[index + 1] == move[-1]:
                    del sequence[index]
                    del sequence[index + 1]

                # not_d, d2 -> d
                elif sequence[index + 1] == move[-1] + '2':
                    sequence[index] = move[-1]
                    del sequence[index + 1]

                # not_d, not_d -> d2
                elif sequence[index + 1] == move:
                    sequence[index] = move[-1] + '2'
                    del sequence[index + 1]
            else:
                for index2, move2 in enumerate(sequence):
                    print(move2, end=' ')
                print('\nInvalid move length at index %i during post conversion optimisation: %s' % (index, move))
                exit(1)

    for index, move in enumerate(sequence):
        print(move, end=' ')
    print('\n')
