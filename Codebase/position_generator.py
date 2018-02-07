from cube.moves import *
from cube.cube_class import Cube
from position_class import Position # (id, position, depth, parent, parent_move, leaf)

DEPTH_LIMIT = 5

def generate_positions(cube, group):
    positions = {}  # depth: set(position)
    depth = 0
    id = 0

    positions[depth] = {Position(0, cube.position, depth, -1, MOVE.NONE, False)}

    while depth < DEPTH_LIMIT:
        positions[depth+1] = set()
        for p in positions[depth]:
            p_id = p.id
            for m in group:
                c = Cube(p.position)
                dyn_move(c, m)

                # check symmetry here
                symmetrical = False

                if not symmetrical:
                    id += 1
                    positions[depth + 1].add(Position(id, c.position, depth, p_id, m, False))

        depth += 1
        print(depth)

    return positions.values()
