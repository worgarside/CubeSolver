from cube.cube_class import Cube, SOLVED_POS
from tree_solver.position_class import Position  # (id, position, depth, parent_id, parent_move, move_chain)
from cube.move_class import Move as MOVE
from cube.moves import dyn_move


def generate_tree(cube, move_group, queue):
    solved = False
    positions = {}
    depth = 0
    pos_id = 0
    position_set = set()
    positions[depth] = {Position(0, cube.position, depth, -1, MOVE.NONE, [])}
    solution_move_chain = []

    while not solved:
        positions[depth + 1] = []
        for p in positions[depth]:
            for m in move_group:
                c = Cube(p.position)
                dyn_move(c, m)
                pos_id += 1

                if c.position not in position_set:

                    new_pos = Position(pos_id, c.position, depth + 1, p.id, str(m), p.move_chain + [str(m)[5:]])

                    if pos_id % 1 == 0:
                        queue.put(new_pos)

                    pos_id += 1
                    positions[depth + 1].append(new_pos)
                    position_set.add(new_pos.position)

                    if new_pos.position == SOLVED_POS:
                        solved = True
                        solution_move_chain = p.move_chain + [str(m)[5:]]
                        break
            if solved:
                break
        depth += 1

    queue.put('solved')
