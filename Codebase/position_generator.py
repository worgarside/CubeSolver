from cube.moves import *
from cube.cube_class import Cube
from position_class import Position # (id, position, depth, parent, parent_move, leaf)

DEPTH_LIMIT = 10

def generate_positions(cube, group):
    positions = {}  # depth: set(position)
    depth = 0
    id = 0

    positions[depth] = {Position(0, cube.position, depth, None, MOVE.NONE, False)}

    while depth < DEPTH_LIMIT:
        positions[depth+1] = set()
        for p in positions[depth]:
            for m in group:
                c = Cube(p.position)
                dyn_move(c, m)

                # check symmetry here
                symmetrical = False

                if not symmetrical:
                    positions[depth + 1].add(Position(id, c.position, depth, None, m, False))

        depth += 1
        print(depth)

    return positions.values()
