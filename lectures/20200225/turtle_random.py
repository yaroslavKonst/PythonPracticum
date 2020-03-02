from turtle import *
from random import *

# TODO: do not go off screen

def stop_work(x, y):
    global work
    work = False

def sgn(x):
	return 1 if x >= 0 else -1

work = True
getscreen().onclick(stop_work)

pensize(3)

while work:
    color(random(), random(), random())
    circle(randrange(20,60) * sgn(randrange(-1, 1)), randrange(10,200))
