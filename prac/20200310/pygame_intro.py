import sys, pygame
pygame.init()

world_size = width, height = 10000, 9000
speed = [2, 2]
DX, DY = 0.1, 0.1
position = [width / 2, height / 2]
screen_size = int(DX * width), int(DY * height)

black = 0, 0, 0

screen = pygame.display.set_mode(screen_size)

ball = pygame.image.load("intro_ball.gif")
ballrect = ball.get_rect()
w, h = ballrect.width / DX, ballrect.height / DY

pygame.time.set_timer(pygame.USEREVENT, 10)

drag = False

while 1:
    event = pygame.event.wait()
    if event.type == pygame.QUIT: sys.exit()

    if event.type == pygame.MOUSEBUTTONDOWN:
        if position[0] - w/2 < event.pos[0]/DX < position[0] + w/2 and position[1] - h/2 < event.pos[1]/DY < position[1] + h/2:
            drag = True
            drg_x, drg_y = event.pos[0] / DX - position[0], event.pos[1] / DY - position[1]

    if event.type == pygame.MOUSEBUTTONUP:
        drag = False

    if event.type == pygame.MOUSEMOTION:
        if drag:
            position[0] = event.pos[0] / DX - drg_x
            position[1] = event.pos[1] / DY - drg_y

    if event.type == pygame.USEREVENT:
        if not drag:
            position[0] += speed[0]
            position[1] += speed[1]
        if position[0] - w/2 < 0 or position[0] + w/2 > width:
            speed[0] = -speed[0]
        if position[1] - h/2 < 0 or position[1] + h/2 > height:
            speed[1] = -speed[1]

        screen.fill(black)
        screen.blit(ball, (int(DX * (position[0] - w/2)), int(DY * (position[1] - h/2))))
        pygame.display.flip()
