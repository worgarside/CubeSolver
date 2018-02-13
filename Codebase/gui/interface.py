from time import sleep, time
from tkinter import *
from tkinter.constants import *

from cube.move_class import Move


class Interface:
    def __init__(self, queue):
        self.queue = queue
        self.root = Tk()
        self.root.title("Rubik's Cube Solver")
        self.root.iconbitmap('Codebase/gui/cube.ico')
        self.root.resizable(width=False, height=False)
        self.cubie = []
        self.height = 0.75 * self.root.winfo_screenheight()
        canvas_width = self.height * (14 / 11)
        control_width = 300
        self.width = canvas_width + control_width
        self.root.geometry('%ix%i' % (self.width, self.height))

        bg_color = '#dddddd'

        self.control_frame = Frame(self.root, width=control_width, height=self.height, bg=bg_color)
        self.control_frame.pack(side=LEFT)

        self.lbl_title = Label(self.control_frame, text="Rubik's Cube Solver", font='Microsoft\ YaHei\ UI 16 bold',
                               bg=bg_color)
        self.lbl_title.place(x=control_width / 2, y=40, anchor=CENTER)

        self.lbl_timer = Label(self.control_frame, text='Time: ', font='Microsoft\ YaHei\ UI 10', bg=bg_color)
        self.lbl_timer.place(x=control_width / 20, y=70)

        self.lbl_depth = Label(self.control_frame, text='Depth: ', font='Microsoft\ YaHei\ UI 10', bg=bg_color)
        self.lbl_depth.place(x=control_width / 20, y=100)

        self.lbl_id = Label(self.control_frame, text='Position Count: ', font='Microsoft\ YaHei\ UI 10', bg=bg_color)
        self.lbl_id.place(x=control_width / 20, y=130)

        self.lbl_move_chain_title = Label(self.control_frame, text='Move Chain: ', font='Microsoft\ YaHei\ UI 10',
                                          bg=bg_color)
        self.lbl_move_chain_title.place(x=control_width / 20, y=160)

        self.lbl_move_chain_moves = Label(self.control_frame, text='U', font='Courier\ New 13', bg=bg_color)
        self.lbl_move_chain_moves.place(x=125, y=162)

        self.canvas = Canvas(self.root, width=canvas_width, height=self.height, bg=bg_color,
                             highlightthickness=3, highlightcolor='black', highlightbackground='black')
        self.canvas.pack(side=RIGHT)

        self.draw_cube()
        self.start_time = int(time())

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

    def update_cube_net(self):
        color_dict = {
            'W': 'white',
            'O': 'orange',
            'R': 'red',
            'G': 'green',
            'B': 'blue',
            'Y': 'yellow'
        }
        move_dict = {Move.U: 'U ', Move.NOT_U: "U'", Move.U2: 'U2', Move.D: 'D ', Move.NOT_D: "D'", Move.D2: 'D2',
                     Move.L: 'L ', Move.NOT_L: "L'", Move.L2: 'L2', Move.R: 'R ', Move.NOT_R: "R'", Move.R2: 'R2',
                     Move.F: 'F ', Move.NOT_F: "F'", Move.F2: 'F2', Move.B: 'B ', Move.NOT_B: "B'", Move.B2: 'B2'}
        try:
            solved = False
            next_solved = False
            while not solved:
                sleep(0.005)
                position = self.queue.get()
                if next_solved:
                    solved = True
                if position == 'solved':
                    next_solved = True
                else:
                    minutes, secs = divmod((int(time()) - self.start_time), 60)
                    self.lbl_timer['text'] = 'Time: %02i:%02i' % (minutes, secs)
                    self.lbl_depth['text'] = 'Depth: %i' % position.depth
                    self.lbl_id['text'] = 'Position Count: %i' % position.id
                    self.lbl_move_chain_moves['text'] = ''
                    for m in position.move_chain:
                        self.lbl_move_chain_moves['text'] += move_dict[m] + '\n'
                    for index, color in enumerate(position.position):
                        self.canvas.itemconfig(self.cubie[index], fill=color_dict[color])
                    self.root.update_idletasks()
                    self.root.update()
        except TclError:
            # catches error when window is closed
            return
