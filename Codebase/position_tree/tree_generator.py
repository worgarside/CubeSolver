from cube.cube_class import Cube, SOLVED_POS
from position_tree.position_class import Position  # (id, position, depth, parent_id, parent_move, move_chain)
from cube.move_class import Move as MOVE
from cube.moves import dyn_move


class TreeGenerator:
    def __init__(self, cube, move_group):
        print('New TreeGenerator')
        self.move_group = move_group
        self.solved = False
        self.positions = {}
        self.depth = 0
        self.pos_id = 0
        self.position_set = set()
        self.positions[self.depth] = {Position(0, cube.position, self.depth, -1, MOVE.NONE, [])}

    def generate_tree(self, queue):
        print('Generating tree...')
        solution_move_chain = []
        while not self.solved:
            print('.', end='')
            self.positions[self.depth + 1] = []
            for p in self.positions[self.depth]:
                for m in self.move_group:
                    c = Cube(p.position)
                    dyn_move(c, m)
                    self.pos_id += 1
                    self.positions[self.depth + 1].append(
                        Position(self.pos_id, c.position, self.depth + 1, p.id, str(m), p.move_chain + [str(m)[5:]]))

                    if c.position not in self.position_set:

                        # if self.pos_id % 50 == 0:
                            # print(self.pos_id)
                        queue.put(c.position)

                        self.pos_id += 1
                        self.positions[self.depth + 1].append(
                            Position(self.pos_id, c.position, self.depth + 1, p.id, str(m),
                                     p.move_chain + [str(m)[5:]]))
                        self.position_set.add(c.position)

                        if c.position == SOLVED_POS:
                            self.solved = True
                            solution_move_chain = p.move_chain + [str(m)[5:]]
                            break
                if self.solved:
                    break
            self.depth += 1
        print("\nSOLVED: %s" % str(solution_move_chain))
