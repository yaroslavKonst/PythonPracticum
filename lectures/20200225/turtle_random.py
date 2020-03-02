from turtle import *
from random import *

# TODO: do not go off screen
# TODO: eliminate small radius

def stop_work(x, y):
    global work
    work = False

work = True
getscreen().onclick(stop_work)

pensize(3)

while work:
    color(random(), random(), random())
    circle(randrange(-60,60), randrange(10,200))
