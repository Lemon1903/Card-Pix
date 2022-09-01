import sys
import pygame as pg
from constants import *
from Scripts.button import Button

# sprite
play_btn = pg.sprite.GroupSingle(
    Button(
        SCREEN_W/2 - HOME_BUTTON_W/2 + 5, 
        SCREEN_H/2 - HOME_BUTTON_W/2 + 185, 
        HOME_BUTTON_W, HOME_BUTTON_H, "play_btn"
    ) 
)

def draw_window(WIN):
    WIN.blit(HOME_BG, (0, 0))
    play_btn.draw(WIN)
    pg.display.update()

def enlarge_play_btn(mouse_pos):
    if play_btn.sprite.rect.collidepoint(mouse_pos):
        play_btn.sprite.enlarge()
        return True
    else:
        play_btn.sprite.shrink()
        return False

def Home(WIN):
    play = False
    while True:
        mouse_pos = pg.mouse.get_pos()
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            if event.type == pg.MOUSEBUTTONDOWN:
                if play: 
                    CLICK_SOUND.play()
                    return

        play = enlarge_play_btn(mouse_pos)
        draw_window(WIN)