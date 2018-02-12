from tkinter import *
from tkinter.constants import *
from time import sleep


def set_aspect(content, padding_frame, aspect_ratio):
    def enforce_aspect_ratio(event):
        desired_width = event.width
        desired_height = int(event.width / aspect_ratio)

        if desired_height > event.height:
            desired_height = event.height
            desired_width = int(event.height * aspect_ratio)

        content.place(in_=padding_frame, x=0, y=0,
                      width=desired_width, height=desired_height)

    padding_frame.bind("<Configure>", enforce_aspect_ratio)


class ResizingCanvas(Canvas):
    def __init__(self, parent, **kwargs):
        Canvas.__init__(self, parent, **kwargs)
        self.bind("<Configure>", self.on_resize)
        self.height = self.winfo_reqheight()
        self.width = self.winfo_reqwidth()

    def on_resize(self, window):
        # determine the ratio of old width/height to new width/height
        x_scale = float(window.width) / self.width
        y_scale = float(window.height) / self.height
        self.width = window.width
        self.height = window.height
        # resize the canvas
        self.config(width=self.width, height=self.height)
        # rescale all the objects tagged with the "all" tag
        self.scale("all", 0, 0, x_scale, y_scale)


class Interface():
    def __init__(self, queue, canvas_width=560, canvas_height=440):
        self.queue = queue
        self.root = Tk("Rubik's Cube Solver")
        self.pad_frame = Frame(borderwidth=0, width=self.root.winfo_screenwidth() / 2,
                               height=self.root.winfo_screenheight() / 2)
        self.pad_frame.grid(row=0, column=0, sticky="nsew", padx=0, pady=0)
        self.content_frame = Frame(self.root)
        set_aspect(self.content_frame, self.pad_frame, aspect_ratio=canvas_width / canvas_height)
        self.root.rowconfigure(0, weight=1)
        self.root.columnconfigure(0, weight=1)
        self.canvas = ResizingCanvas(self.content_frame, width=canvas_width, height=canvas_height)
        self.canvas.pack(fill=BOTH, expand=YES)

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
                self.canvas.create_rectangle(*tuple((i * 40) + 40 for i in coords[c]), fill='white', outline='black'))

        self.canvas.addtag_all("all")

    def update_position(self):
        try:
            solved = False
            while not solved:
                sleep(0.005)
                position = self.queue.get()
                if position == 'solved':
                    solved = True
                else:
                    for index, color in enumerate(position):
                        self.canvas.itemconfig(self.cubie[index], fill=self.color_dict[color])
                    self.root.update_idletasks()
                    self.root.update()
        except TclError:
            # catches error when window is closed
            return
