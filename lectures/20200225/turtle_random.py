from turtle import *
from random import *

def stop_work(x, y):
    global work
    work = False

def sgn(x):
    return 1 if x >= 0 else -1

work = True
getscreen().onclick(stop_work)

ret_base = False

mode("standard")
speed(0)

pensize(3)

while work:
    width, height = getscreen().window_width(), getscreen().window_height()
    color(random(), random(), random())
    if (abs(xcor()) > width / 2 - 60) or (abs(ycor()) > height / 2 - 60) or ret_base:
        ret_base = True
        hdg = heading() - towards(0, 0)
        while hdg < 0:
            hdg += 360
        while hdg >= 360:
            hdg -= 360
        if hdg > 180:
            circle(randrange(20,60), randrange(10,85))
        else:
            circle(-randrange(20,60), randrange(10,85))
        if (abs(xcor()) < width / 2 - 80) and (abs(ycor()) < height / 2 - 80):
            ret_base = False
    else:
        circle(randrange(20,60) * sgn(randrange(-1, 1)), randrange(10,200))
