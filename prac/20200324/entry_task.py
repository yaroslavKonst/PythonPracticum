from tkinter import *

class App(Frame):

    def dec(self):
        obj = self
        def upd_E3(*argp, **argn):
            nonlocal obj
            obj.E3["text"] = obj.E1.selection_get() if obj.E1.selection_present() else ""
        return upd_E3


    def __init__(self, master=None, Title="Application", **kwargs):
        Frame.__init__(self, master, **kwargs)
        self.master.rowconfigure(0, weight = 1)
        self.master.columnconfigure(0, weight = 1)
        self.master.title(Title)
        self.grid(sticky = "NEWS")
        self.rowconfigure(0, weight = 1)
        self.columnconfigure(0, weight = 1)

        self.S = StringVar()
        self.E1 = Entry(self, textvariable = self.S)
        self.E1.grid(sticky = "NEWS", row = 0, column = 0)
        self.E2 = Entry(self, textvariable = self.S)
        self.E2.grid(sticky = "NEWS", row = 0, column = 1)
        self.E3 = Label(self)
        self.E3.grid(sticky = "NEWS", row = 1, column = 0)
        self.E1.bind("<KeyRelease>", self.dec())

A = App()

A.mainloop()
