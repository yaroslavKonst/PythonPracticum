import pygame
from random import randrange
pygame.init()
screen = pygame.display.set_mode((800, 600))

SZ = 100, 80

windows, nwin = [], 0

timeout = 1000
pygame.time.set_timer(pygame.USEREVENT, timeout)

while True:
    e = pygame.event.wait()
    if e.type is pygame.QUIT:
        print("QUIT")
        break
    if e.type is pygame.MOUSEBUTTONDOWN:
        if e.button == 3:
            color = pygame.Color(randrange(100,256), randrange(100,256),randrange(100,256))
            windows.append((nwin, color, pygame.Rect(e.pos, SZ)))
            nwin += 1
    else:
        for (i, color, rect) in reversed(windows):
            if hasattr(e, "pos") and rect.collidepoint(e.pos):
                print(f"{e} to {i}")
                break
        else:
            print(e)

    screen.fill(0)
    for i, color, rect in windows:
        screen.fill(color, rect)

    pygame.display.flip()
