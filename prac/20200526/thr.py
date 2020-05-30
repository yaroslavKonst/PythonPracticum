import multiprocessing as mp
import sys
import time
import random

def subpr(pipe):
    pipe[1].send(int(pipe[1].recv() + pipe[1].recv()))

p = [mp.Pipe() for i in range(8)]
P = [mp.Process(target=subpr, args=(p[i],)) for i in range(8)]

for a in P:
    a.start()

for a in p:
    a[0].send(10)
    a[0].send(20)

for a in p:
    print(int(a[0].recv()))

for a in P:
    a.join()

print("Finish")
