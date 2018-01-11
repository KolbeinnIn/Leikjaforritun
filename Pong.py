# Kolbeinn Ingólfsson
# 10.1.2018
# Skilaverkefni 1


import pygame
import time
clock = pygame.time.Clock()
pygame.init()
x_position = 310
y_position = 230
x2_position = 310
y2_position = 230

x_velocity = 0
y_velocity = 0
x2_velocity = 0
y2_velocity = 0

xK_position = 0
yK_position = 0
xK_velocity = 0
yK_velocity = 0

window_size = window_width, window_height = 960, 720
window = pygame.display.set_mode(window_size, pygame.RESIZABLE)

pygame.display.set_caption('PUBG')

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

window.fill(BLACK)  # This command sets the background color
#x_coord = y_coord = 0
running = True
teljari = 30
teljari2 = 60
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                y_velocity = -10
            elif event.key == pygame.K_DOWN:
                y_velocity = 10
        #elif event.type == pygame.KEYUP:
            #y_velocity = 0

        # PLAYER 2
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                y2_velocity = -10
            elif event.key == pygame.K_s:
                y2_velocity = 10
        #elif event.type == pygame.KEYUP:
            #y2_velocity = 0

        xK_velocity = 2
        yK_velocity = 2

    xK_position += xK_velocity
    yK_position += yK_velocity

    x_position += x_velocity
    y_position += y_velocity

    x2_position += x2_velocity
    y2_position += y2_velocity

    window.fill(BLACK)
    pygame.draw.circle(window, WHITE, (xK_position, yK_position), 10)
    pygame.draw.rect(window, WHITE, pygame.Rect(50, y_position, 10, 50))
    pygame.draw.rect(window, WHITE, pygame.Rect(900, y2_position, 10, 50))
    pygame.draw.line(window, WHITE, (480, 0), (480, 1000))


    if y_position > 720 or y_position < 0:
        y_velocity = 0
    if y2_position > 720 or y2_position < 0:
        y2_velocity = 0

    if yK_position > 720 or yK_position < 0:
        yK_velocity *= -1
    if xK_position > 960 or xK_position < 0:
        xK_velocity *= -1


    pygame.display.update()
    clock.tick(60)

pygame.quit()
