import pickle

from cube.cube_class import Cube, Position
from cube.moves import dyn_move


def generate_tree(cube, moveset, queue):
    """
    Generates a tree of positions at runtime from the scanned position with the aim of finding the solved position
    :param cube: The scanned Cube
    :param moveset: The moveset to be used in creating the tree
    :param queue: The LifoQueue new positions are placed in to be passed to the GUI
    """
    solved = False
    positions = {}
    position_set = set()
    depth = 1
    current_id = 0
    positions[0] = {Position(depth, cube.position, [], current_id)}

    while not solved:
        positions[depth] = []
        # For all previous depth positions, perform each of the moves on each position
        for pos_object in positions[depth - 1]:
            for m in moveset:
                c = Cube(pos_object.position)
                dyn_move(c, m)
                new_pos = Position(depth, c.position, pos_object.move_sequence + [m], current_id)

                if valid_pos(c.position, position_set):
                    current_id += 1
                    queue.put(new_pos)
                    positions[depth].append(new_pos)

                    if new_pos.position == Cube.SOLVED_POS:
                        solved = True
                        queue.put('solved')
                        queue.put(new_pos)

                        """
                        Save the serialized solve sequence to a file for accessing by the main process. This may not 
                        be the best way of returning the variable, but the processes do not share memory so this is
                        the workaround for now
                        """
                        with open('Codebase/solvers/tree/solution.pickle', 'wb') as solution:
                            pickle.dump(new_pos.move_sequence, solution, protocol=pickle.HIGHEST_PROTOCOL)
                        break
            if solved:
                break
        depth += 1


def valid_pos(position, position_set):
    """
    Validity checker for the positions
    :param position: Position string to be validated
    :param position_set: The set of positions being compared against
    :return: Boolean to say if the position is valid (i.e. is is not a duplicate)
    """
    if position in position_set:
        return False

    position_set.add(position)
    return True
