'''This file is edited from the original to 
be better at expressing what functions are supposed to do.

Runs better?'''

import pygame as pg 
import random, time
pg.init()
clock = pg.time.Clock()

black = (0, 0, 0)
white = (255, 255, 255)
win_width = 800
win_height = 600
screen = pg.display.set_mode((win_width, win_height))
pg.display.set_caption('eh')

font = pg.font.Font(None, 30)
speed = 10
score = 0
wave = 1
health = 50
running = True

player_size = 40
player_pos = win_width / 2, win_height - player_size
player_image = pg.image.load('guy.png')
player_image = pg.transform.scale(player_image, (player_size, player_size))

obj_size = 60
obj_data = []
obj = pg.image.load('ENEMY.png')
obj = pg.transform.scale(obj, (obj_size, obj_size))

bg_image = pg.image.load('background.png')
bg_image = pg.transform.scale(bg_image, (win_width, win_height))

wipeout_size = 40
wipeout_data = []
wipeout = pg.image.load('DESTROY.png')
wipeout = pg.transform.scale(wipeout, (wipeout_size, wipeout_size))

buff = pg.image.load('help.png')
buff_data = []
buff_size = 40
buff = pg.transform.scale(buff, (buff_size, buff_size))

pg.mixer.music.load('Music.mp3')
pg.mixer.music.play(-1)
pg.mixer.music.set_volume(0.6)

def die():
    pg.mixer.music.stop()
    screen.fill(black)
    death_text = f'You died.'
    death_text = font.render(death_text, 1, white)
    screen.blit(death_text, (win_width / 2 - 40, win_height / 2))
    pg.display.flip()
    diesound = pg.mixer.Sound('dead.mp3')
    diesound.play()
    time.sleep(5)

def create_object(thing_data, thing, length, pick, size):
    if len(thing_data) < length and random.random() < pick:
        x = random.randint(0, win_width - size)
        y = 0
        thing_data.append([x, y, thing])

    return thing_data

def update_objects(obj_data, thing_type):
    global score

    for object in obj_data:
        x, y, image_data = object
        if y < win_height:
            if thing_type == 1 or thing_type == 2:
                y += speed * 0.8
            else:
                y += speed* 0.7
            object[1] = y
            screen.blit(image_data, (x, y))
        else:
            obj_data.remove(object)
            if not thing_type == 3:
                score += 1

def collision_check(obj_data, size, player_pos, thing_type):
    global running, player_size, health

    for object in obj_data:
        x, y, image_data = object
        player_x, player_y = player_pos[0], player_pos[1]
        thing_rect = pg.Rect(x, y, size, size)
        player_rect = pg.Rect(player_x, player_y, player_size, player_size)
        
        if player_rect.colliderect(thing_rect):
            if thing_type == 1:
                hit = pg.mixer.Sound('damaged.mp3')
                hit.play()
                health -= 10
                obj_data.remove(object)
            elif thing_type == 2:
                die()
                time.sleep(2)
                running = False
                break
            elif thing_type == 3:
                health += 5
                heal = pg.mixer.Sound('heal.mp3')
                heal.play()
                buff_data.remove(object)

while running:

    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

        if event.type == pg.KEYDOWN:
            x, y = player_pos[0], player_pos[1]
            if event.key == pg.K_LEFT:
                x -= 20
                if x < 0:
                    x = 0
            elif event.key == pg.K_RIGHT:
                x += 20
                if x > win_width - player_size:
                    x = win_width - player_size
            player_pos = [x, y]

    if health < 1:
        die()
        time.sleep(2)
        running = False

    wave = score // 20 + 1
    speed = 10 + (wave - 1)
    obj_size = 40 + (wave - 1)
    wipeout_size = 40 + (wave * 5 - 1)

    obj = pg.transform.scale(obj, (obj_size, obj_size))
    wipeout = pg.transform.scale(wipeout, (wipeout_size, wipeout_size))

    screen.blit(bg_image, (0, 0))
    screen.blit(player_image, (player_pos[0], player_pos[1]))

    score_text = f'Score: {score}'
    score_text = font.render(score_text, 1, black)
    screen.blit(score_text, (win_width - 200, win_height - 40))

    wave_text = f'Wave: {wave}'
    wave_text = font.render(wave_text, 1, black)
    screen.blit(wave_text, (win_width - 200, win_height - 60))

    health_text = f'Health: {health}'
    health_text = font.render(health_text, 1, black)
    screen.blit(health_text, (win_width - 200, win_height - 80))

    create_object(obj_data, obj, 10, 0.05, obj_size)
    create_object(buff_data, buff, 5, 0.01, buff_size)
    create_object(wipeout_data, wipeout, 6, 0.03, buff_size)

    update_objects(obj_data, 1)
    update_objects(wipeout_data, 2)
    update_objects(buff_data, 3)

    collision_check(obj_data, obj_size, player_pos, 1)
    collision_check(wipeout_data, wipeout_size, player_pos, 2)
    collision_check(buff_data, buff_size, player_pos, 3)

    clock.tick(30)
    pg.display.flip()
