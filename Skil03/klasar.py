# Kolbeinn Ingólfsson
# 12.2.2018
# Klasar fyrir Skil02

import pygame


class Player(object):
    def __init__(self):
        self.rect = pygame.Rect(624, 690, 16, 16)
        self.stig = 0

    def move(self, dx):
        if dx != 0:
            self.move_single_axis(dx)

    def move_single_axis(self, dx):
        if self.rect.x <= 1262:
            self.rect.x += dx
        else:
            self.rect.x = 1262

        if self.rect.x >= 0:
            self.rect.x += dx
        else:
            self.rect.x = 0

    def position(self):
        return self.rect.x


class Missile(object):
    def __init__(self, pos):
        self.pos = pos
        self.image = pygame.image.load("images/missile.png").convert()  # surface
        self.rect = self.image.get_rect(topleft=(self.pos, 690))             # rect-ið

    def move(self, window):
        self.move_single_axis(window)

    def move_single_axis(self, window):
        self.rect.y -= 3
        window.blit(self.image, self.rect)
        # print(self.rect.y)



