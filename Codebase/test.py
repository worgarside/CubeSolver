from tkinter import *
from tkinter.constants import *



def set_aspect(content_frame, pad_frame, aspect_ratio):

    def enforce_aspect_ratio(event):
        desired_width = event.width
        desired_height = int(event.width / aspect_ratio)

        if desired_height > event.height:
            desired_height = event.height
            desired_width = int(event.height * aspect_ratio)

        content_frame.place(in_=pad_frame, x=0, y=0,
                            width=desired_width, height=desired_height)

    pad_frame.bind("<Configure>", enforce_aspect_ratio)




root = Tk()

pad_frame = Frame(borderwidth=0, background="bisque", width=200, height=200)
pad_frame.grid(row=0, column=0, sticky="nsew", padx=10, pady=20)
content_frame = Frame(root, borderwidth=5, relief=GROOVE, background="blue")
Label(content_frame, text='content').pack()
set_aspect(content_frame, pad_frame, aspect_ratio=2.0 / 1.0)
root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)

root.mainloop()
