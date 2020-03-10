import sys, pygame
pygame.init()

world_size = width, height = 10000, 9000
speed = [2, 2]
DX, DY = 0.1, 0.1
pos = [width / 2, height / 2]
screen_size = int(DX * width), int(DY * height)

black = 0, 0, 0

screen = pygame.display.set_mode(screen_size)

ball = pygame.image.load("intro_ball.gif")
ballrect = ball.get_rect()
w, h = ballrect.width / DX, ballrect.height / DY
print(w, h)
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    pos[0] += speed[0]
    pos[1] += speed[1]
    if pos[0] - w/2 < 0 or pos[0] + w/2 > width:
        speed[0] = -speed[0]
    if pos[1] - h/2 < 0 or pos[1] + h/2 > height:
        speed[1] = -speed[1]

    screen.fill(black)
    screen.blit(ball, (int(DX * (pos[0] - w/2)), int(DY * (pos[1] - h/2))))
    pygame.display.flip()
