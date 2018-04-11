from cube.cube_class import Cube, Position, SOLVED_POS
from cube.moves import dyn_move
import pickle


def generate_tree(cube, move_group, queue):
    solved = False
    positions = {}
    position_set = set()
    depth = 0
    current_id = 0
    positions[depth] = {Position(depth, cube.position, [], current_id)}

    while not solved:
        positions[depth + 1] = []
        for p in positions[depth]:
            for m in move_group:
                c = Cube(p.position)
                dyn_move(c, m)
                new_pos = Position(depth, c.position, p.move_sequence + [m], current_id)

                if valid_pos(new_pos, position_set):
                    current_id += 1
                    queue.put(new_pos)
                    positions[depth + 1].append(new_pos)

                    if new_pos.position == SOLVED_POS:
                        solved = True
                        queue.put('solved')
                        queue.put(new_pos)

                        with open('Codebase/solvers/tree/solution.pickle', 'wb') as solution:
                            pickle.dump(new_pos.move_sequence, solution, protocol=pickle.HIGHEST_PROTOCOL)
                        break
            if solved:
                break
        depth += 1



def valid_pos(position, position_set):
    if position.position in position_set:
        return False

    position_set.add(position.position)
    return True
