# Kolbeinn Ingólfsson
# 12.2.2018
# Klasar fyrir Skil02

import pygame

clock = pygame.time.Clock()


class Player(pygame.sprite.Sprite):
    def __init__(self, window):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("images/player.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = 390
        self.rect.y = 390
        self.stig = 0
        self.window = window

    def move(self, dx, dy):
        if dx != 0:
            self.move_single_axis(dx, dy)
        if dy != 0:
            self.move_single_axis(dx, dy)

    def move_single_axis(self, dx, dy):
        if self.rect.x <= 846:
            self.rect.x += dx
        else:
            self.rect.x = 0

        if self.rect.x >= 0:
            self.rect.x += dx
        else:
            self.rect.x = 813

        if self.rect.y <= 399:
            self.rect.y += dy
        else:
            self.rect.y = 399

        if self.rect.y >= -45:
            self.rect.y += dy
        else:
            self.rect.y = 399


class Missile(pygame.sprite.Sprite):
    def __init__(self, missile_image):
        pygame.sprite.Sprite.__init__(self)
        self.image = missile_image
        self.rect = self.image.get_rect()


class Enemy(pygame.sprite.Sprite):
    def __init__(self, enemy_image):
        pygame.sprite.Sprite.__init__(self)
        self.image = enemy_image
        self.rect = self.image.get_rect()


class Cover(pygame.sprite.Sprite):
    def __init__(self, block_image):
        pygame.sprite.Sprite.__init__(self)
        self.image = block_image
        self.rect = self.image.get_rect()


