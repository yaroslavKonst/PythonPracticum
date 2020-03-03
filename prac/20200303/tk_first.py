from tkinter import *

f = Frame()
f.master.columnconfigure(0, weight=1)
f.master.rowconfigure(0, weight=1)
f.grid(sticky="NEWS")

f.columnconfigure(0, weight=1)
f.columnconfigure(1, weight=2)

b1 = Button(master=f, text="Button1")
b2 = Button(master=f, text="Button2")

b1.grid(sticky="EW")
b2.grid(sticky="EW", column=1, row=0)

mainloop()
