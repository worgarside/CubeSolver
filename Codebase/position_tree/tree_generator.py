from cube.cube_class import Cube, SOLVED_POS
from position_tree.position_class import Position  # (id, position, depth, parent_id, parent_move, move_chain)
from cube.move_class import Move as MOVE
from cube.moves import dyn_move


class TreeGenerator:
    def __init__(self, cube, move_group, window):
        self.window = window
        self.solved = False
        self.positions = {}
        self.depth = 0
        self.pos_id = 0
        self.position_set = set()
        self.positions[self.depth] = {Position(0, cube.position, self.depth, -1, MOVE.NONE, [])}

        self.window.create_elements()
        self.generate_tree(move_group)


    def generate_tree(self, move_group):
        while not self.solved:
            self.positions[self.depth + 1] = []
            for p in self.positions[self.depth]:
                for m in move_group:
                    c = Cube(p.position)
                    dyn_move(c, m)
                    self.pos_id += 1
                    self.positions[self.depth + 1].append(
                        Position(self.pos_id, c.position, self.depth + 1, p.id, str(m), p.move_chain + [str(m)[5:]]))

                    if c.position not in self.position_set:

                        if self.pos_id % 50 == 0:
                            print(self.pos_id)
                            self.window.update_position(c.position)

                        self.pos_id += 1
                        self.positions[self.depth + 1].append(
                            Position(self.pos_id, c.position, self.depth + 1, p.id, str(m),
                                     p.move_chain + [str(m)[5:]]))
                        self.position_set.add(c.position)

                        if c.position == SOLVED_POS:
                            self.solved = True
                            break
                if self.solved:
                    break
            self.depth += 1
        print('SOLVED')