import pygame as pg

from allgames_games.games_cl import ClickerGame
from allgames_games.games_ch import ChaserGame
from allgames_games.games_al import FallingGame

class GameMenu:      
    def __init__(self, screen, clock, assets):
        self.screen = screen
        self.clock = clock
        self.assets = assets

        self.clock = pg.time.Clock()
        self.running = True

        self.font = pg.font.Font(None, 50)

        # Load thumbnails
        self.clicker_thumb = pg.image.load("clicker_thumb.png")
        self.chaser_thumb = pg.image.load("chaser_thumb.png")
        self.falling_thumb = pg.image.load("falling_thumb.png")

        self.clicker_thumb = pg.transform.scale(self.clicker_thumb, (250, 200))
        self.chaser_thumb = pg.transform.scale(self.chaser_thumb, (250, 200))
        self.falling_thumb = pg.transform.scale(self.falling_thumb, (250, 200))

        # Button rectangles
        self.clicker_rect = pg.Rect(100, 300, 250, 200)
        self.chaser_rect = pg.Rect(375, 300, 250, 200)
        self.falling_rect = pg.Rect(650, 300, 250, 200)

        self.running = True
        self.next_state = "menu"

    def handle_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.running = False

            if event.type == pg.MOUSEBUTTONDOWN:
                mouse = pg.mouse.get_pos()

                if self.clicker_rect.collidepoint(mouse):
                    ClickerGame().run()

                if self.chaser_rect.collidepoint(mouse):
                    ChaserGame().run()

                if self.falling_rect.collidepoint(mouse):
                    FallingGame(self.screen, self.clock, self.assets).run()

    def draw(self):
        self.screen.fill((30, 30, 40))

        title = self.font.render("Choose a Game", True, (255, 255, 255))
        self.screen.blit(title, (400, 100))

        # Draw thumbnails
        self.screen.blit(self.clicker_thumb, self.clicker_rect)
        self.screen.blit(self.chaser_thumb, self.chaser_rect)
        self.screen.blit(self.falling_thumb, self.falling_rect)

        pg.display.flip()

    def run(self):
        while self.running:
            self.handle_events()
            self.draw()
            self.clock.tick(60)