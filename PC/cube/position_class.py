class Position:
    def __init__(self, pos_id, position, depth, move_chain):
        self.pos_id = pos_id
        self.position = position
        self.depth = depth
        self.move_chain = move_chain

    def __str__(self):
        return str(self.pos_id) + ' ' + self.position + ' ' + str(self.depth) + ' ' + str(self.move_chain)
