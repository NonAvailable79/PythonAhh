import pygame as pg
import random, time
pg.init()
clock = pg.time.Clock()

black = (0, 0, 0)
white = (255, 255, 255)

win_width = 800
win_height = 600
screen = pg.display.set_mode((win_width, win_height))
pg.display.set_caption('justacopy')

lane_width = 120
extra = 220
car = pg.image.load('ccar.png')
car = pg.transform.scale(car, (lane_width, 192))
car_pos = [extra, win_height - 192]

obstacle_1 = pg.image.load('cone.png')
obstacle_1 = pg.transform.scale(obstacle_1, (lane_width, lane_width))
obstacle_2 = pg.image.load('stop.png')
obstacle_2 = pg.transform.scale(obstacle_2, (lane_width, lane_width))
obstacles = []

home = pg.image.load('home.png')
road = pg.image.load('road.png')

pg.mixer.music.load('front.mp3')
pg.mixer.music.play(-1)

font = pg.font.Font(None, 30)
time_ = 0
game_speed = 10
running = True
fps = 33
can = 0
in_game = 'home'

def end_go_back():
    global in_game, obstacles, time_

    for i in range(5, -1, -1):
        screen.fill(black)

        dead_text = font.render('You crashed your car.', 1, white)
        screen.blit(dead_text, (win_width / 2, win_height / 2))

        done = f'Final score: {int(time_)}'
        done = font.render(done, 1, white)
        screen.blit(done, (win_width / 2, 350))

        hometime = f'Redirecting in {i} seconds...'
        hometime = font.render(hometime, 1, white)
        screen.blit(hometime, (win_width / 2, 400))
        time.sleep(1)
        pg.display.flip()

    time_ = 0
    obstacles = []
    in_game = 'home'

def check_click():
    global in_game

    x, y = pg.mouse.get_pos()
    if 200 < x < 500 and 350 < y < 400:
        in_game = 'game'

def spawn_obstacles():
    global obstacles, can
    if len(obstacles) < 3 and random.random() < 0.4 and can > 50:
        x = extra + random.randint(0, 2) * lane_width
        y = 0
        picked_image = random.choice([obstacle_1, obstacle_2])
        obstacles.append([x, y, picked_image])

def update_obstacles(obstacles):
    for object in obstacles:
        x, y, image_data = object
        if y < win_height:
            y += game_speed
            object[1] = y
            screen.blit(image_data, (x, y))
        else:
            obstacles.remove(object)
            
    return obstacles

def collision_check():
    for hello in obstacles:
        x, y, image_data = hello
        car_x, car_y = car_pos[0], car_pos[1]
        obs_rect = pg.Rect(x, y, lane_width, lane_width)
        player_rect = pg.Rect(car_x, car_y, lane_width, 192)
        
        if player_rect.colliderect(obs_rect):
            end_go_back()

while running:
    if in_game == 'game':
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False

            if event.type == pg.KEYDOWN:
                x, y = car_pos[0], car_pos[1]
                if event.key == pg.K_LEFT:
                    x -= lane_width
                    if x < extra:
                        x = extra
                elif event.key == pg.K_RIGHT:
                    x += lane_width
                    if x > win_width - extra - 20:
                        x = win_width - extra - 20
                car_pos = [x, y]

        wave = time_ // 20 + 1
        speed = 10 + (wave - 1)
        time_ += 1 / fps

        screen.blit(road, (0, 0))
        screen.blit(car, (car_pos[0], car_pos[1]))
        
        can += 1

        spawn_obstacles()
        update_obstacles(obstacles)
        collision_check()
        
        if can > 50:
            can = 0

        score_text = f'Score: {int(time_)}'
        score_text = font.render(score_text, 1, black)
        screen.blit(score_text, (20, win_height - 20))

        clock.tick(33)
        pg.display.flip()

    elif in_game == 'home':
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            if event.type == pg.MOUSEBUTTONDOWN:
                check_click()

        screen.blit(home, (0, 0))

        clock.tick(fps)
        pg.display.flip()

pg.quit()
