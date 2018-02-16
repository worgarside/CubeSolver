from cube.cube_class import Cube, SOLVED_SET
from cube.moves import dyn_move
from cube.position_class import Position  # (id, position, depth, move_chain)


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
    # check orientation symmetry
    # orientation_list = [[Move.NOT_X], [Move.Y2, Move.X], [Move.NOT_X, Move.Y], [Move.NOT_X, Move.NOT_Y], [Move.X],
    #                     [Move.X, Move.Y2], [Move.X, Move.NOT_Y], [Move.X, Move.Y], [Move.X, Move.Z],
    #                     [Move.NOT_X, Move.Z], [Move.X2, Move.Z], [Move.Z], [Move.NOT_X, Move.NOT_Z], [Move.Y, Move.X],
    #                     [Move.NOT_Z], [Move.Y2, Move.Z], [Move.NOT_Y], [Move.Y], [Move.Y2], [Move.X2, Move.Y],
    #                     [Move.Z2], [Move.X2], [Move.X2, Move.Y2]]
    #
    # for move_set in orientation_list:
    #     c = Cube()
    #     for m in move_set:
    #         dyn_move(c, m)
    #     position_set.add(c.position)

    # check if position has already been found
    # avoids move chain equivalence - [U, U] = [U2]
    if position.position in position_set:
        return False

    position_set.add(position.position)
    return True
