import pygame as pg 
import time
import random
pg.init()
clock = pg.time.Clock()
speed = 33

white = (255, 255, 255)
black = (0, 0, 0)

win_width = 800
win_height = 600
screen = pg.display.set_mode((win_width, win_height))
pg.display.set_caption('ok')
font = pg.font.Font(None, 40)

size = 50
player = pg.image.load('player.png')
player = pg.transform.scale(player, (size, size))
player_pos = [0, 0]
player_speed = 18
player_added_speed = 0

chaser = pg.image.load('chaser.png')
chaser = pg.transform.scale(chaser, (size, size))
chaser_pos = [win_width - size, win_height - size]
chaser_speed = 1.23
chaser_added_speed = 0

acc = pg.image.load('faster.png')
acc = pg.transform.scale(acc, (size, size))
acc_data = []

portal = pg.image.load('portal.png')
portal = pg.transform.scale(portal, (size, size))
portal_data = []

pg.mixer.music.load('Hi.mp3')
pg.mixer.music.play(-1)

running = True
time_ = 0

def die():
    global time_
    pg.mixer.music.stop()
    diesound = pg.mixer.Sound('die.mp3')
    diesound.play()
    screen.fill(black)
    death_text = font.render('You died.', 1, white)
    screen.blit(death_text, (300, 100))
    survival_text = f'You survived {int(time_)} seconds.'
    survival_text = font.render(survival_text, 1, white)
    screen.blit(survival_text, (200, 300))
    pg.display.flip()
    time.sleep(7)

def spawn_stuff():
    global acc_data, portal_data, size
    if len(acc_data) < 2 and random.randint(1, 20) == 1:
        acc_x = random.randint(0, win_width - size)
        acc_y = random.randint(0, win_height - size)
        acc_data.append([acc_x, acc_y, acc])

    if len(portal_data) < 2 and random.randint(1, 20) == 1:
        portal_x = random.randint(0, win_width - size)
        portal_y = random.randint(0, win_height - size)
        portal_data.append([portal_x, portal_y, portal])

    for i in range(len(acc_data)):
        screen.blit(acc, (acc_data[i][0], acc_data[i][1]))
    for i in range(len(portal_data)):
        screen.blit(portal, (portal_data[i][0], portal_data[i][1]))

def chase():
    global player_pos, chaser_pos

    x, y = player_pos
    cx, cy = chaser_pos
    if x < cx:
        cx -= 1.233333333333333333333
    if x > cx:
        cx += 1.2333333
    if y < cy:
        cy -= 1.23
    if y > cy:
        cy += 1.2
    chaser_pos = [cx, cy]

def collision_check(chaser_added_speed, player_added_speed):
    global player_pos, chaser_pos, size, running

    player_rect = pg.Rect(player_pos[0], player_pos[1], size, size)
    chaser_rect = pg.Rect(chaser_pos[0], chaser_pos[1], size, size)

    if player_rect.colliderect(chaser_rect):
        running = False
        die()

    for hm in acc_data:
        acc_rect = pg.Rect(hm[0], hm[1], size, size)
        if player_rect.colliderect(acc_rect):
            player_added_speed += 1
            acc_data.remove(hm)
        if chaser_rect.colliderect(acc_rect):
            chaser_added_speed += 1
            acc_data.remove(hm)

    for hm in portal_data:
        portal_rect = pg.Rect(hm[0], hm[1], size, size)
        if player_rect.colliderect(portal_rect):
            player_pos = [random.randint(0, win_width), random.randint(0, win_height)]
            portal_data.remove(hm)
        if chaser_rect.colliderect(portal_rect):
            chaser_pos = [random.randint(0, win_width), random.randint(0, win_height)]
            portal_data.remove(hm)

while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        if event.type == pg.KEYDOWN:
            x, y = player_pos
            if event.key == pg.K_LEFT:
                x -= 18
                if x < 0:
                    x = 0
            if event.key == pg.K_RIGHT:
                x += 18
                if x > win_width - size:
                    x = win_width - size
            if event.key == pg.K_UP:
                y -= 18
                if y < 0:
                    y = 0
            if event.key == pg.K_DOWN:
                y += 18
                if y > win_height - size:
                    y = win_height - size
            player_pos = [x, y]

    chase()
    collision_check(chaser_added_speed, player_added_speed)

    chaser_speed = 1.23 + chaser_added_speed
    player_speed = 18 + player_added_speed

    time_ += 1 / speed
    screen.fill(white)
    spawn_stuff()
    screen.blit(player, (player_pos[0], player_pos[1]))
    screen.blit(chaser, (chaser_pos[0], chaser_pos[1]))

    time_text = f'Survival time: {int(time_)} seconds'
    time_text = font.render(time_text, 1, black)
    screen.blit(time_text, (20, 20))

    clock.tick(speed)
    pg.display.flip()

pg.quit()
