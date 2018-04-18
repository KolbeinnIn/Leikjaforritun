#Kolbeinn Ingólfsson
#Skilaverkefni 3 - Leikjaforritun -

import pygame
import random
import os
import klasar

os.environ["SDL_VIDEO_CENTERED"] = "300"
pygame.init()

bakgrunnur = pygame.image.load("images/spaceman.png")

window_size = window_width, window_height = 846, 445
window = pygame.display.set_mode(window_size)
pygame.display.set_caption('Space invaders')

player = klasar.Player(window)
enemy_image = pygame.image.load("images/enemy1_1.png").convert_alpha()
missile = pygame.image.load("images/missile.png").convert_alpha()

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

enemyPosition = 65
missile_list = pygame.sprite.Group()
enemy_list = pygame.sprite.Group()
all_sprites_list = pygame.sprite.Group()
all_sprites_list.add(player)


for row in range(5):
    for column in range(10):
        enemy = klasar.Enemy(enemy_image)
        enemy.rect.x = 157 + (column * 50)
        enemy.rect.y = enemyPosition + (row * 45)
        enemy_list.add(enemy)
        all_sprites_list.add(enemy)


flag = True
teljari = 0
teljari2 = 2
running = True
speed = 1
listi = []
while running:
    window.fill(BLACK)
    window.blit(bakgrunnur, [0, 0])
    stig = player.stig
    clock.tick(60)
    key = pygame.key.get_pressed()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and teljari == 0:
            shot = klasar.Missile(missile)
            shot.rect.x = player.rect.x + 22
            shot.rect.y = player.rect.y
            missile_list.add(shot)
            all_sprites_list.add(shot)
            flag = True

    if flag and teljari < 20:
        teljari += 1
    if teljari >= 20:
        teljari = 0
        flag = False

    if key[pygame.K_LEFT] or key[pygame.K_a]:
        player.move(-2)
    if key[pygame.K_RIGHT] or key[pygame.K_d]:
        player.move(2)

    pygame.sprite.groupcollide(missile_list, enemy_list, True, True)

    for shot in missile_list:
        shot.rect.y -= 5
    for block in enemy_list:
        if block.rect.x == 0:
            speed = 1
        if block.rect.x == 800:
            speed = -1
        block.rect.x += speed





    all_sprites_list.draw(window)
    pygame.display.flip()
pygame.quit()
