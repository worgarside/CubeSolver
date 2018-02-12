from time import sleep
from tkinter import *
from tkinter.constants import *


class Interface:
    def __init__(self, queue):
        self.queue = queue
        self.root = Tk()
        self.root.resizable(width=False, height=False)
        self.width = self.root.winfo_screenwidth() / 2
        self.height = self.root.winfo_screenheight() / 2

        self.root.geometry("%ix%i" % (self.width, self.height))
        self.cubie = []

        control_width = self.width - (self.height * (14 / 11))

        self.control_frame = Frame(self.root, width=control_width, height=self.height, bg='#cdd0d6')
        self.control_frame.pack(side=LEFT)

        self.lbl_title = Label(self.control_frame, text="Rubik's Cube Solver", font='Microsoft\ YaHei\ UI 16 bold',
                               bg='#cdd0d6')
        self.lbl_title.place(x=control_width / 2, y=self.height / 20, anchor=CENTER)

        self.lbl_id = Label(self.control_frame, text='Position ID: ', font='Microsoft\ YaHei\ UI 10', bg='#cdd0d6')
        self.lbl_id.place(x=control_width / 20, y=(1.75 * self.height) / 20)

        self.lbl_depth = Label(self.control_frame, text='Depth: ', font='Microsoft\ YaHei\ UI 10', bg='#cdd0d6')
        self.lbl_depth.place(x=control_width / 20, y=(2.75 * self.height) / 20)

        self.lbl_move_chain_title = Label(self.control_frame, text='Move Chain: ', font='Microsoft\ YaHei\ UI 10',
                                          bg='#cdd0d6')
        self.lbl_move_chain_title.place(x=control_width / 20, y=(3.75 * self.height) / 20)

        self.lbl_move_chain_moves = Label(self.control_frame, text='U', font='Courier\ New 13', bg='#cdd0d6')
        self.lbl_move_chain_moves.place(x=(control_width / 20) + 82, y=(3.76 * self.height) / 20)

        self.canvas = Canvas(self.root, width=self.height * (14 / 11), height=self.height, bg='#cdd0d6',
                             highlightthickness=5, highlightcolor='black', highlightbackground='black')
        self.canvas.pack(side=RIGHT)

        self.draw_cube()

    def draw_cube(self):
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
                self.canvas.create_rectangle(*tuple((i * self.height / 11) + (self.height / 11) for i in coords[c]),
                                             fill='white', outline='black'))

        self.canvas.addtag_all("all")

    def update_position(self):
        color_dict = {
            'W': 'white',
            'O': 'orange',
            'R': 'red',
            'G': 'green',
            'B': 'blue',
            'Y': 'yellow'
        }
        try:
            solved = False
            while not solved:
                sleep(0.005)
                position = self.queue.get()
                if position == 'solved':
                    solved = True
                else:
                    for index, color in enumerate(position.position):
                        self.lbl_id['text'] = "Position ID: %i" % position.id
                        self.lbl_depth['text'] = "Depth: %i" % position.depth
                        self.lbl_move_chain_moves['text'] = position.move_chain
                        self.canvas.itemconfig(self.cubie[index], fill=color_dict[color])
                    self.root.update_idletasks()
                    self.root.update()
        except TclError:
            # catches error when window is closed
            return
