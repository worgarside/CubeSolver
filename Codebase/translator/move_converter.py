from copy import deepcopy

import translator.color_moves as col_moves
from cube.cube_class import Move, Face


def convert_sequence(cube, sequence, verbose):
    """
    The root function for translating the sequence to be robot compatible
    :param cube: The temporary Cube
    :param sequence: The original solve sequence
    :param verbose: Boolean to change verbosity of translation
    :return: The robot compatible sequence
    """
    color_sequence = convert_digital_to_colors(cube, sequence)
    robot_sequence = create_robot_solve_sequence(cube, color_sequence, verbose)
    optimise_sequence(robot_sequence)
    return robot_sequence


def convert_digital_to_colors(cube, sequence):
    """
    Converts each of the FACE based moves into COLOR based moves
    This means that even though the robot rotates the cube in order to perform
    certain moves, the frame of reference remains unchanged
    :param cube: The scanned Cube
    :param sequence: The solve sequence which needs to be translated
    :return: a sequence of colors - allowing for the moves to be performed correctly regardless of orientation
    """

    face_color = {
        Face.UP: cube.get_color_of_face(face=Face.UP).name,
        Face.DOWN: cube.get_color_of_face(face=Face.DOWN).name,
        Face.LEFT: cube.get_color_of_face(face=Face.LEFT).name,
        Face.RIGHT: cube.get_color_of_face(face=Face.RIGHT).name,
        Face.FRONT: cube.get_color_of_face(face=Face.FRONT).name,
        Face.BACK: cube.get_color_of_face(face=Face.BACK).name
    }

    move_to_color_dict = {
        Move.U: [face_color[Face.UP]],
        Move.NOT_U: ['NOT_' + face_color[Face.UP]],
        Move.U2: [face_color[Face.UP] + '2'],
        Move.D: [face_color[Face.DOWN]],
        Move.NOT_D: ['NOT_' + face_color[Face.DOWN]],
        Move.D2: [face_color[Face.DOWN] + '2'],
        Move.L: [face_color[Face.LEFT]],
        Move.NOT_L: ['NOT_' + face_color[Face.LEFT]],
        Move.L2: [face_color[Face.LEFT] + '2'],
        Move.R: [face_color[Face.RIGHT]],
        Move.NOT_R: ['NOT_' + face_color[Face.RIGHT]],
        Move.R2: [face_color[Face.RIGHT] + '2'],
        Move.F: [face_color[Face.FRONT]],
        Move.NOT_F: ['NOT_' + face_color[Face.FRONT]],
        Move.F2: [face_color[Face.FRONT] + '2'],
        Move.B: [face_color[Face.BACK]],
        Move.NOT_B: ['NOT_' + face_color[Face.BACK]],
        Move.B2: [face_color[Face.BACK] + '2'],
    }

    color_sequence = []
    for move in sequence:
        color_sequence.extend(move_to_color_dict[move])

    return color_sequence


def create_robot_solve_sequence(cube, color_sequence, verbose):
    """
    Create a robot-compatible solve sequence by translating and performing it concurrently on a Cube
    :param cube: the Cube to be solved
    :param color_sequence: The sequence of colors previously generated
    :param verbose: Boolean to change verbosity of translation
    :return: The robot-compatible solve sequence
    """
    temp_cube = deepcopy(cube)
    for color in color_sequence:
        # Get the method name, then run it on the temp_cube
        print('\n %s : ' % color, end='') if verbose else 0
        method = getattr(col_moves, color.lower())
        method(temp_cube, verbose)
    print()
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
