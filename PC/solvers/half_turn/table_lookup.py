import json
from sqlite3 import OperationalError

from cube.cube_class import Cube, Move

INVERSION_DICT = {
    Move.U: Move.NOT_U, Move.D: Move.NOT_D, Move.L: Move.NOT_L,
    Move.R: Move.NOT_R, Move.F: Move.NOT_F, Move.B: Move.NOT_B,
    Move.NOT_U: Move.U, Move.NOT_D: Move.D, Move.NOT_L: Move.L,
    Move.NOT_R: Move.R, Move.NOT_F: Move.F, Move.NOT_B: Move.B,
    Move.U2: Move.U2, Move.D2: Move.D2, Move.L2: Move.L2,
    Move.R2: Move.R2, Move.F2: Move.F2, Move.B2: Move.B2,
}


def lookup_position(db, position):
    lookup_pos = position
    try:
        orig_sequence = json.loads(
            db.query("SELECT move_sequence FROM half_turn where position = '%s'" % lookup_pos).fetchone()[0])

        reverse_sequence = orig_sequence[::-1]

        inverted_sequence = []
        for move in reverse_sequence:
            inverted_sequence.append(INVERSION_DICT[Move(move)])

        return inverted_sequence
    except OperationalError as err:
        print(err)
        exit()
    except TypeError:
        print('Cube not found in table gs3p0 \n\n %s' % Cube(lookup_pos))
        exit()
