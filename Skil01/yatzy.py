# Kolbeinn Ingólfsson
# 15.1.2018
# Skilaverkefni 1 - yatzy

import pygame
from random import *

pygame.init()

window_size = window_width, window_height = 960, 720
window = pygame.display.set_mode(window_size)

pygame.display.set_caption('Yatzy')
asd1 = pygame.image.load("sd1.png")
asd2 = pygame.image.load("sd2.png")
asd3 = pygame.image.load("sd3.png")
asd4 = pygame.image.load("sd4.png")
asd5 = pygame.image.load("sd5.png")
asd6 = pygame.image.load("sd6.png")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
GREY = (70, 80, 90)
YELLOW = (255, 255, 0)

my_font = pygame.font.SysFont("", 30)
ten = [asd1, asd2, asd3, asd4, asd5, asd6]
def a(listi):
    return listi[randint(0, 5)]

window.fill(BLACK)
window.blit(a(ten), (370, 200))
window.blit(a(ten), (495, 200))
window.blit(a(ten), (300, 330))
window.blit(a(ten), (430, 330))
window.blit(a(ten), (560, 330))

pygame.draw.rect(window, WHITE, pygame.Rect(427, 470, 100, 60))
label = my_font.render('X', 1, YELLOW)

pygame.display.update()

#427, 470
#527, 530

my_font = pygame.font.SysFont("", 30)
# pygame.draw.line(window, WHITE, (480, 50), (480, 1000)) helmingarlína skjásins

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            pygame.display.update()

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if 527 > event.pos[0] > 427:
                if 530 > event.pos[1] > 470:
                    pygame.display.update()
            #pygame.draw.circle(window, GREEN, event.pos, 20, 0)


    window.blit(a(ten), (370, 200))
    window.blit(a(ten), (495, 200))
    window.blit(a(ten), (300, 330))
    window.blit(a(ten), (430, 330))
    window.blit(a(ten), (560, 330))

pygame.quit()
