from cube.cube_class import Cube, SOLVED_POS
from cube.move_class import Move
from cube.moves import dyn_move
from cube.position_class import Position  # (pos_id, position, depth, move_sequence)

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

    sequence = db.query("SELECT move_chain FROM phase_four where position = '%s'" % position).fetchone()[0]

    print(sequence)




def cube_is_good(cube):
    sides = [cube.left, cube.right, cube.front, cube.back]

    for side in sides:
        for facelet in side:
            if facelet != side[4]:
                return False
    return True
