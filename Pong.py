# Kolbeinn Ingólfsson
# 10.1.2018
# Skilaverkefni 1


import pygame
import time

clock = pygame.time.Clock()
pygame.init()
x_position = 0
y_position = 0
x2_position = 0
y2_position = 0

x_velocity = 0
y_velocity = 0
x2_velocity = 0
y2_velocity = 0

xK_position = 480
yK_position = 480
xK_velocity = -1
yK_velocity = -1

window_size = window_width, window_height = 960, 720
window = pygame.display.set_mode(window_size)

pygame.display.set_caption('PUBG')

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False

        # PLAYER 1
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                y_velocity = -8
            elif event.key == pygame.K_s:
                y_velocity = 8
        elif event.type == pygame.KEYUP:
            y_velocity = 0

        # PLAYER 2
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                y2_velocity = -8
            elif event.key == pygame.K_DOWN:
                y2_velocity = 8

    # Bolti
    xK_position += xK_velocity
    yK_position += yK_velocity

    # Player 1 (Vinstri)
    x_position += x_velocity
    y_position += y_velocity

    # Player 2 (Hægri)
    x2_position += x2_velocity
    y2_position += y2_velocity

    #

    window.fill(BLACK)
    pygame.draw.circle(window, WHITE, (xK_position, yK_position), 10)
    pygame.draw.rect(window, WHITE, pygame.Rect(50, y_position, 10, 50))
    pygame.draw.rect(window, WHITE, pygame.Rect(900, y2_position, 10, 50))
    pygame.draw.line(window, WHITE, (480, 0), (480, 1000))

    # hér fyrir neðan eru bara línur sem sýna hvar borderarnir eru
    # pygame.draw.line(window, RED, (959, 0), (959, 1000))
    # pygame.draw.line(window, RED, (1, 0), (1, 1000))
    # pygame.draw.line(window, RED, (0, 719), (1000, 719))
    # pygame.draw.line(window, RED, (0, 1), (1000, 1))

    if y_position > 660 or y_position < 0:
        y_velocity = 0

    if y2_position > 660 or y2_position < 0:
        y2_velocity = 0

    if yK_position > 710 or yK_position < 10:
        yK_velocity *= -1
    if xK_position > 950 or xK_position < 0:
        xK_velocity *= -1

    #

    # Bounce off pads
    print("Bolti X:", xK_position)
    print("Bolti Y:", yK_position)
    print("\nLeft bo: ", y_position)
    print("left+50: ", (y_position+50))
    pygame.draw.line(window, RED, (x_position + 60, y_position), (x_position + 60, y_position + 50))
    pygame.draw.circle(window, RED, (0, 0), 20)
    if xK_position <= 60:
        if yK_position > y_position and yK_position < (y_position + 100):
            xK_velocity *= -1
        # yK_velocity += 1
        # xK_velocity += 1

    #time.sleep(0.1)
    pygame.display.update()
    clock.tick(60)

pygame.quit()
