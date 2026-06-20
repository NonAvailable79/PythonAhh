'''
| Hey, if you are here from Github, please read the README.md file.
-
| If not, nobody cares. So run the file ._.
| If not, you're probably my family or friends. It's ok, You don't have to understand the code.
| Basically, this is a bunch of games. Yay~!
-
| AI helped me make this. Thanks Chat-GPT. The games are in PythonGames and made previously.
| They're now classes (>.<) but nobody cares >.< :] ;/
| GitHub Copilot is giving me annoying suggestions. Thank you~ (i like annoyingness)
-
| Please do not run the file from anywhere but here because the imports are based on this directory.
| So don't complain to me!
-
    YOURE MY SODA POP
    get soda popped
-
| made in 2026 by :/
'''
import allgames_manager as gm
import allgames_assets as asss
import allgames_to_preload_assets as tpa
from allgames_menu import GameMenu

import pygame as pg

def main():
    pg.init()

    screen = pg.display.set_mode((1000, 700))
    clock = pg.time.Clock()

    assets = asss.AssetManager()
    tpa.preload_al_assets(assets)
    tpa.preload_ch_assets(assets)
    tpa.preload_cl_assets(assets)
    tpa.preload_dr_assets(assets)

    manager = gm.GameManager(screen, clock, assets)
    manager.run()

    pg.quit()


if __name__ == "__main__":
    main()

pg.quit()