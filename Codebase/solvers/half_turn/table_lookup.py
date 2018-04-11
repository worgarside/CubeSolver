import json
from sqlite3 import OperationalError

from cube.cube_class import Cube, Move


def lookup_position(db, position):
    """
    Looks for position in table to find solve sequence
    :param db: Database Cursor object
    :param position: the position being searched for
    :return: solve sequence
    """
    try:
        orig_sequence = json.loads(
            db.query("SELECT move_sequence FROM half_turn where position = '%s'" % position).fetchone()[0])

        reverse_sequence = orig_sequence[::-1]

        # Need to invert the moves to go back from mixed -> solved as the moves are one way
        inverted_sequence = []
        for move in reverse_sequence:
            inverted_sequence.append(Cube.INVERSION_DICT[Move(move)])

        return inverted_sequence
    except OperationalError as err:
        # Usually if table doesn't exist
        print(err)
        exit()
    except TypeError:
        # If the position isn't in the table
        print("Position '%s' not found in table half_turn" % position)
        exit()
