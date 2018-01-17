# Kolbeinn Ingólfsson
# 10.1.2018
# Skilaverkefni 1 - Pong


import pygame
import time
from random import *
while True:
    nafn = input("Sláðu inn MAX 3 stafi: ")
    if len(nafn) > 3 or len(nafn) < 1:
        print("Rangur innsláttur")
    else:
        break
while True:
    nafn2 = input("Sláðu inn MAX 3 stafi: ")
    if len(nafn) > 3 or len(nafn) < 1:
        print("Rangur innsláttur")
    else:
        break
clock = pygame.time.Clock()
pygame.init()
x_position = 0
y_position = 385
x2_position = 0
y2_position = 385

x_velocity = 0
y_velocity = 0
x2_velocity = 0
y2_velocity = 0

xK_position = 480
yK_position = 400
listi = [3, -3]
xK_velocity = listi[randint(0, 1)]
yK_velocity = listi[randint(0, 1)]

window_size = window_width, window_height = 960, 770
window = pygame.display.set_mode(window_size)
my_font = pygame.font.SysFont("", 50)
pygame.display.set_caption('PUBG')

p1 = 0
p2 = 0

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
start_ticks = pygame.time.get_ticks()
counter, text = 5, '5'.rjust(3)
pygame.time.set_timer(pygame.USEREVENT, 1000)
font = pygame.font.SysFont('Consolas', 30)

running = True
while running:
    if counter != -2:
        for e in pygame.event.get():
            if e.type == pygame.USEREVENT:
                counter -= 1
                if counter > 0:
                    text = str(counter).rjust(3)
                else:
                    text = 'START!'
            if e.type == pygame.QUIT:
                break
        else:
            window.fill((255, 255, 255))
            window.blit(font.render(text, True, (0, 0, 0)), (450, 370))
            pygame.display.flip()
            clock.tick(60)
            continue

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
            if event.key == pygame.K_w:
                y_velocity = 0
            elif event.key == pygame.K_s:
                y_velocity = 0

        # PLAYER 2
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                y2_velocity = -8
            elif event.key == pygame.K_DOWN:
                y2_velocity = 8
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                y2_velocity = 0
            elif event.key == pygame.K_DOWN:
                y2_velocity = 0

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
    pygame.draw.line(window, WHITE, (480, 50), (480, 960))
    pygame.draw.line(window, WHITE, (0, 50), (1000, 50))
    pygame.draw.line(window, WHITE, (0, 49), (1000, 49))

    # the text is rendered and put in the variable label
    label = my_font.render('%d - %d' % (p1, p2), 1, WHITE)
    label2 = my_font.render(nafn, 1, WHITE)
    label3 = my_font.render(nafn2, 1, WHITE)
    window.blit(label2, (10, 15))
    window.blit(label3, (880, 15))
    # and then drawn on the screen and positioned within the red rectangle
    if p1 > 9:
        window.blit(label, (430, 15))
    else:
        window.blit(label, (445, 15))

    # hér fyrir neðan eru bara línur sem sýna hvar borderarnir eru
    # pygame.draw.line(window, RED, (959, 0), (959, 1000))
    # pygame.draw.line(window, RED, (1, 0), (1, 1000))
    # pygame.draw.line(window, RED, (0, 719), (1000, 719))
    # pygame.draw.line(window, RED, (0, 1), (1000, 1))

    if y_position > 720 or y_position < 50:
        y_velocity = 0

    if y2_position > 720 or y2_position < 50:
        y2_velocity = 0

    if yK_position > 760 or yK_position < 60:
        yK_velocity *= -1

    if xK_position > 950:
        p1 += 1
        xK_position = 480
        yK_position = 360
        yK_velocity = listi[randint(0, 1)]
        xK_velocity = listi[randint(0, 1)]

    if xK_position < 10:
        p2 += 1
        xK_position = 480
        yK_position = 360
        yK_velocity = listi[randint(0, 1)]
        xK_velocity = listi[randint(0, 1)]


    # Bounce off pads
    if 52 < xK_position <= 60:
        if yK_position > y_position - 10 and yK_position < (y_position + 60):
            # print("\nBolti X:", xK_position)
            # print("Bolti Y:", yK_position)
            # print("\nLeft bo: ", y_position)
            # print("left+50: ", (y_position + 50))
            xK_velocity *= -1
            if xK_velocity > 0:
                xK_velocity += 1
            else:
                xK_velocity -= 1
            if yK_velocity > 0:
                yK_velocity += 1
            else:
                yK_velocity -= 1

    if 892 < xK_position <= 900:
        if yK_position > y2_position - 10 and yK_position < (y2_position + 60):
            # print("\nBolti X:", xK_position)
            # print("Bolti Y:", yK_position)
            # print("\nLeft bo: ", y_position)
            # print("left+50: ", (y_position + 50))

            xK_velocity *= -1
            if xK_velocity > 0:
                xK_velocity += 1
            else:
                xK_velocity -= 1
            if yK_velocity > 0:
                yK_velocity += 1
            else:
                yK_velocity -= 1

    pygame.display.update()
    clock.tick(60)


pygame.quit()
