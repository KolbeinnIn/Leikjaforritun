#Kolbeinn Ingólfsson
#12.2.2018
#Klasar fyrir Skil02

import pygame

veggir = []

class Player(object):
    def __init__(self):
        self.rect = pygame.Rect(16, 16, 16, 16)

    def move(self, dx, dy):

        # Move each axis separately. Note that this checks for collisions both times.
        if dx != 0:
            self.move_single_axis(dx, 0)
        if dy != 0:
            self.move_single_axis(0, dy)

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



class Veggur(object):
    def __init__(self, pos):
        veggir.append(self)
        self.rect = pygame.Rect(pos[0], pos[1], 16, 16)