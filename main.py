import pygame as pg
from Scenes.game_scene import Game
from Scenes.home_scene import Home
from Scenes.lvl_select_scene import Level_Select
from colors import *
from constants import *

# ===== game window =====
pg.init()
LOADING_FONT = pg.font.Font("Assets/fonts/ThaleahFat.ttf", 70)
WIN = pg.display.set_mode((SCREEN_W, SCREEN_H))
GAME_ICON = pg.image.load("Assets/Others/game_icon/game_icon3.png")
pg.display.set_caption("Card Pix")
pg.display.set_icon(GAME_ICON)
MUSIC_BG.play(loops=-1)

# ===== function =====
def loading_screen():
    WIN.fill(INDIGO)
    LOADING = LOADING_FONT.render("Loading...", 1, WHITE3)
    WIN.blit(LOADING, (SCREEN_W/2 - LOADING.get_width()/2, SCREEN_H/2 - LOADING.get_height()/2))
    pg.display.update()

    LVL1 = Level(
        cards_in_lvl=8, pair_cards=1, width=150, height=150, 
        rows=2, pos_x=85, pos_y=140, padx=150, pady=155,
        card_names=["tomeyto-card", "lemon-card", "potato-card", "mochi-card"])
    LVL2 = Level(
        cards_in_lvl=12, pair_cards=1, width=150, height=150, 
        rows=2, pos_x=25, pos_y=140, padx=115, pady=155,
        card_names=["lemon-card", "tomeyto-card", "potato-card", 
            "mochi-card", "pineapple-card", "apple-card"])
    LVL3 = Level(
        cards_in_lvl=16, pair_cards=1, width=120, height=120, 
        rows=2, pos_x=15, pos_y=150, padx=90, pady=155,
        card_names=["lemon-card", "tomeyto-card", "potato-card", "mochi-card",
            "pineapple-card", "apple-card", "orange-card", "strawberry-card"])
    LVL4 = Level(
        cards_in_lvl=32, pair_cards=2, width=90, height=90, 
        rows=4, pos_x=70, pos_y=110, padx=80, pady=90,
        card_names=["lemon-card", "tomeyto-card", "potato-card", "mochi-card",
            "pineapple-card", "apple-card", "orange-card", "strawberry-card"])
    LVL5 = Level(
        cards_in_lvl=64, pair_cards=4, width=65, height=65, 
        rows=4, pos_x=-4, pos_y=133, padx=48, pady=80,
        card_names=["lemon-card", "tomeyto-card", "potato-card", "mochi-card",
            "pineapple-card", "apple-card", "orange-card", "strawberry-card"])
    Levels.extend([LVL1, LVL2, LVL3, LVL4, LVL5])

def main():
    scenes = {
        "Home": "HomeScene",
        "Game": "GameScene",
        "LevelSelect": "LevelSelectScene"
    }
    scene = "Home"
    level = None
    while scene is not None:
        if scenes[scene] == "HomeScene":
            Home(WIN)
            scene = "LevelSelect"
        elif scenes[scene] == "GameScene":
            level, scene = Game(WIN, level)
        elif scenes[scene] == "LevelSelectScene":
            level, scene = Level_Select(WIN)

if __name__ == "__main__":
    loading_screen()
    main()