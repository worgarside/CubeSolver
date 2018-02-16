from cube.cube_class import Cube, SOLVED_POS, SOLVED_POS_REDUCED, EDGES
from cube.color_class import Color
from cube.moves import dyn_move
from cube.position_class import Position  # (pos_id, position, depth, move_chain)

DEPTH_LIMIT = 5


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

                if (c.position not in position_set) and (all_edges_good(c.position)):
                    id += 1
                    # write all data to file / add to database
                    positions[depth + 1].add(Position(id, c.position, depth + 1, p.move_chain + [str(m)]))
                    position_set.add(c.position)

        depth += 1
        print(depth)

    return positions.values()


def all_edges_good(position):
    """
    WG
    WR
    WB
    WO

    GR
    RB
    BO
    OG

    YG
    YR
    YB
    YO
    """
    # for edge in EDGES:
    #     if position[edge[0]] == Color.RED.value:
    #         if position[edge[1]] == Color.GREEN.value:
    #             pass
    #         elif position[edge[1]] == Color.WHITE.value:
    #             pass
    #         elif position[edge[1]] == Color.BLUE.value:
    #             pass
    #         elif position[edge[1]] == Color.YELLOW.value:
    #             pass
    #         else:
    #             print('error')
    #             exit()
    return True


def code_position(position):
    colors = []
    pos_coded = ""

    for color in position:
        if color not in colors:
            colors.append(color)

        pos_coded += str(colors.index(color))

    return pos_coded
