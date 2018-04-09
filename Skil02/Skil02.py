# Kolbeinn Ingólfsson
# 12.2.2018
# Skilaverkefni 2 - Maze leikur

import klasar
import pygame
from random import *
import os

os.environ["SDL_VIDEO_CENTERED"] = "300"
pygame.init()

window_size = window_width, window_height = 960, 720
window = pygame.display.set_mode(window_size)
pygame.display.set_caption('Maze')

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
player = klasar.Player()
sprengjur = klasar.sprengjur
varnir = klasar.varnir
teljari = 0
count = 0

level = [
    "WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
    "W             WW W                   W   W    W      W     W",
    "W W WWWWWWWWWW W W WWWWWWWWWWWWWWWWW W W WWWW W WWW  W     W",
    "W W        W W W W                 W   W        W W  W     W",
    "W WWW WWWW W W W WWWWWWWWWW WWWWWWWWWWWW WWWWWWWW W  W     W",
    "W   W W  W W W W                       W W    W      W     W",
    "W W      W S      WWWWWWWWWWWWWWWWWWWWWW WWWW WWWW   W     W",
    "W WWWWWWWWWWWWWWW W                                        W",
    "W              W  WWW                                      W",
    "WVWWWWWWWWWWWW W  V                                        W",
    "W            W W  WWWWWW                                   W",
    "W   S        W W                                           W",
    "W            W W                                           W",
    "WV           W W                                           W",
    "W     S        S                                           W",
    "W                                                          W",
    "W                                                          W",
    "W          V                                               W",
    "W                S                                         W",
    "W                       W                                  W",
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
level = [
    "WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
    "W WA      W                                   WW           W",
    "W WWW W W WWWWWWWWWWW WWWWWWWWWWWWWWWWWWWWWWW WW WWWWWWWWW W",
    "WA    W W           W W                          W         W",
    "WBWWWWW WWWWWW WWWWWW W WWWWWWWWWWWWWWWWWWWWWWWWWW WWWWW WWW",
    "W W       W           W W                        W   W   W W",
    "W WWWWWWWWW WWWWWW WWWW W WWWWWWWWWWWWWWWWWWWWWWWWWWWW W W W",
    "W W       W W    W W  W   W        W        W   W   W  W   W",
    "W W WWWWWWW W WW W W WWWWWW WWWWWWWW WWWWWW W W W W W WWWW W",
    "W W         W WW W W W      W        W        W   W W    W W",
    "W WWW WWWWWWW W  W W W WWW  W WWWW WWW WWWWWWWWWWWW WWWW W W",
    "W W   W       WWWW W W W WWWW WW   W    W W   W   W    W W W",
    "W W WWW WWWWWWW    W W W       W WWW WWWW W W W W W WWWW W W",
    "W W W   W       WWWW W W WWWWW W W   W      W W W   W    W W",
    "W W W WWW WWWWWWW      W     W W WWWWWWWWWWWW W WWWWW WWWW W",
    "W W W  W  W       WWWWWWWWWW W W              W     W    W W",
    "W W WW W WW WWWWWWW          W W WWWWWWWWWWWWWWWWWWWWWWW WWW",
    "W        WW W     W WWWWWWWWWW W W   W   W   W   W   W   W W",
    "W WWWWW WW  W WWWWW W          W   W   W   W   W   W   W   W",
    "W W     WW WW W   W W WWWW WWWWWWWWWWWWWWW WWWWWWWWWWWWWWWWW",
    "W W WWWWW  W  W W W W W  W W             W W               W",
    "W W W     WW WW WWWWW WW W WWWWWWWWWWWWW W W WWWWWWWWWWWW  W",
    "W   W WWWWW  W           W               W   W          W  W",
    "W W W WW     W WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW W  W",
    "W W      WWW W                              W         W W  W",
    "W WWWWWWWW W WWWWWWWW                       W WWWWWWWWW W  W",
    "W W          W                              W W       W W  W",
    "W     WWWWWWWW                              W W WWWWW W W  W",
    "W W                                           W W W W W W  W",
    "W   W                                       WWW W W W      W",
    "W W W                               B       WWWWWWWWWWWWWWWW",
    "W W W                                                      W",
    "W W W                                                      W",
    "W W W              X                                       W",
    "W W W                                                      W",
    "W W W                                                      W",
    "W W WWWWW               B                                  W",
    "W W     W                                                  W",
    "W WWWWW W                                                  W",
    "W W   W W                                                  W",
    "W W W W W                                                  W",
    "W W W W W                                                  W",
    "W WWW W WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWXW",
    "W     W                                                  X E",
    "WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",

]
"""

x = y = 0
for lina in level:
    for stafur in lina:
        if stafur == "W":
            klasar.Veggur((x, y))
        elif stafur == "E":
            klasar.Endir((x, y), 0)
        elif stafur == "S":
            klasar.Sprengja((x, y))
        elif stafur == "V":
            klasar.SprengjuVarnir((x, y))
        x += 16
    y += 16
    x = 0


radius = []
for a in range(len(sprengjur)):
    radius.append(klasar.radius())


running = True
while running:
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
    if key[pygame.K_UP] or key[pygame.K_w]:
        player.move(0, -2)
    if key[pygame.K_DOWN] or key[pygame.K_s]:
        player.move(0, 2)



    window.fill(BLACK)
    for veggur in klasar.veggir:
        pygame.draw.rect(window, WHITE, veggur.rect)

    for vorn in varnir:
        pygame.draw.rect(window, (50, 150, 120), vorn.rect)

    for sprengja in range(len(sprengjur)):
        pygame.draw.circle(window, lBlue, (sprengjur[sprengja].rect[0] + radius[sprengja],
                                           sprengjur[sprengja].rect[1] + radius[sprengja]), radius[sprengja])


    if stig >= 15:
        x = y = 0
        for lina in level:
            for stafur in lina:
                if stafur == "E":
                    klasar.Endir((x, y), 1)
                x += 16
            y += 16
            x = 0
        pygame.draw.rect(window, GREEN, klasar.endir[0])
        if player.rect.colliderect(klasar.endir[0]):
            raise SystemExit("Til hamingju!")

    else:
        pygame.draw.rect(window, RED, klasar.endir[0])

    if player.fjVarna >= 1:
        spilari = YELLOW
    else:
        spilari = (255, 165, 0)

    pygame.draw.rect(window, spilari, player.rect)
    pygame.display.flip()
pygame.quit()
