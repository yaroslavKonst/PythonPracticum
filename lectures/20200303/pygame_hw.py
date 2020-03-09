import pygame
from random import randrange

class Line:
    def __init__(self, x1, y1, x2, y2):
        self.X1, self.Y1 = x1, y1
        self.X2, self.Y2 = x2, y2

def get_random_color():
    return pygame.Color(randrange(100,256), randrange(100,256),randrange(100,256))

def draw_line(screen, color, x1, y1, x2, y2):
    if x1 == x2 and y1 == y2:
        screen.set_at((x1, y1), color)
        return
    if abs(x2 - x1) > abs(y2 - y1):
        if x2 < x1:
            x1, x2, y1, y2 = x2, x1, y2, y1
        i = x1
        k = (y2 - y1) / (x2 - x1)
        while i <= x2:
            screen.set_at((i, int((i - x1) * k + y1)), color)
            i += 1
    else:
        if y2 < y1:
            x1, x2, y1, y2 = x2, x1, y2, y1
        i = y1
        k = (x2 - x1) / (y2 - y1)
        while i <= y2:
            screen.set_at((int((i - y1) * k + x1), i), color)
            i += 1

pygame.init()
screen = pygame.display.set_mode((800, 600))

SZ = 100, 80

objects, nobj = [], 0

drag, start_pos, cur_pos = False, (0, 0), (0, 0)

timeout = 1500
pygame.time.set_timer(pygame.USEREVENT, timeout)

while True:
    e = pygame.event.wait()
    if e.type is pygame.QUIT:
        print("QUIT")
        break
    if e.type is pygame.MOUSEBUTTONDOWN:
        if e.button == 3:
            color = get_random_color()
            objects.append((nobj, color, pygame.Rect(e.pos, SZ)))
            nobj += 1
        if e.button == 1:
            drag = True
            start_pos, cur_pos = e.pos, e.pos
            line_color = get_random_color()
    if e.type is pygame.MOUSEBUTTONUP:
        if e.button == 1 and drag:
            drag = False
            objects.append((nobj, line_color, Line(*start_pos, *e.pos)))
            nobj += 1
    if e.type is pygame.MOUSEMOTION:
        if drag:
            cur_pos = e.pos
            if e.pos[0] <= 0 or e.pos[1] <= 0 or e.pos[0] >= screen.get_size()[0] or e.pos[1] >= screen.get_size()[1]:
                grag = False
    if e.type is pygame.ACTIVEEVENT:
        if e.gain == 0 and drag == True:
            drag = False
    else:
        for (i, color, obj) in reversed(objects):
            if type(obj) == pygame.Rect and hasattr(e, "pos") and obj.collidepoint(e.pos):
                print(f"{e} to {i}")
                break
        else:
            print(e)

    screen.fill(0)
    for i, color, obj in objects:
        if type(obj) == pygame.Rect:
            screen.fill(color, obj)
        if type(obj) == Line:
            draw_line(screen, color, obj.X1, obj.Y1, obj.X2, obj.Y2)

    if drag:
        draw_line(screen, line_color, *start_pos, *cur_pos)

    pygame.display.flip()
