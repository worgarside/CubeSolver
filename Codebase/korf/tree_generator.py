from cube.cube_class import Cube, SOLVED_POS
from korf.position_class import Position # (id, position, depth, parent_id, parent_move, move_chain)
from cube.move_class import Move as MOVE
from cube.moves import dyn_move
import sys

def generator(db, cube, move_group):
    solved = False
    solution_id = -1
    positions = {}
    depth = 0
    id = 0
    positions[depth] = {Position(0, cube.position, depth, -1, MOVE.NONE, [])}
    solution_move_chain = []

    while not solved:
        positions[depth + 1] = []
        for p in positions[depth]:
            for m in move_group:
                c = Cube(p.position)
                dyn_move(c, m)
                id += 1
                positions[depth + 1].append(Position(id, c.position, depth + 1, p.id, str(m), p.move_chain + [str(m)[5:]]))

                if id % 47 == 0:
                    sys.stdout.write("\rDepth: %i     Pos ID: %i     Cube: %s     Move Chain: %s                         " % (depth, id, c.position, p.move_chain + [str(m)[5:]]))
                    sys.stdout.flush()

                if c.position == SOLVED_POS:
                    solved = True
                    solution_id = id
                    solution_move_chain = p.move_chain + [str(m)[5:]]
                    break

        depth += 1

    sys.stdout.write("\rDepth: %i     Pos ID: %i     Cube: %s     Move Chain: %s                         " %
                     (depth, solution_id, SOLVED_POS, solution_move_chain))
    sys.stdout.flush()
