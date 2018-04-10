# Kolbeinn Ingólfsson
# 12.2.2018
# Klasar fyrir Skil02

import pygame
from random import *

sprengjur = []
varnir = []
veggir = []
endir = []


class Player(object):
    def __init__(self):
        self.rect = pygame.Rect(304, 450, 16, 16)
        self.stig = 0

    def move(self, dx, dy):
        if dx != 0:
            self.move_single_axis(dx)
            print(dx)

    def move_single_axis(self, dx):
        if self.rect.x <= 622:
            self.rect.x += dx
        else:
            self.rect.x = 622

        if self.rect.x >= 0:
            self.rect.x += dx
        else:
            self.rect.x = 0
        print(self.rect.x)


