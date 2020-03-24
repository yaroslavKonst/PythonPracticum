from tkinter import *
from threading import Timer

main_frame = Frame()
main_frame.master.columnconfigure(0, weight = 1)
main_frame.grid(sticky = "NEWS", row = 0, column = 0)

main_frame.columnconfigure(0, weight = 0)
main_frame.columnconfigure(1, weight = 1)
main_frame.columnconfigure(2, weight = 1)

number_entry = Entry(master = main_frame)
number_entry.grid(sticky = "NEW", row = 0, column = 1)

def new_item():
    global T
    global a
    if a % 2 == 0:
        a = a / 2
    else:
        a = 3 * a + 1
    out_label["text"] = str(a)
    T = Timer(1 / N, new_item)
    if W:
        T.start()

N, W = 5, False
T = Timer(1 / N, new_item)
a = 0

def butt_press():
    global a
    global W
    if not W:
        s = number_entry.get()
        if s.isnumeric():
            a = int(s)
            start_stop_button["text"] = "Stop"
            W = True
            T.start()
    else:
        W = False
        start_stop_button["text"] = "Start"

start_stop_button = Button(master = main_frame, command = butt_press, text = "Start", cursor = "hand1")
start_stop_button.grid(sticky = "NEW", row = 0, column = 0)

out_label = Label(master = main_frame)
out_label.grid(sticky = "NEW", row = 0, column = 2)

mainloop()
