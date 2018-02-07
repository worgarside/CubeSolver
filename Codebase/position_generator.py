from cube.moves import *
from cube.cube_class import Cube
from position_class import Position # (id, position, depth, parent_id, parent_move, leaf)

DEPTH_LIMIT = 4

def generate_positions(cube, group):
    move_count = len(group)
    positions = {}  # depth: set(position)
    position_set = set()
    depth = 0
    id = 0

    positions[depth] = {Position(0, cube.position, depth, -1, MOVE.NONE, False)}

    while depth < DEPTH_LIMIT:
        positions[depth+1] = set()
        for p in positions[depth]:
            prev_count = 0
            if p.leaf == True:
                print('LEAF')
            for m in group:
                c = Cube(p.position)
                dyn_move(c, m)

                # check symmetry here
                symmetrical = False

                if not symmetrical:
                    if c.position not in position_set:
                        id += 1
                        # write all data to file / add to database
                        positions[depth + 1].add(Position(id, c.position, depth, p.id, m, False))

                        position_set.add(c.position)
                    else:
                        prev_count += 1

            # if all m are in position_set, then p.leaf = True
            if prev_count == 6:
                p.leaf = True

        depth += 1
        print(depth)

    return positions.values()
