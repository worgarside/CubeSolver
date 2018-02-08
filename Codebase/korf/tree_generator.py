from cube.cube_class import Cube, SOLVED_POS
from korf.position_class import Position # (id, position, depth, parent_id, parent_move, leaf)
from cube.move_class import Move as MOVE
from cube.moves import dyn_move

def generator(cube, move_group):
    solved = False
    solution_id = -1
    positions = {}  # depth: set(position)
    depth = 0
    id = 0

    positions[depth] = {Position(0, cube.position, depth, -1, MOVE.NONE)}

    while not solved:
    # while depth < 2:
        for p in positions[depth]:
            positions[depth + 1] = set()
            for m in move_group:
                c = Cube(p.position)
                dyn_move(c, m)
                id += 1

                positions[depth + 1].add(Position(id, c.position, depth + 1, p.id, str(m)))

                # print(c.position == SOLVED_POS)

                if c.position == SOLVED_POS:
                    print("--------------------------------------------------- SOLVED HERE ---------------------------------------------------")
                    solved = True
                    solution_id = id
                    print(solution_id)
                    solution_depth = depth + 1
                    break



        depth += 1
        # print(str(depth) + '  ' + str(solved)[:1])


    test_list = [item for item in positions[2] if item.id == solution_id]

    print(test_list)

    print(positions[0])

    for k in positions.keys():
        # for p in positions[k]:
        #     print(p.id)


    # backtrace
    # return branch moves