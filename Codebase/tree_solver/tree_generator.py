from cube.cube_class import Cube, SOLVED_SET
from cube.move_class import Move
from cube.moves import dyn_move
from tree_solver.position_class import Position  # (id, position, depth, move_chain)


def generate_tree(cube, move_group, queue):
    solved = False
    positions = {}
    position_set = set()
    depth = 0
    pos_id = 0
    positions[depth] = {Position(0, cube.position, depth, [])}

    while not solved:
        positions[depth + 1] = []
        for p in positions[depth]:
            for m in move_group:
                c = Cube(p.position)
                dyn_move(c, m)
                new_pos = Position(pos_id, c.position, depth + 1, p.move_chain + [m])

                if valid_pos(new_pos, position_set):
                    pos_id += 1
                    queue.put(new_pos)
                    positions[depth + 1].append(new_pos)

                    if new_pos.position in SOLVED_SET:
                        solved = True
                        queue.put('solved')
                        queue.put(new_pos)
                        break
            if solved:
                break
        depth += 1


def valid_pos(position, position_set):
    # check if position has already been found
    # avoids move chain equivalence - [U, U] = [U2]
    if position.position in position_set:
        return False

    position_set.add(position.position)
    return True
