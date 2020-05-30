from tkinter import *
import pyfiglet

class Fig:
    def render(self, *args, **kwargs):
        print("Render")
        self.entry2["text"] = pyfiglet.Figlet(font=pyfiglet.DEFAULT_FONT).renderText(self.entry1.get())

    def __init__(self):
        self.main_frame = Frame()
        self.main_frame.master.rowconfigure(0, weight=1)
        self.main_frame.master.columnconfigure(0, weight=1)
        self.main_frame.grid(sticky="NEWS", row=0, column=0)
        self.main_frame.rowconfigure(1, weight=1)
        self.main_frame.columnconfigure(0, weight=1)

        self.entry1 = Entry(master=self.main_frame)
        self.entry1.grid(sticky="EW", row=0, column=0)
        self.entry1.bind("<Button-1>", self.render)
        self.entry2 = Label(master=self.main_frame, justify=LEFT, font=("Source Code Pro", "12"))
        self.entry2.grid(sticky="NEWS", row=1, column=0)

    def run(self):
        mainloop()
