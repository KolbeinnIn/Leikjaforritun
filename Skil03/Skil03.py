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
pygame.mixer.pre_init(44100, -16, 1, 512)


player = klasar.Player(window)
enemy_image = pygame.image.load("images/enemy1_1.png").convert_alpha()
missile = pygame.image.load("images/missile.png").convert_alpha()
eMissile = pygame.image.load("images/eMissile.png").convert_alpha()
cover_image = pygame.image.load("images/cover.png")


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

enemyPosition = 35
coverPos = 350
missile_list = pygame.sprite.Group()    # skot players
e_missile_list = pygame.sprite.Group()  # skot ovina (e fyrir enemy)
enemy_list = pygame.sprite.Group()
cover_list = pygame.sprite.Group()
player_list = pygame.sprite.Group()
all_sprites_list = pygame.sprite.Group()
all_sprites_list.add(player)


"""sounds = {}
for sound_name in ["ovinur_deyr", "skot"]:
    sounds[sound_name] = pygame.mixer.Sound("sounds/{}.wav".format(sound_name))
    sounds[sound_name].set_volume(10)
"""
#Enemies
for row in range(4):
    for column in range(8):
        enemy = klasar.Enemy(enemy_image)
        enemy.rect.x = 157 + (column * 50)
        enemy.rect.y = enemyPosition + (row * 45)
        enemy_list.add(enemy)
        all_sprites_list.add(enemy)
#Cover
for x in range(1, 4):
    for row in range(3):
        for column in range(20):
            cover = klasar.Enemy(cover_image)
            cover.rect.x = (193 * x) + (column * 2)
            cover.rect.y = coverPos + (row * 5)
            cover_list.add(cover)
            all_sprites_list.add(cover)

player_list.add(player)

flag = True
flag2 = False
teljari = 0
teljari2 = 2
running = True
speed = 1
enemy_shot = 0

lif = 4
while running:
    window.fill(BLACK)
    window.blit(bakgrunnur, [0, 0])
    stig = player.stig
    clock.tick(60)
    key = pygame.key.get_pressed()
    enemy_shot += 1
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and teljari == 0:
            #sounds["skot"].play()
            shot = klasar.Missile(missile)
            shot.rect.x = player.rect.x + 22
            shot.rect.y = player.rect.y
            missile_list.add(shot)
            all_sprites_list.add(shot)
            flag = True

    if enemy_shot % 53 == 0:
        eSkot = klasar.Missile(eMissile)
        a = random.randrange(0, len(enemy_list))
        eSkot.rect.x = enemy_list.sprites()[a].rect.x
        eSkot.rect.y = enemy_list.sprites()[a].rect.y
        e_missile_list.add(eSkot)
        all_sprites_list.add(eSkot)

    if flag and teljari < 40:
        teljari += 1
    if teljari >= 40:
        teljari = 0
        flag = False

    if key[pygame.K_LEFT] or key[pygame.K_a]:
        player.move(-2)
    if key[pygame.K_RIGHT] or key[pygame.K_d]:
        player.move(2)

    pygame.sprite.groupcollide(missile_list, enemy_list, True, True) and print("asd")#sounds["ovinur_deyr"].play()
    pygame.sprite.groupcollide(missile_list or e_missile_list, cover_list, True, True) and print("asd")#sounds["cover_collision"].play()

    if lif >= 0:
        if pygame.sprite.groupcollide(e_missile_list, player_list, True, False):
            # sounds["lose_life"].play()
            lif -= 1
            if lif == 0:
                print("Þú tapaðir")
                # sounds["game_over"].play()
                running = False

    for eshot in e_missile_list:
        eshot.rect.y += 5

    for shot in missile_list:
        shot.rect.y -= 5
    for block in enemy_list:
        if block.rect.x == 0:
            speed = 1
            flag2 = True
        if block.rect.x == 800:
            speed = -1
            flag2 = True
        if flag2:
            for x in range(len(enemy_list)):
                enemy_list.sprites()[x].rect.y += 3
            flag2 = False
        block.rect.x += speed

    if len(enemy_list) == 0:
        print("Til hamingju")
        running = False

    label = my_font.render("Líf: %s" % str(lif), 1, WHITE)
    window.blit(label, (20, 20))
    all_sprites_list.draw(window)
    pygame.display.flip()
pygame.quit()
