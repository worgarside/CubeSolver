class Position:
    def __init__(self, position, move_sequence):
        self.position = position
        self.move_sequence = move_sequence

    def __str__(self):
        return self.position + ' ' + str(self.move_sequence)
