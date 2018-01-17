# Kolbeinn Ingólfsson
# 15.1.2018
# Skilaverkefni 1 - yatzy

import pygame
from random import *

pygame.init()


class Box:
    def __init__(self, box_image, x_pos=0, y_pos=0):
        self.image = pygame.image.load(box_image).convert()
        self.rect = self.image.get_rect()
        self.rect.x = x_pos
        self.rect.y = y_pos


def a(listi):
    return listi[randint(0, 5)]


ten = ["sd1.png", "sd2.png", "sd3.png", "sd4.png", "sd5.png", "sd6.png"]

window_size = window_width, window_height = 960, 720
window = pygame.display.set_mode(window_size)

pygame.display.set_caption('Yatzy')
# takki = pygame.image.load("takki_box.png")


listi = [(370, 200), (495, 200), (300, 330), (430, 330), (560, 330)]

boxes = []
boxes.append(Box("takki_box.png", 424, 470))
for x in range(len(listi)):
    boxes.append(Box(a(ten), listi[x][0], listi[x][1]))


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
GREY = (70, 80, 90)
YELLOW = (255, 255, 0)

my_font = pygame.font.SysFont("", 30)

window.fill(BLACK)


for x in range(6):
    window.blit(boxes[x].image, (boxes[x].rect.x, boxes[x].rect.y))

pygame.display.update()

# pygame.draw.line(window, WHITE, (480, 50), (480, 1000)) helmingarlína skjásins

teningur = 0

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            for box in boxes:
                if box.rect.collidepoint(event.pos):
                    print(teningur)
                    if box.rect.collidepoint(event.pos) == boxes[0].rect.collidepoint(event.pos):
                        if teningur == 0:
                            print("asd")
                            for x in range(len(boxes)-1):
                                boxes[x] = (Box(a(ten), listi[x][0], listi[x][1]))
                        else:
                            print("asd1")
                            for x in range(1, 6):
                                if teningur == x:
                                    boxes[x] = (Box(a(ten), listi[teningur-1][0], listi[teningur-1][1]))

                        for x in range(1, 6):
                            window.blit(boxes[x].image, (boxes[x].rect.x, boxes[x].rect.y))
                        pygame.display.update()

                    for x in range(1, 6):
                        if box.rect.collidepoint(event.pos) == boxes[x].rect.collidepoint(event.pos):
                            teningur = x



pygame.quit()
