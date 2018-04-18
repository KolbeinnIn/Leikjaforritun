#Kolbeinn Ingólfsson
#Skilaverkefni 3 - Leikjaforritun -

import pygame
from random import *
import os
import klasar
import copy

os.environ["SDL_VIDEO_CENTERED"] = "300"
pygame.init()

bakgrunnur = pygame.image.load("images/spaceman.png")

window_size = window_width, window_height = 846, 445
window = pygame.display.set_mode(window_size)
pygame.display.set_caption('Maze')

player = klasar.Player(window)

IMG_NAMES = ["enemy1_1" for x in range(8)]
IMAGES = {name: pygame.image.load("images/%s.png" % str(name)).convert_alpha()
          for name in IMG_NAMES}


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
pos = []

flag = False
teljari = 0
running = True
copied = False
while running:
    pos = player.position()
    window.fill(BLACK)
    window.blit(bakgrunnur, [0, 0])
    stig = player.stig
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False

    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT] or key[pygame.K_a]:
        player.move(-2)
    if key[pygame.K_RIGHT] or key[pygame.K_d]:
        player.move(2)

    if key[pygame.K_SPACE] and teljari == 0:
        global skot
        skot = klasar.Missile(pos+22)
        flag = True

    if flag and teljari < 38:    #Að nota teljara til þess að deleta skotinu er reliable vegna clock.tick(60)
        skot.move(window)        #þá er það eins sama hversu öflug tölvan sem runnar kóðan er
        teljari += 1
    if teljari >= 38:
        teljari = 0
        flag = False
    a = pygame.image.load("images/player.png").convert_alpha()
    b = pygame.image.load("images/enemy1_1.png").convert_alpha()
    window.blit(a, (player.position(), 380))
    window.blit(b, (300, 50))

    pygame.display.flip()
pygame.quit()
