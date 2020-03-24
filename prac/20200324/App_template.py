from tkinter import *

class App(Frame):
    def __init__(self, master=None, Title="Application", **kwargs):
        Frame.__init__(self, master, **kwargs)
        self.master.rowconfigure(0, weight = 1)
        self.master.columnconfigure(0, weight = 1)
        self.master.title(Title)
        self.grid(sticky = "NEWS")
        self.rowconfigure(0, weight = 1)
        self.columnconfigure(0, weight = 1)

A = App()
A.mainloop()
