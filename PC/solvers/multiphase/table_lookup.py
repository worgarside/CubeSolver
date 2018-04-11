import json
from sqlite3 import OperationalError

from cube.cube_class import Cube, Color, Move, Face

INVERSION_DICT = {
    Move.U: Move.NOT_U, Move.D: Move.NOT_D, Move.L: Move.NOT_L,
    Move.R: Move.NOT_R, Move.F: Move.NOT_F, Move.B: Move.NOT_B,
    Move.NOT_U: Move.U, Move.NOT_D: Move.D, Move.NOT_L: Move.L,
    Move.NOT_R: Move.R, Move.NOT_F: Move.F, Move.NOT_B: Move.B,
    Move.U2: Move.U2, Move.D2: Move.D2, Move.L2: Move.L2,
    Move.R2: Move.R2, Move.F2: Move.F2, Move.B2: Move.B2,
}


def lookup_position(db, position, phase):
    lookup_pos = _color_to_monochrome(position, phase)
    try:
        orig_sequence = json.loads(db.query("SELECT move_sequence FROM gs2p%i where position = '%s'"
                                            % (phase, lookup_pos)).fetchone()[0])

        reverse_sequence = orig_sequence[::-1]

        inverted_sequence = []
        for move in reverse_sequence:
            inverted_sequence.append(INVERSION_DICT[Move(move)])

        return inverted_sequence
    except OperationalError as err:
        print(err)
        exit()
    except TypeError:
        print('Cube not found in table gs2p%i \n\n %s' % (phase, Cube(lookup_pos)))
        exit()


def _color_to_monochrome(position, phase):
    color_dict = {
        Face.UP: Cube(position).get_color_of_face(face=Face.UP),
        Face.DOWN: Cube(position).get_color_of_face(face=Face.DOWN),
        Face.FRONT: Cube(position).get_color_of_face(face=Face.FRONT),
        Face.BACK: Cube(position).get_color_of_face(face=Face.BACK),
    }

    adjacent = {1: 19, 3: 10, 5: 16, 7: 13, 10: 3, 13: 7, 16: 5, 19: 1, 21: 32, 23: 24, 24: 23, 26: 27, 27: 26,
                29: 30, 30: 29, 32: 21, 34: 48, 37: 46, 40: 50, 43: 52, 46: 37, 48: 34, 50: 40, 52: 43, }

    monochrome_pos = ''

    if phase == 0:
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
        for index, facelet in enumerate(position):
            if Color(facelet) in {color_dict[Face.UP], color_dict[Face.DOWN]}:
                monochrome_pos += Color.DARK.value
            else:
                monochrome_pos += Color.NONE.value
        return monochrome_pos

    elif phase == 2:
        for index, facelet in enumerate(position):
            if Color(facelet) == color_dict[Face.UP]:
                monochrome_pos += Color.DARK.value
            elif Color(facelet) == color_dict[Face.DOWN]:
                monochrome_pos += Color.NONE.value
            else:
                monochrome_pos += Color.WHITE.value
        return monochrome_pos

    elif phase == 3:
        return Cube(position).position_reduced
    elif phase == 4:
        return position
    else:
        print('Invalid phase: %s' % str(phase))
        exit()
