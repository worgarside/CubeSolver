from copy import deepcopy

import translator.color_moves as col_moves
from cube.cube_class import Move, Face


def convert_sequence(cube, sequence, verbose):
    """
    The root function for translating the sequence to be robot compatible
    :param cube: The temporary Cube
    :param sequence: The original solve sequence
    :param verbose: Boolean to change verbosity of translation
    :return:
    """
    color_sequence = convert_digital_to_colors(cube, sequence)
    robot_sequence = create_robot_solve_sequence(cube, color_sequence, verbose)
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
