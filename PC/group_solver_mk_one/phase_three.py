from cube.cube_class import Cube
from cube.move_class import Move
from cube.moves import dyn_move
from cube.position_class import Position  # (pos_id, position, depth, move_sequence)

MOVE_GROUP = [Move.U2, Move.D2, Move.L2, Move.R2, Move.F, Move.B]

OPPOSITE_MOVE_DICT = {
    Move.U2: Move.D2,
    Move.D2: Move.U2,
    Move.L2: Move.R2,
    Move.R2: Move.L2,
    Move.F: Move.B,
    Move.B: Move.F,
}


def make_all_faces_good(position):
    print(' - Phase 3 - - - - - - -')
    position_set = set()
    positions = {}  # depth: set(position)
    depth = 0

    positions[depth] = [Position(depth, position, [Move.NONE])]
    if cube_is_good(Cube(position)):
        return Position(depth, position, [])

    while depth < 15:
        print('%i... ' % depth, end='')
        positions[depth + 1] = []
        for p in positions[depth]:
            for m in MOVE_GROUP:
                # avoids Half Turns or Extended Half Turns
                if p.move_sequence[-1] == m or \
                        (p.move_sequence[-1] == OPPOSITE_MOVE_DICT[m] and p.move_sequence[-2] == m):
                    continue

                c = Cube(p.position, True)
                dyn_move(c, m)

                if c.position not in position_set:
                    if cube_is_good(c):
                        return Position(depth, c.position, p.move_sequence + [m])
                    positions[depth + 1].append(Position(depth, c.position, p.move_sequence + [m]))
                    position_set.add(c.position)

        depth += 1
    print('FAIL')


def cube_is_good(cube):
    sides = [cube.left, cube.right, cube.front, cube.back]

    for side in sides:
        for facelet in side:
            if facelet != side[4]:
                return False
    return True
