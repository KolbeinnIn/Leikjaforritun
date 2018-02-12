# Kolbeinn Ingólfsson
# 12.2.2018
# Skilaverkefni 2 - Maze leikur

import klasar
import pygame
from random import *


pygame.init()

window_size = window_width, window_height = 960, 720
window = pygame.display.set_mode(window_size)
pygame.display.set_caption('Maze')

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
GREY = (70, 80, 90)
YELLOW = (255, 255, 0)
my_font = pygame.font.SysFont("", 30)

clock = pygame.time.Clock()
player = klasar.Player()

"""
level = [
    "WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
    "W                                                          W",
    "W WWWWWWW                                                  W",
    "W                                                          W",
    "W                                                          W",
    "W                                                          W",
    "W                                                          W",
    "W                                                          W",
    "W                                                          W",
    "W                                                          W",
    "W                                                          W",
    "W                                                          W",
    "W                                                          W",
    "W                                                          W",
    "W                                                          W",
    "W                                                          W",
    "W                                                          W",
    "W                                                          W",
    "W                                                          W",
    "W                                                          W",
    "W                                                          W",
    "W                                                          W",
    "W                                                          W",
    "W                                                          W",
    "W                                                          W",
    "W                                                          W",
    "W                                                          W",
    "W                                                          W",
    "W                                                          W",
    "W                                                          W",
    "W                                                          W",
    "W                                                          W",
    "W                                                          W",
    "W                                                          W",
    "W                                                          W",
    "W                                                          W",
    "W                                                          W",
    "W                                                          W",
    "W                                                          W",
    "W                                                          W",
    "W                                                          W",
    "W                                                          W",
    "W                                                          W",
    "W                                                          W",
    "WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWEW",
]
"""
#level = [random("W") x for x in]
level = []
top = "WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW"
side = "W                                                          W"
strengur = ""
for lina1 in range(45):
    for i in range(60):
        if lina1 == 0 or lina1 == 44:
            if i == 0 or i == 59:
                strengur += "W"
            else:
                strengur += " "

    level.append(strengur)


level[0] = top
level[-1] = top


E = ""
for e in range(len(level[-2])):
    if e == 59:
        E += "E"
    if e == 0:
        E += "W"
    else:
        E += " "


level[-2] = E

x = y = 0
for lina in level:
    for stafur in lina:
        if stafur == "W":
            klasar.Veggur((x, y))
        if stafur == "E":
            end_rect = pygame.Rect(x, y, 16, 16)
        x += 16
    y += 16
    x = 0

running = True
while running:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False
    # Move the player if an arrow key is pressed
    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT]:
        player.move(-2, 0)
    if key[pygame.K_RIGHT]:
        player.move(2, 0)
    if key[pygame.K_UP]:
        player.move(0, -2)
    if key[pygame.K_DOWN]:
        player.move(0, 2)

    # Just added this to make it slightly fun ;)
    if player.rect.colliderect(end_rect):
        raise SystemExit("You win!")

    # Draw the scene
    window.fill((0, 0, 0))
    for veggur in klasar.veggir:
        pygame.draw.rect(window, (255, 255, 255), veggur.rect)
    pygame.draw.rect(window, (255, 0, 0), end_rect)
    pygame.draw.rect(window, (255, 200, 0), player.rect)
    pygame.display.flip()


pygame.quit()