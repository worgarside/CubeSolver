from cube.moves import *
from cube.cube_class import Cube
from position_class import Position # (id, position, depth, parent_id, parent_move)

DEPTH_LIMIT = 4

def generate_positions(cube, group):
    positions = {}  # depth: set(position)
    position_set = set()
    coded_position_set = set()
    depth = 0
    id = 0

    positions[depth] = {Position(0, cube.position, depth, -1, MOVE.NONE)}

    while depth < DEPTH_LIMIT:
        positions[depth+1] = set()
        for p in positions[depth]:
            prev_count = 0
            for m in group:
                c = Cube(p.position)
                dyn_move(c, m)

                # check symmetry here
                symmetrical = False

                if not symmetrical:
                    # use a set to check duplicates
                    # if c.position not in position_set:
                    if code_position(c.position) not in coded_position_set:
                        id += 1
                        # write all data to file / add to database
                        positions[depth + 1].add(Position(id, c.position, depth, p.id, m))

                        position_set.add(c.position)
                        coded_position_set.add(code_position(c.position))
                    else:
                        prev_count += 1

        depth += 1
        print(depth)

    return positions.values()


def code_position(position):
    colors = []
    pos_coded = ""

    for color in position:
        if color not in colors:
            colors.append(color)

        pos_coded += str(colors.index(color))

    return pos_coded