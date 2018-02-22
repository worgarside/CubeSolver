class Position:
    def __init__(self, position, depth, move_chain):
        self.position = position
        self.depth = depth
        self.move_chain = move_chain

    def __str__(self):
        return self.position + ' ' + str(self.depth) + ' ' + str(self.move_chain)
