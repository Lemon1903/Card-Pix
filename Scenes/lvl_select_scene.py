import sys
import pygame as pg
from Scripts.button import Button
from colors import LIGHTER_BLACK
from constants import *

# sprites
back_btn = Button(20, 10, LVL_SEL_BUTTON_W, LVL_SEL_BUTTON_H, "back")
lvl_buttons_sprites = pg.sprite.Group((LEVEL_BUTTONS, back_btn))
enlarged_btn = None

def draw_window(WIN):
    WIN.blit(LVL_SELECTION_BG, (0, 0))
    lvl_buttons_sprites.draw(WIN)
    pg.display.update()

def check_mouse_collision(mouse_pos):
    for button in lvl_buttons_sprites.sprites():
        if button.rect.collidepoint(mouse_pos):
            return button

def shade_hovered_btn(button):
    global enlarged_btn
    if enlarged_btn is not None:
        enlarged_btn.revert_to_original()
    if button is not None:
        button.shade()
        enlarged_btn = button

def function_button_clicked():
    if back_btn.is_activated: return (None, "Home")
    for i, button in enumerate(LEVEL_BUTTONS):
        if button.is_activated: return (i+1, "Game")
    return (None, None)
    
def Level_Select(WIN):
    while True:
        mouse_pos = pg.mouse.get_pos()
        button = check_mouse_collision(mouse_pos)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            if event.type == pg.MOUSEBUTTONDOWN:
                if button is not None:
                    button.activate()
                    CLICK_SOUND.play()

        shade_hovered_btn(button)
        draw_window(WIN)
        lvl, scene = function_button_clicked()
        if button is not None:
            button.is_activated = False
            button.revert_to_original()
        if scene is not None:
            return (lvl, scene)
        