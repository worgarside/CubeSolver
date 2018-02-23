import pickle

from cube.cube_class import SOLVED_POS
from cube.move_class import Move

MOVE_GROUP = [Move.U2, Move.D2, Move.L2, Move.R2, Move.F2, Move.B2]

OPPOSITE_MOVE_DICT = {
    Move.U2: Move.D2,
    Move.D2: Move.U2,
    Move.L2: Move.R2,
    Move.R2: Move.L2,
    Move.F2: Move.B2,
    Move.B2: Move.F2,
}


def solve_cube(position, db):
    print(' - Phase 4 - - - - - - -')

    if position == SOLVED_POS:
        return []

    sequence = pickle.loads(
        db.query("SELECT move_chain FROM phase_four where position = '%s'" % position).fetchone()[0])


    return sequence
