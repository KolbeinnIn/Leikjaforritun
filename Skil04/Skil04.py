# Kolbeinn Ingólfsson
# 25.4.2018
# Skilaverkefni 4 - 2 skriðdrekar.

import pygame


pygame.init()

window_size = window_width, window_height = 960, 720
window = pygame.display.set_mode(window_size)

pygame.display.set_caption('Skil04')

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
GREY = (70, 80, 90)
YELLOW = (255, 255, 0)

my_font = pygame.font.SysFont("", 60)
clock = pygame.time.Clock()

running = True
while running:
    clock.tick(10)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False


    pygame.display.update()
pygame.quit()

