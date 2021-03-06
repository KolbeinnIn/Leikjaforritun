# Kolbeinn Ingólfsson
# 12.2.2018
# Klasar fyrir Skil02

import pygame
from random import *

sprengjur = []
varnir = []
veggir = []
endir = []


def radius():
    return randint(5, 8)


class Player(object):
    def __init__(self):
        self.rect = pygame.Rect(16, 16, 16, 16)
        self.fjVarna = 0
        self.ovirkarSprengjur = 0
        self.stig = 0

    def move(self, dx, dy):
        if dx != 0:
            self.move_single_axis(dx, 0)
        if dy != 0:
            self.move_single_axis(0, dy)

    def anti(self):
        return self.fjVarna

    def draw(self):
        if self.fjVarna > 0:
            spilari = (255, 200, 0)
        else:
            spilari = (255, 128, 0)
        return spilari

    def move_single_axis(self, dx, dy):
        self.rect.x += dx
        self.rect.y += dy

        for veggur in veggir:
            if self.rect.colliderect(veggur.rect):
                if dx > 0:
                    self.rect.right = veggur.rect.left
                if dx < 0:
                    self.rect.left = veggur.rect.right
                if dy > 0:
                    self.rect.bottom = veggur.rect.top
                if dy < 0:
                    self.rect.top = veggur.rect.bottom

        for e in range(0, len(endir), 2):
            if endir[e+1] == 0:
                if self.rect.colliderect(endir[e].rect):
                    if dx > 0:
                        self.rect.right = endir[e].rect.left
                    if dx < 0:
                        self.rect.left = endir[e].rect.right
                    if dy > 0:
                        self.rect.bottom = endir[e].rect.top
                    if dy < 0:
                        self.rect.top = endir[e].rect.bottom


        for sprengja in sprengjur:
            if self.rect.colliderect(sprengja.rect):
                if self.fjVarna >= 1:
                    if dx > 0:
                        self.rect.right = sprengja.rect.left
                        sprengjur.remove(sprengja)
                        self.ovirkarSprengjur += 1
                        self.fjVarna -= 1
                        self.stig += 5
                    if dx < 0:
                        self.rect.left = sprengja.rect.right
                        sprengjur.remove(sprengja)
                        self.ovirkarSprengjur += 1
                        self.fjVarna -= 1
                        self.stig += 5
                    if dy > 0:
                        self.rect.bottom = sprengja.rect.top
                        sprengjur.remove(sprengja)
                        self.ovirkarSprengjur += 1
                        self.fjVarna -= 1
                        self.stig += 5
                    if dy < 0:
                        self.rect.top = sprengja.rect.bottom
                        sprengjur.remove(sprengja)
                        self.ovirkarSprengjur += 1
                        self.fjVarna -= 1
                        self.stig += 5
                else:
                    raise SystemExit("BOOM!")


                if dx > 0:
                    self.rect.right = sprengja.rect.left
                if dx < 0:
                    self.rect.left = sprengja.rect.right
                if dy > 0:
                    self.rect.bottom = sprengja.rect.top
                if dy < 0:
                    self.rect.top = sprengja.rect.bottom

        for vorn in varnir:
            if self.rect.colliderect(vorn.rect):
                if dx > 0:
                    self.fjVarna += 1
                    varnir.remove(vorn)
                if dx < 0:
                    self.fjVarna += 1
                    varnir.remove(vorn)
                if dy > 0:
                    self.fjVarna += 1
                    varnir.remove(vorn)
                if dy < 0:
                    self.fjVarna += 1
                    varnir.remove(vorn)


class Sprengja(object):

    def __init__(self, pos):
        sprengjur.append(self)
        self.rect = pygame.Rect(pos[0], pos[1], 16, 16)


class SprengjuVarnir(object):

    def __init__(self, pos):
        varnir.append(self)
        self.rect = pygame.Rect(pos[0], pos[1], 16, 16)


class Veggur(object):
    def __init__(self, pos):
        veggir.append(self)
        self.rect = pygame.Rect(pos[0], pos[1], 16, 16)


class Endir(object):
    def __init__(self, pos, rg):
        if rg == 1:
            global endir
            endir = []
        endir.append(self)
        endir.append(rg)
        self.rect = pygame.Rect(pos[0], pos[1], 16, 16)

