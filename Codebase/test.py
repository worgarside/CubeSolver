from tkinter import *

root = Tk()

f = Frame(root, bg="orange", width=500, height=500)
f.pack(side=LEFT, expand=1)

f3 = Frame(f, bg="red", width=500)
f3.pack(side=LEFT, expand=1)

b = Button(f3, text="1", bg="red")
b.grid(row=0, column=0)
b2 = Button(f3, text="2")
b2.grid(row=1, column=1)
b3 = Button(f3, text="3")
b3.grid(row=2, column=2)

root.mainloop()
