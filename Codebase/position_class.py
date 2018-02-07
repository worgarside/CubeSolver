class Position:
    def __init__(self, id, position, depth, parent, parent_move, leaf):
        self.id = id
        self.position = position
        self.depth = depth
        self.parent = parent
        self.parent_move = parent_move
        self.leaf = leaf

    def __str__(self):
        return str(self.id) + ', ' + self.position