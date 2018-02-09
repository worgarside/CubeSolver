from cube.cube_class import Cube, SOLVED_POS
from korf.position_class import Position # (id, position, depth, parent_id, parent_move, leaf)
from cube.move_class import Move as MOVE
from cube.moves import dyn_move

def generator(db, cube, move_group):
    solved = False
    solution_id = -1
    positions = {}  # depth: set(position)
    depth = 0
    id = 0
    added = 0
    positions[depth] = {Position(0, cube.position, depth, -1, MOVE.NONE)}

    while not solved:
    # while depth < 2:
        positions[depth + 1] = []
        for p in positions[depth]:
            for m in move_group:
                c = Cube(p.position)
                dyn_move(c, m)
                id += 1
                positions[depth + 1].append(Position(id, c.position, depth + 1, p.id, str(m)))
                added += 1

                if c.position == SOLVED_POS:
                    solved = True
                    solution_id = id
                    break

        depth += 1

    # print('\n----------------------------------------\n')
    # print(added)
    for depth, position_set in positions.items():
        for p in position_set:
            db.query("INSERT INTO positions VALUES (?, ?, ?, ?, ?)", (p.id, p.position, p.depth, p.parent_id, str(p.parent_move)))

    backtrace(solution_id, positions)
    # backtrace
    # return branch moves

def backtrace(solution_id, position_dict):
    target_id = solution_id
    move_list= []


    for depth, position_set in sorted(list(position_dict.items()), key=lambda x: x[0], reverse=True):
        position = [item for item in position_set if item.id == target_id][0]
        move_list.append(position.parent_move)
        target_id = position.parent_id

    print(move_list)