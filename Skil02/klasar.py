# Kolbeinn Ingólfsson
# 12.2.2018
# Klasar fyrir Skil02

import pygame
from random import *

sprengjur = []
varnir = []
veggir = []


class Player(object):
    def __init__(self):
        self.rect = pygame.Rect(16, 16, 16, 16)
        self.fjVarna = 0
        self.ovirkarSprengjur = 0

    def move(self, dx, dy):

        # Move each axis separately. Note that this checks for collisions both times.
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

        # Move the rect
        self.rect.x += dx
        self.rect.y += dy

        # If you collide with a wall, move out based on velocity
        for veggur in veggir:
            if self.rect.colliderect(veggur.rect):
                if dx > 0:  # Moving right; Hit the left side of the wall
                    self.rect.right = veggur.rect.left
                if dx < 0:  # Moving left; Hit the right side of the wall
                    self.rect.left = veggur.rect.right
                if dy > 0:  # Moving down; Hit the top side of the wall
                    self.rect.bottom = veggur.rect.top
                if dy < 0:  # Moving up; Hit the bottom side of the wall
                    self.rect.top = veggur.rect.bottom

        for sprengja in sprengjur:
            if self.rect.colliderect(sprengja.rect):
                if self.fjVarna >= 1:
                    print(self.fjVarna)
                    if dx > 0:
                        self.rect.right = sprengja.rect.left
                        sprengjur.remove(sprengja)
                        self.ovirkarSprengjur -= 1
                        self.fjVarna -= 1
                    if dx < 0:
                        self.rect.left = sprengja.rect.right
                        sprengjur.remove(sprengja)
                        self.ovirkarSprengjur += 1
                        self.fjVarna -= 1
                    if dy > 0:
                        self.rect.bottom = sprengja.rect.top
                        sprengjur.remove(sprengja)
                        self.ovirkarSprengjur += 1
                        self.fjVarna -= 1
                    if dy < 0:
                        self.rect.top = sprengja.rect.bottom
                        sprengjur.remove(sprengja)
                        self.ovirkarSprengjur += 1
                        self.fjVarna -= 1
                else:
                    print(sprengja)
                    raise SystemExit("You hit something")

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
                if dx > 0:  # Moving right; Hit the left side of the wall
                    self.fjVarna += 1
                    varnir.remove(vorn)
                if dx < 0:  # Moving left; Hit the right side of the wall
                    self.fjVarna += 1
                    varnir.remove(vorn)
                if dy > 0:  # Moving down; Hit the top side of the wall
                    self.fjVarna += 1
                    varnir.remove(vorn)
                if dy < 0:  # Moving up; Hit the bottom side of the wall
                    self.fjVarna += 1
                    varnir.remove(vorn)


def radius():
    return randint(6, 8)


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
