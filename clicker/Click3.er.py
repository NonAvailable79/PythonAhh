import pygame as pg
pg.init()

white = (255, 255, 255)
black = (0, 0, 0)
green = (0, 255, 0)
blueISH = (0, 100, 155)

win_width = 800
win_height = 600
screen = pg.display.set_mode([win_width, win_height])
pg.display.set_caption('AAAAAAAAAAAAAA')
font = pg.font.Font(None, 50)

pg.mixer.music.load('ok.mp3')
pg.mixer.music.play(-1)

stick = pg.image.load('stick.png')
stick = pg.transform.scale(stick, (100, 100))

hammer = pg.image.load('hammer.png')
hammer = pg.transform.scale(hammer, (100, 100))

smasher = pg.image.load('smasher.png')
smasher = pg.transform.scale(smasher, (100, 100))

hand = pg.image.load('hand.png')
hand = pg.transform.scale(hand, (100, 100))

robot = pg.image.load('robot.png')
robot = pg.transform.scale(robot, (100, 100))

factory = pg.image.load('factory.png')
factory = pg.transform.scale(factory, (100, 100))

lock = pg.image.load('lock.png')
lock = pg.transform.scale(lock, (800, 200))

planet = pg.image.load('planet.png')
planet = pg.transform.scale(planet, (100, 100))

star = pg.image.load('star.png')
star = pg.transform.scale(star, (100, 100))

constellation = pg.image.load('constellation.png')
constellation = pg.transform.scale(constellation, (100, 100))

galaxy = pg.image.load('galaxy.png')
galaxy = pg.transform.scale(galaxy, (100, 100))

cluster = pg.image.load('cluster.png')
cluster = pg.transform.scale(cluster, (100, 100))

universe = pg.image.load('universe.png')
universe = pg.transform.scale(universe, (100, 100))

multiverse = pg.image.load('multiverse.png')
multiverse = pg.transform.scale(multiverse, (100, 100))

infinity = pg.image.load('infinity.png')
infinity = pg.transform.scale(infinity, (100, 100))

fund_x_min = win_width / 2 - 100
fund_x_max = win_width / 2 + 100
fund_y_min = win_height / 2 - 50
fund_y_max = win_height / 2 + 50

sticks = 0
hammers = 0
smashers = 0

hands = 0
robots = 0
factories = 0

planets = 0
stars = 0
constellations = 0
galaxies = 0
clusters = 0
universes = 0
multiverses = 0
infinities = 0

running = True
money = 0
power = 1

click = pg.mixer.Sound('no.mp3')

def check_click():
    global money, sticks, hammers, smashers, hands, robots, factories, planets, stars
    global constellations, galaxies, clusters, universes, multiverses, infinities
    click.play()
    x, y = pg.mouse.get_pos()

    if fund_x_min < x < fund_x_max and fund_y_min < y < fund_y_max:
        money += power

    if (win_width - 100) < x < win_width and 20 < y < 120 and money > 49:
        sticks += 1
        money -= 50
    
    if (win_width - 100) < x < win_width and 140 < y < 240 and money > 599:
        hammers += 1
        money -= 600

    if (win_width - 100) < x < win_width and 260 < y < 360 and money > 1999:
        smashers += 1
        money -= 2000

    if x < 100 and 20 < y < 120 and money > 99:
        hands += 1
        money -= 100

    if x < 100 and 140 < y < 240 and money > 399:
        robots += 1
        money -= 400

    if x < 100 and 260 < y < 360 and money > 2499:
        factories += 1
        money -= 2500

    if 400 < y < 500:
        if 600 < x < 700 and money > 10700000000:
            galaxies += 1
            money -= 10700000000
        elif 400 < x < 500 and money > 1000000000:
            constellations += 1
            money -= 1000000000
        elif 200 < x < 300 and money > 10000000:
            stars += 1
            money -= 10000000
        elif x < 100 and money > 1000000:
            planets += 1
            money -= 1000000

    if 520 < y < 620:
        if 600 < x < 700 and money > 1000000000000000000000:
            infinities += 1
            money -= 1000000000000000000000
        elif 400 < x < 500 and money > 1000000000000000:
            multiverses += 1
            money -= 1000000000000000
        elif 200 < x < 300 and money > 10000000000000:
            universes += 1
            money -= 10000000000000
        elif x < 100 and money > 425300000000:
            clusters += 1
            money -= 425300000000

