import json
from sqlite3 import OperationalError

import kociemba

from cube.cube_class import Cube, Color, Move, Face


def lookup_position(db, position, phase):
    """
    Looks for position in table to find solve sequence
    :param db: Database Cursor object
    :param position: the position being searched for
    :param phase: current phase number, determines table being searched
    :return: solve sequence
    """
    lookup_pos = _color_to_monochrome(position, phase)
    try:
        orig_sequence = json.loads(db.query("SELECT move_sequence FROM multiphase_%i where position = '%s'"
                                            % (phase, lookup_pos)).fetchone()[0])

        reverse_sequence = orig_sequence[::-1]

        inverted_sequence = []
        for move in reverse_sequence:
            inverted_sequence.append(Cube.INVERSION_DICT[Move(move)])

        return inverted_sequence
    except OperationalError as err:
        print(err)
        exit()
    except TypeError:
        print("Position '%s' not found in table multiphase_%i" % (lookup_pos, phase))
        return LookupError, lookup_pos


def _color_to_monochrome(position, phase):
    """
    Each phase relies on solving a reduced-color version of a Cube, usually with only two colors (NONE and DARK mostly).
    This function reduces the position that was passed in to the colours being used
    :param position: full color position to be reduced
    :param phase: the current phase, determines how the position is reduced
    :return: the reduced 'monochrome' position
    """

    # Dictionary containing current colors on the relevant faces
    color_dict = {
        Face.UP: Cube(position).get_color_of_face(face=Face.UP),
        Face.DOWN: Cube(position).get_color_of_face(face=Face.DOWN),
        Face.FRONT: Cube(position).get_color_of_face(face=Face.FRONT),
        Face.BACK: Cube(position).get_color_of_face(face=Face.BACK),
    }

    monochrome_pos = ''

    if phase == 0:
        # Facelets are colored according to if they're 'good'/'bad' - described more in the main dissertation document
        adjacent = {1: 19, 3: 10, 5: 16, 7: 13, 10: 3, 13: 7, 16: 5, 19: 1, 21: 32, 23: 24, 24: 23, 26: 27, 27: 26,
                    29: 30, 30: 29, 32: 21, 34: 48, 37: 46, 40: 50, 43: 52, 46: 37, 48: 34, 50: 40, 52: 43}
        for index, facelet in enumerate(position):
            if index in adjacent:
                if Color(facelet) in {color_dict[Face.UP], color_dict[Face.DOWN]}:
                    monochrome_pos += Color.DARK.value
                elif Color(facelet) in {color_dict[Face.FRONT], color_dict[Face.BACK]} \
                        and Color(position[adjacent[index]]) not in {color_dict[Face.UP], color_dict[Face.DOWN]}:
                    monochrome_pos += Color.DARK.value
                else:
                    monochrome_pos += Color.NONE.value
            else:
                monochrome_pos += Color.NONE.value
        return monochrome_pos

    elif phase == 1:
        # Colors facelets dark if they are UP/DOWN colored, colored none otherwise
        for index, facelet in enumerate(position):
            if Color(facelet) in {color_dict[Face.UP], color_dict[Face.DOWN]}:
                monochrome_pos += Color.DARK.value
            else:
                monochrome_pos += Color.NONE.value
        return monochrome_pos

    elif phase == 2:
        # Phase 2 is actually tricolor - same as previous phase, but UP and DOWN are now different colors
        for index, facelet in enumerate(position):
            if Color(facelet) == color_dict[Face.UP]:
                monochrome_pos += Color.DARK.value
            elif Color(facelet) == color_dict[Face.DOWN]:
                monochrome_pos += Color.NONE.value
            else:
                monochrome_pos += Color.WHITE.value
        return monochrome_pos

    elif phase == 3:
        # Simple half color reduction
        return Cube(position).position_reduced
    elif phase == 4:
        # No reduction for phase 4
        return position
    else:
        print('Invalid phase: %s' % str(phase))
        exit()


def kociemba_fallback(position):
    """
    Fallback to kociemba if the position is not in the table
    The kociemba package uses a different was of representing a Cube so the position must be converted
    :param position: original position
    :return: kociemba solved sequence
    """

    temp_cube = Cube(position)
    temp_position = temp_cube.up + temp_cube.right + temp_cube.front + temp_cube.down + temp_cube.left + temp_cube.back

    """
    This assumes that WHITE = UP, ORANGE = LEFT, etc. etc. - while this may be wrong (it shouldn't be, because of the 
    orientation method), it will still allow the cube to be solved, just the virtual colors won't match the real ones
    """
    kociemba_dict = {'W': 'U', 'O': 'L', 'G': 'F', 'R': 'R', 'B': 'B', 'Y': 'D', }
    kociemba_position = ''
    for facelet in temp_position:
        kociemba_position += kociemba_dict[facelet]
    print('.', end='')
    try:
        """
        Try to solve the Cube with the kociemba package, then turn the solution into the same format as the ones 
        produced elsewhere
        """
        kociemba_solution = kociemba.solve(kociemba_position)
        print('!\n')
        kociemba_moves = kociemba_solution.split()
        solve_sequence = []
        for index, move in enumerate(kociemba_moves):
            if move[-1] == "'":
                kociemba_moves[index] = 'NOT_' + move[0]
            solve_sequence.append(Move[kociemba_moves[index]])
        return solve_sequence
    except ValueError:
        # If the Cube is invalid, kociemba cannot solve it either
        print(".\nInvalid Cube, cannot be solved.\nYour position:       %s\nKociemba's position: %s\nBye :(" % (
            position, kociemba_position))
        exit()

    exit()
