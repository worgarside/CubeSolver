from cube.cube_class import Cube, SOLVED_POS
from cube.move_class import Move as MOVE
from cube.moves import dyn_move
from tree_solver.position_class import Position  # (id, position, depth, parent_id, parent_move, move_chain)


def generate_tree(cube, move_group, queue):
    solved = False
    positions = {}
    depth = 0
    pos_id = 0
    position_set = set()
    positions[depth] = {Position(0, cube.position, depth, -1, MOVE.NONE, "")}
    move_dict = {MOVE.U: "U ", MOVE.NOT_U: "U'", MOVE.U2: "U2", MOVE.D: "D ", MOVE.NOT_D: "D'", MOVE.D2: "D2",
                 MOVE.L: "L ", MOVE.NOT_L: "L'", MOVE.L2: "L2", MOVE.R: "R ", MOVE.NOT_R: "R'", MOVE.R2: "R2",
                 MOVE.F: "F ", MOVE.NOT_F: "F'", MOVE.F2: "F2", MOVE.B: "B ", MOVE.NOT_B: "B'", MOVE.B2: "B2", }

    while not solved:
        positions[depth + 1] = []
        print(depth)
        for p in positions[depth]:
            for m in move_group:
                c = Cube(p.position)
                dyn_move(c, m)
                pos_id += 1

                if c.position not in position_set:

                    new_pos = Position(pos_id, c.position, depth + 1, p.id, str(m), p.move_chain + move_dict[m] + "\n")

                    if pos_id % 50 == 0:
                        queue.put(new_pos)

                    pos_id += 1
                    positions[depth + 1].append(new_pos)
                    position_set.add(new_pos.position)

                    if new_pos.position == SOLVED_POS:
                        solved = True
                        queue.put(new_pos)
                        break
            if solved:
                break
        depth += 1


    queue.put('solved')