while running:

    screen.fill(blueISH)
    pg.draw.rect(screen, green, (fund_x_min, fund_y_min,
                                 200, 100))
    
    screen.blit(stick, (win_width - 100, 20))
    screen.blit(hammer, (win_width - 100, 140))
    screen.blit(smasher, (win_width - 100, 260))

    screen.blit(hand, (0, 20))
    screen.blit(robot, (0, 140))
    screen.blit(factory, (0, 260))


    if money < 1000000:
        screen.blit(lock, (0, 400))
    else:
        screen.blit(planet, (0, 400))
        screen.blit(star, (200, 400))
        screen.blit(constellation, (400, 400))
        screen.blit(galaxy, (600, 400))
        screen.blit(cluster, (0, 520))
        screen.blit(universe, (200, 520))
        screen.blit(multiverse, (400, 520))
        screen.blit(infinity, (600, 520))

        planet_text = f'Planets: {planets}'
        planet_text = font.render(planet_text, 1, black)
        screen.blit(planet_text, (0, 400))

        star_text = f'Stars: {stars}'
        star_text = font.render(star_text, 1, black)
        screen.blit(star_text, (200, 400))

        constellation_text = f'Constls: {constellations}'
        constellation_text = font.render(constellation_text, 1, black)
        screen.blit(constellation_text, (400, 400))

        galaxy_text = f'Galaxies: {galaxies}'
        galaxy_text = font.render(galaxy_text, 1, black)
        screen.blit(galaxy_text, (600, 400))

        universe_text = f'Universes: {universes}'
        universe_text = font.render(universe_text, 1, black)
        screen.blit(universe_text, (200, 520))

        cluster_text = f'Clusters: {clusters}'
        cluster_text = font.render(cluster_text, 1, black)
        screen.blit(cluster_text, (0, 520))

        multiverse_text = f'Multvrs: {multiverses}'
        multiverse_text = font.render(multiverse_text, 1, black)
        screen.blit(multiverse_text, (400, 520))

        infinity_text = f'Infinities: {infinities}'
        infinity_text = font.render(infinity_text, 1, black)
        screen.blit(infinity_text, (600, 520))

    power = 1 + (sticks * (hands + 1)) + (hammers * (robots + 1) * 10) + (smashers *  (1 + factories) * 83) + (planets * 18234) + (stars * 103535) + (constellations * 17237456) + (galaxies * 921919191) + (universes * 65198765436) + (multiverses * 39816783451297) + (infinities * 754282343454563)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        if event.type == pg.MOUSEBUTTONDOWN:
            check_click()

    money_text = f'$ {money}'
    money_text = font.render(money_text, 1, black)
    screen.blit(money_text, (win_width / 2 - 100, 40))

    stick_text = f'Sticks: {sticks}'
    stick_text = font.render(stick_text, 1, black)
    screen.blit(stick_text, (win_width - 200, 40))

    hammer_text = f'Hammers: {hammers}'
    hammer_text = font.render(hammer_text, 1, black)
    screen.blit(hammer_text, (win_width - 240, 160))

    smasher_text = f'Smashers: {smashers}'
    smasher_text = font.render(smasher_text, 1, black)
    screen.blit(smasher_text, (win_width - 260, 280))

    hand_text = f'Hands: {hands}'
    hand_text = font.render(hand_text, 1, black)
    screen.blit(hand_text, (20, 40))

    robot_text = f'Robots: {robots}'
    robot_text = font.render(robot_text, 1, black)
    screen.blit(robot_text, (20, 160))

    factory_text = f'Factories: {factories}'
    factory_text = font.render(factory_text, 1, black)
    screen.blit(factory_text, (20, 280))

    #250!!
    pg.display.flip()

pg.quit()
