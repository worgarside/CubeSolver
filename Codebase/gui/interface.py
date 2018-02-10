from tkinter import *

class Interface():
    def __init__(self, width = 500, height = 500):
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
        self.canvas.pack()
        self.update_canvas()

    def update_canvas(self):
        self.root.update_idletasks()
        self.root.update()
        # self.root.mainloop()

    def create_elements(self):
        self.cubie_1 = self.canvas.create_rectangle(20, 20, 100, 100, fill='white')
        print('creating things')

    def update_position(self, position):
        self.canvas.itemconfig(self.cubie_1, fill=self.color_dict[position[0]])
        self.update_canvas()