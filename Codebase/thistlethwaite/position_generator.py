from cube.moves import dyn_move
from cube.cube_class import Cube
from thistlethwaite.position_class import Position # (id, position, depth, parent_id, parent_move)

DEPTH_LIMIT = 6

def generate_positions(cube, group):
    positions = {}  # depth: set(position)
    position_set = set()
    depth = 0
    id = 0

    positions[depth] = {Position(0, cube.position, depth, -1, MOVE.NONE)}

    while depth < DEPTH_LIMIT:
        positions[depth+1] = set()
        for p in positions[depth]:
            for m in group:
                c = Cube(p.position)
                dyn_move(c, m)

                if c.position not in position_set:
                    id += 1
                    # write all data to file / add to database
                    positions[depth + 1].add(Position(id, c.position, depth + 1, p.id, str(m)[5:]))
                    position_set.add(c.position)

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