from cube.cube_class import Cube, SOLVED_POS
from cube.move_class import Move
from cube.moves import dyn_move
from cube.position_class import Position  # (pos_id, position, depth, move_chain)

DEPTH_LIMIT = 6


def generate_positions(group):
    positions = {}  # depth: set(position)
    position_set = set()
    depth = 0
    id = 0

    positions[depth] = {Position(0, SOLVED_POS, depth, [])}

    while depth < DEPTH_LIMIT:
        positions[depth + 1] = set()
        for p in positions[depth]:
            for m in group:
                c = Cube(p.position)
                dyn_move(c, m)

                if c.position not in position_set:
                    id += 1
                    # write all data to file / add to database
                    positions[depth + 1].add(Position(id, c.position, depth + 1, p.move_chain + [str(m)]))
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
