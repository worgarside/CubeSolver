class Position:
    def __init__(self, id, position, depth, parent_id, parent_move):
        self.id = id
        self.position = position
        self.depth = depth
        self.parent_id = parent_id
        self.parent_move = parent_move

    def __str__(self):
        return str(self.id) + ' ' + self.position + ' ' + str(self.depth) + ' ' + str(self.parent_id) + ' ' + str(
            self.parent_move)[5:]
