from allgames_menu import GameMenu
from allgames_games.games_al import FallingGame
from allgames_games.games_ch import ChaserGame
from allgames_games.games_cl import ClickerGame
from allgames_games.games_dr import DrivingGame
import inspect

class GameManager:

    def __init__(self, screen, clock, assets):

        self.screen = screen
        self.clock = clock
        self.assets = assets

        self.games = {
            "menu": GameMenu,
            "clicker": ClickerGame,
            "chaser": ChaserGame,
            "falling": FallingGame,
            "driver": DrivingGame
        }

        self.current_game = GameMenu(screen, clock, assets)

    def run(self):

        running = True

        while running:

            next_game = self.current_game.run()

            if next_game == "quit":
                running = False

            else:
                game_class = self.games[next_game]
                # instantiate flexibly depending on constructor signature
                try:
                    sig = inspect.signature(game_class.__init__)
                    params = len(sig.parameters) - 1
                except Exception:
                    params = 3

                if params >= 3:
                    self.current_game = game_class(self.screen, self.clock, self.assets)
                elif params == 0:
                    self.current_game = game_class()
                else:
                    try:
                        self.current_game = game_class(self.screen, self.clock)
                    except Exception:
                        self.current_game = game_class()