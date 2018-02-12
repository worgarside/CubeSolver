from tkinter import *
from time import sleep


class Interface():
    def __init__(self, queue, width=560, height=440):
        self.queue = queue
        self.root = Tk()
        self.canvas = Canvas(self.root, width=width, height=height)
        self.color_dict = {
            'W': 'white',
            'O': 'orange',
            'R': 'red',
            'G': 'green',
            'B': 'blue',
            'Y': 'yellow'
        }
        self.cubie = []
        self.create_elements()


    def create_elements(self):
        coords = [
            (3, 0, 4, 1), (4, 0, 5, 1), (5, 0, 6, 1),
            (3, 1, 4, 2), (4, 1, 5, 2), (5, 1, 6, 2),
            (3, 2, 4, 3), (4, 2, 5, 3), (5, 2, 6, 3),
            (0, 3, 1, 4), (1, 3, 2, 4), (2, 3, 3, 4), (3, 3, 4, 4), (4, 3, 5, 4), (5, 3, 6, 4), (6, 3, 7, 4),
            (7, 3, 8, 4), (8, 3, 9, 4), (9, 3, 10, 4), (10, 3, 11, 4), (11, 3, 12, 4),
            (0, 4, 1, 5), (1, 4, 2, 5), (2, 4, 3, 5), (3, 4, 4, 5), (4, 4, 5, 5), (5, 4, 6, 5), (6, 4, 7, 5),
            (7, 4, 8, 5), (8, 4, 9, 5), (9, 4, 10, 5), (10, 4, 11, 5), (11, 4, 12, 5),
            (0, 5, 1, 6), (1, 5, 2, 6), (2, 5, 3, 6), (3, 5, 4, 6), (4, 5, 5, 6), (5, 5, 6, 6), (6, 5, 7, 6),
            (7, 5, 8, 6), (8, 5, 9, 6), (9, 5, 10, 6), (10, 5, 11, 6), (11, 5, 12, 6),
            (3, 6, 4, 7), (4, 6, 5, 7), (5, 6, 6, 7),
            (3, 7, 4, 8), (4, 7, 5, 8), (5, 7, 6, 8),
            (3, 8, 4, 9), (4, 8, 5, 9), (5, 8, 6, 9),
        ]
        for c in range(len(coords)):
            self.cubie.append(
                self.canvas.create_rectangle(*tuple((i * 40) + 40 for i in coords[c]), fill='red', outline='white'))

        self.canvas.pack()

    def update_position(self):
        while not self.queue.empty():
            position = self.queue.get()
            for index, color in enumerate(position):
                self.canvas.itemconfig(self.cubie[index], fill=self.color_dict[color])

            self.root.update_idletasks()
            self.root.update()
        print('Queue Empty')
