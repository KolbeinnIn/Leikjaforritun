#Kolbeinn Ingólfsson
#Skilaverkefni 3 - Leikjaforritun -

import pygame
from random import *
import os
import klasar

os.environ["SDL_VIDEO_CENTERED"] = "300"
pygame.init()

window_size = window_width, window_height = 640, 480
window = pygame.display.set_mode(window_size)
pygame.display.set_caption('Maze')

player = klasar.Player()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
lBlue = (0, 120, 255)
GREY = (70, 80, 90)
YELLOW = (255, 255, 0)
my_font = pygame.font.SysFont("", 30)
clock = pygame.time.Clock()


running = True
while running:
    window.fill(BLACK)
    stig = player.stig
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False

    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT] or key[pygame.K_a]:
        player.move(-2, 0)
    if key[pygame.K_RIGHT] or key[pygame.K_d]:
        player.move(2, 0)

    pygame.draw.rect(window, WHITE, player.rect)
    pygame.display.flip()
pygame.quit()
