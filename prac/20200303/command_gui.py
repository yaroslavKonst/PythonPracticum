from tkinter import *

main_frame = Frame()

main_frame.master.columnconfigure(0, weight = 1)
main_frame.master.rowconfigure(0, weight = 1)

main_frame.grid(sticky = "NEWS")
main_frame.columnconfigure(0, weight = 0)
main_frame.columnconfigure(1, weight = 1)
main_frame.rowconfigure(0, weight = 0)

options_frame = Frame(master = main_frame)
options_frame.grid(sticky = "NEWS", column = 0, row = 0)

butt_res = Button(master = options_frame, text = "lsblk")
butt_res.grid(sticky = "EW", column = 0, row = 0)

check_fs = Checkbutton(master = options_frame, text = "Show file system type")
check_fs.grid(sticky = "EWN", column = 0, row = 1)

check_UUID = Checkbutton(master = options_frame, text = "Show file system UUID")
check_UUID.grid(sticky = "EWN", column = 0, row = 2)

out_label = Label(master = main_frame, width = 80)
out_label.grid(sticky = "NEWS", column = 1, row = 0);

check_fs["cursor"] = "hand1"
check_UUID["cursor"] = "hand1"

mainloop()
