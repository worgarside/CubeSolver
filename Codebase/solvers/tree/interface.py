from time import sleep, time
from tkinter import *
from tkinter.constants import *


class Interface:
    BG_COLOR = '#dddddd'
    CONTROL_WIDTH = 300
    FACELET_COORDS = [
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
    COLOR_DICT = {
        'W': 'white',
        'O': 'orange',
        'R': 'red',
        'G': 'green',
        'B': 'blue',
        'Y': 'yellow'
    }
    FONT = 'Microsoft\ YaHei\ UI 10'

    def __init__(self, queue):
        """
        Initialises a Tkinter window to show the progress of the tree solver. All of the instance variables are used to
        define components in the window and their dimensions/positions
        :param queue: A link back to the LifoQueue which the generator fills 
        """
        self.queue = queue
        self.root = Tk()
        self.root.title("Rubik's Cube Solver")
        self.root.iconbitmap('Codebase/solvers/tree/cube.ico')
        self.root.resizable(width=False, height=False)
        self.cubie = []
        self.height = 0.75 * self.root.winfo_screenheight()
        canvas_width = self.height * (14 / 11)
        self.width = canvas_width + Interface.CONTROL_WIDTH
        self.root.geometry('%ix%i' % (self.width, self.height))

        self.control_frame = Frame(self.root, width=Interface.CONTROL_WIDTH, height=self.height, bg=Interface.BG_COLOR)
        self.control_frame.pack(side=LEFT)

        self.lbl_title = Label(self.control_frame, text="Rubik's Cube Solver", font='Microsoft\ YaHei\ UI 16 bold',
                               bg=Interface.BG_COLOR)
        self.lbl_title.place(x=Interface.CONTROL_WIDTH / 2, y=40, anchor=CENTER)

        self.lbl_timer = Label(self.control_frame, text='Time: ', font=Interface.FONT, bg=Interface.BG_COLOR)
        self.lbl_timer.place(x=Interface.CONTROL_WIDTH / 20, y=70)

        self.lbl_depth = Label(self.control_frame, text='Depth: ', font=Interface.FONT, bg=Interface.BG_COLOR)
        self.lbl_depth.place(x=Interface.CONTROL_WIDTH / 20, y=100)

        self.lbl_id = Label(self.control_frame, text='Position Count: ', font=Interface.FONT, bg=Interface.BG_COLOR)
        self.lbl_id.place(x=Interface.CONTROL_WIDTH / 20, y=130)

        self.lbl_move_sequence_title = Label(self.control_frame, text='Move Sequence: ', font=Interface.FONT,
                                             bg=Interface.BG_COLOR)
        self.lbl_move_sequence_title.place(x=Interface.CONTROL_WIDTH / 20, y=160)

        self.lbl_move_sequence_moves = Label(self.control_frame, text='U', font='Courier\ New 13',
                                             bg=Interface.BG_COLOR)
        self.lbl_move_sequence_moves.place(x=155, y=162)

        self.canvas = Canvas(self.root, width=canvas_width, height=self.height, bg=Interface.BG_COLOR,
                             highlightthickness=3, highlightcolor='black', highlightbackground='black')
        self.canvas.pack(side=RIGHT)

        self.draw_cube()
        self.start_time = int(time())

    def draw_cube(self):
        """
        Draws the Cube net/facelets on the graphics canvas
        """
        for c in range(len(Interface.FACELET_COORDS)):
            self.cubie.append(
                self.canvas.create_rectangle(
                    *tuple((i * self.height / 11) + (self.height / 11) for i in Interface.FACELET_COORDS[c]),
                    fill='white', outline='black'
                )
            )

    def update_cube_net(self):
        """
        Updates the colors of the facelets on the canvas according to the position highest in the LifoQueue.
        Also updates the values in the relevant labels too
        :return: None, just breaks the process
        """
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
                    self.lbl_id['text'] = 'Position Count: %i' % position.pos_id
                    self.lbl_move_sequence_moves['text'] = ''
                    for m in position.move_sequence:
                        self.lbl_move_sequence_moves['text'] += m.value + '\n'
                    for index, color in enumerate(position.position):
                        self.canvas.itemconfig(self.cubie[index], fill=Interface.COLOR_DICT[color])
                    self.root.update_idletasks()
                    self.root.update()
            input('Press enter to continue')
            self.root.destroy()
        except TclError:
            # catches error when window is prematurely closed
            return
