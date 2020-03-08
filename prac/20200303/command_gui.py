from tkinter import *
import posix
import sys

def execute_command():
    pipe_fd = posix.pipe()
    pid = posix.fork()
    if pid == 0:
        cmdline = ["lsblk"]
        if check_fs_val.get() or check_UUID_val.get():
            cmdline.append("-o")
            col = "+"
            if check_fs_val.get():
                col += "fstype"
            if check_fs_val.get() and check_UUID_val.get():
                col += ","
            if check_UUID_val.get():
                col += "UUID"
            cmdline.append(col)
        posix.dup2(pipe_fd[1], 1)
        posix.close(pipe_fd[0])
        posix.close(pipe_fd[1]);
        posix.execv("/bin/lsblk", cmdline)
        quit()
    else:
        posix.close(pipe_fd[1])
        ret = bytearray()
        readbytes = posix.read(pipe_fd[0], 1000)
        while readbytes != b"":
            ret += readbytes
            readbytes = posix.read(pipe_fd[0], 1000)
        posix.close(pipe_fd[0])
        posix.wait()
        return str(ret, sys.stdout.encoding)

def button_press():
    out_label["text"] = execute_command()

main_frame = Frame()

main_frame.master.columnconfigure(0, weight = 1)
main_frame.master.rowconfigure(0, weight = 1)

main_frame.grid(sticky = "NEWS")
main_frame.columnconfigure(0, weight = 0)
main_frame.columnconfigure(1, weight = 1)
main_frame.rowconfigure(0, weight = 0)

options_frame = Frame(master = main_frame)
options_frame.grid(sticky = "NEWS", column = 0, row = 0)

butt_res = Button(master = options_frame, text = "lsblk", command = button_press)
butt_res.grid(sticky = "EW", column = 0, row = 0)

check_fs_val = IntVar()
check_fs = Checkbutton(master = options_frame, text = "Show file system type", variable = check_fs_val, onvalue = 1, offvalue = 0)
check_fs.grid(sticky = "EWN", column = 0, row = 1)

check_UUID_val = IntVar()
check_UUID = Checkbutton(master = options_frame, text = "Show file system UUID", variable = check_UUID_val, onvalue = 1, offvalue = 0)
check_UUID.grid(sticky = "EWN", column = 0, row = 2)

out_label = Label(master = main_frame, width = 80, height = 40, justify = LEFT)
out_label.grid(sticky = "NEWS", column = 1, row = 0);

check_fs["cursor"] = "hand1"
check_UUID["cursor"] = "hand1"


mainloop()
