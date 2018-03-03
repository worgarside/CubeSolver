class Position:
    def __init__(self, depth, position, move_sequence):
        self.depth = depth
        self.position = position
        self.move_sequence = move_sequence

    def __str__(self):
        return self.position + ' ' + str(self.move_sequence)
