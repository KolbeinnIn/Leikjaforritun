# Kolbeinn Ingólfsson
# 12.2.2018
# Klasar fyrir Skil02

import pygame

clock = pygame.time.Clock()




class Player(object):
    def __init__(self, window):
        self.image = pygame.image.load("images/player.png").convert()
        self.rect = self.image.get_rect()
        self.rect.x = 380
        self.stig = 0
        self.window = window

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
        self.rect = self.image.get_rect(topleft=(self.pos, 380))        # rect-ið

    def move(self, window):
        self.move_single_axis(window)

    def move_single_axis(self, window):
        self.rect.y -= 10
        window.blit(self.image, self.rect)


class Enemy(pygame.sprite.Sprite):
    def __init__(self, row, column, window, IMAGES):
        pygame.sprite.Sprite.__init__(self)
        self.IMAGES = IMAGES
        self.window = window
        self.row = row
        self.column = column
        self.images = []
        self.load_images()
        self.index = 0
        self.image = self.images[self.index]
        self.rect = self.image.get_rect()
        self.direction = 1
        self.rightMoves = 15
        self.leftMoves = 30
        self.moveNumber = 0
        self.moveTime = 600
        self.firstTime = True
        self.movedY = False
        self.columns = [False] * 10
        self.aliveColumns = [True] * 10
        self.addRightMoves = False
        self.addLeftMoves = False
        self.numOfRightMoves = 0
        self.numOfLeftMoves = 0
        self.timer = clock.get_ticks()

    def update(self, keys, currentTime, killedRow, killedColumn, killedArray):
        self.check_column_deletion(killedRow, killedColumn, killedArray)
        if currentTime - self.timer > self.moveTime:
            self.movedY = False
            if self.moveNumber >= self.rightMoves and self.direction == 1:
                self.direction *= -1
                self.moveNumber = 0
                self.rect.y += 35
                self.movedY = True
                if self.addRightMoves:
                    self.rightMoves += self.numOfRightMoves
                if self.firstTime:
                    self.rightMoves = self.leftMoves
                    self.firstTime = False
                self.addRightMovesAfterDrop = False
            if self.moveNumber >= self.leftMoves and self.direction == -1:
                self.direction *= -1
                self.moveNumber = 0
                self.rect.y += 35
                self.movedY = True
                if self.addLeftMoves:
                    self.leftMoves += self.numOfLeftMoves
                self.addLeftMovesAfterDrop = False
            if self.moveNumber < self.rightMoves and self.direction == 1 and not self.movedY:
                self.rect.x += 10
                self.moveNumber += 1
            if self.moveNumber < self.leftMoves and self.direction == -1 and not self.movedY:
                self.rect.x -= 10
                self.moveNumber += 1

            self.index += 1
            if self.index >= len(self.images):
                self.index = 0
            self.image = self.images[self.index]

            self.timer += self.moveTime
        self.window.blit(self.image, self.rect)

    def check_column_deletion(self, killedRow, killedColumn, killedArray):
        if killedRow != -1 and killedColumn != -1:
            killedArray[killedRow][killedColumn] = 1
            for column in range(10):
                if all([killedArray[row][column] == 1 for row in range(5)]):
                    self.columns[column] = True

        for i in range(5):
            if all([self.columns[x] for x in range(i + 1)]) and self.aliveColumns[i]:
                self.leftMoves += 5
                self.aliveColumns[i] = False
                if self.direction == -1:
                    self.rightMoves += 5
                else:
                    self.addRightMoves = True
                    self.numOfRightMoves += 5

        for i in range(5):
            if all([self.columns[x] for x in range(9, 8 - i, -1)]) and self.aliveColumns[9 - i]:
                self.aliveColumns[9 - i] = False
                self.rightMoves += 5
                if self.direction == 1:
                    self.leftMoves += 5
                else:
                    self.addLeftMoves = True
                    self.numOfLeftMoves += 5

    def load_images(self):
        images = {0: ["1_1", "1_1"],
                  1: ["1_1", "1_1"],
                  2: ["1_1", "1_1"],
                  3: ["1_1", "1_1"],
                  4: ["1_1", "1_1"],
                  }

        img1, img2 = (self.IMAGES["enemy{}".format(img_num)] for img_num in images[self.row])
        self.images.append(pygame.transform.scale(img1, (40, 35)))
        self.images.append(pygame.transform.scale(img2, (40, 35)))

