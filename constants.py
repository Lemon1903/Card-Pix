import pygame as pg
from Scripts.level import Level
from Scripts.button import Button
from Scripts.timer import Timer

pg.init()
PASSWORD = "020622"
# ===== sizes =====
SCREEN_W, SCREEN_H = 780, 560
UI_W, UI_H = 400, 400
ARTS_W, ARTS_H = 980, 560
GAME_BUTTON_W, GAME_BUTTON_H = 90, 90
HOME_BUTTON_W, HOME_BUTTON_H = 250, 120
LVL_SEL_BUTTON_W, LVL_SEL_BUTTON_H = 90, 90 
# ===== scene backgroounds =====
GAME_BG = pg.transform.scale(
    pg.image.load("Assets/Others/background.png"), (SCREEN_W, SCREEN_H))
HOME_BG = pg.transform.scale(
    pg.image.load("Assets/Others/home_screen.png"), (SCREEN_W, SCREEN_H))
LVL_SELECTION_BG = pg.transform.scale(
    pg.image.load("Assets/Others/level_selection.png"), (SCREEN_W, SCREEN_H))
# ===== UIs =====
PAUSE_UI = pg.transform.scale(
    pg.image.load("Assets/Others/pause.png"), (SCREEN_W, SCREEN_H))
LEVEL_COMPLETE_UI = pg.transform.scale(
    pg.image.load("Assets/Others/level_complete.png"), (UI_W, UI_H)) 
LEVEL_COMPLETE_UI_RECT = pg.Rect(SCREEN_W/2 - UI_W/2,  SCREEN_H/2 - UI_H/2, UI_W, UI_H)
GAME_OVER_UI = pg.transform.scale(
    pg.image.load("Assets/Others/game_over.png"), (UI_W, UI_H))
GAME_OVER_UI_RECT = LEVEL_COMPLETE_UI_RECT
GET_PASS_UI = pg.transform.scale(
    pg.image.load("Assets/Others/enter_pass.png"), (SCREEN_W, SCREEN_H))
ARTS_UI = pg.transform.scale(
    pg.image.load("Assets/Others/arts.png"), (SCREEN_W, SCREEN_H))
PASSWORD_ENTRY = pg.transform.scale(
    pg.image.load("Assets/Others/pass_entry.png"), (GAME_BUTTON_W+100, GAME_BUTTON_H-15))
PASSWORD_ENTRY_RECT = PASSWORD_ENTRY.get_rect(
    x=SCREEN_W/2 - PASSWORD_ENTRY.get_width()/2,
    y=SCREEN_H/2 - PASSWORD_ENTRY.get_height()/2 + 20)
ART1 = pg.transform.scale(pg.image.load("Assets/Others/arts/art1.png"), (ARTS_W, ARTS_H))
ART2 = pg.transform.scale(pg.image.load("Assets/Others/arts/art2.png"), (ARTS_W, ARTS_H))
ART3 = pg.transform.scale(pg.image.load("Assets/Others/arts/art3.png"), (ARTS_W, ARTS_H))
ART4 = pg.transform.scale(pg.image.load("Assets/Others/arts/art4.png"), (ARTS_W, ARTS_H))
ART5 = pg.transform.scale(pg.image.load("Assets/Others/arts/art5.png"), (ARTS_W, ARTS_H))
ARTS =  (ART1, ART2, ART3, ART4, ART5)
# ===== levels =====
Levels = [None]
# ===== game font =====
SCORE_FONT = pg.font.Font("Assets/fonts/ThaleahFat.ttf", 47)
PASSWORD_FONT = pg.font.Font("Assets/fonts/ThaleahFat.ttf", 50)
# ===== sounds =====
MUSIC_BG = pg.mixer.Sound("Assets/sounds/bg_music.mp3")
MUSIC_BG.set_volume(0.1)
FLIP_SOUND = pg.mixer.Sound("Assets/sounds/flip.wav")
MATCH_SOUND = pg.mixer.Sound("Assets/sounds/match.wav")
VICTORY_SOUND = pg.mixer.Sound("Assets/sounds/victory.wav")
VICTORY_SOUND.set_volume(1)
GAMEOVER_SOUND = pg.mixer.Sound("Assets/sounds/game_over.wav")
CLICK_SOUND = pg.mixer.Sound("Assets/sounds/click.wav")
CLICK_SOUND.set_volume(1)
# ===== buttons sprites =====
LC_RESTART_BTN = Button(
    SCREEN_W/2 - GAME_BUTTON_W/2 - 110, 
    SCREEN_H/2 - GAME_BUTTON_H/2 + 105,
    GAME_BUTTON_W, GAME_BUTTON_H, "restart_btn")
LC_HOME_BTN = Button(
    SCREEN_W/2 - GAME_BUTTON_W/2 + 5,
    SCREEN_H/2 - GAME_BUTTON_H/2 + 115,
    GAME_BUTTON_W, GAME_BUTTON_H, "home_btn")
LC_NEXT_BTN = Button(
    SCREEN_W/2 - GAME_BUTTON_W/2 + 110, 
    SCREEN_H/2 - GAME_BUTTON_H/2 + 105,
    GAME_BUTTON_W, GAME_BUTTON_H, "next_btn")
GO_RESTART_BTN = Button(
    SCREEN_W/2 - GAME_BUTTON_W/2 - 55, 
    SCREEN_H/2 - GAME_BUTTON_H/2 + 45,
    GAME_BUTTON_W, GAME_BUTTON_H, "restart_btn_go")
GO_HOME_BTN = Button(
    SCREEN_W/2 - GAME_BUTTON_W/2 + 60,
    SCREEN_H/2 - GAME_BUTTON_H/2 + 45,
    GAME_BUTTON_W, GAME_BUTTON_H, "home_btn")
TU_PAUSE_BTN = Button(
    SCREEN_W - 100, 0, GAME_BUTTON_W, GAME_BUTTON_H, "pause_btn")
TU_ARTS_BTN = Button(
    TU_PAUSE_BTN.rect.x - 90, 0, GAME_BUTTON_W , GAME_BUTTON_H, "arts_btn")
PA_RESUME_BTN = Button(
    SCREEN_W/2 - GAME_BUTTON_W/2 + 5,
    SCREEN_H/2 - GAME_BUTTON_H/2 + 45,
    GAME_BUTTON_W, GAME_BUTTON_H, "resume_btn")
PA_RESTART_BTN = Button(
    SCREEN_W/2 - GAME_BUTTON_W/2 - 95, 
    SCREEN_H/2 - GAME_BUTTON_H/2 + 45,
    GAME_BUTTON_W, GAME_BUTTON_H, "restart_btn_go")
PA_HOME_BTN = Button(
    SCREEN_W/2 - GAME_BUTTON_W/2 + 100, 
    SCREEN_H/2 - GAME_BUTTON_H/2 + 45,
    GAME_BUTTON_W, GAME_BUTTON_H, "home_btn")
LVL1_BTN = Button(
    SCREEN_W/2 - LVL_SEL_BUTTON_W/2 - 130, 
    SCREEN_H/2 - LVL_SEL_BUTTON_H/2 - 10, 
    LVL_SEL_BUTTON_W, LVL_SEL_BUTTON_H, "level_1")
LVL2_BTN = Button(
    SCREEN_W/2 - LVL_SEL_BUTTON_W/2, 
    SCREEN_H/2 - LVL_SEL_BUTTON_H/2 - 10, 
    LVL_SEL_BUTTON_W, LVL_SEL_BUTTON_H, "level_2") 
LVL3_BTN = Button(
    SCREEN_W/2 - LVL_SEL_BUTTON_W/2 + 130, 
    SCREEN_H/2 - LVL_SEL_BUTTON_H/2 - 10, 
    LVL_SEL_BUTTON_W, LVL_SEL_BUTTON_H, "level_3")
LVL4_BTN = Button(
    SCREEN_W/2 - LVL_SEL_BUTTON_W/2 - 65, 
    SCREEN_H/2 - LVL_SEL_BUTTON_H/2 + 70, 
    LVL_SEL_BUTTON_W, LVL_SEL_BUTTON_H, "level_4")
LVL5_BTN = Button(
    SCREEN_W/2 - LVL_SEL_BUTTON_W/2 + 65, 
    SCREEN_H/2 - LVL_SEL_BUTTON_H/2 + 70, 
    LVL_SEL_BUTTON_W, LVL_SEL_BUTTON_H, "level_5")
LVL1_DISABLED_BTN = Button(
    SCREEN_W/2 - LVL_SEL_BUTTON_W/2 - 130, 
    SCREEN_H/2 - LVL_SEL_BUTTON_H/2 - 10, 
    LVL_SEL_BUTTON_W, LVL_SEL_BUTTON_H, "level_1_disabled")
LVL2_DISABLED_BTN = Button(
    SCREEN_W/2 - LVL_SEL_BUTTON_W/2, 
    SCREEN_H/2 - LVL_SEL_BUTTON_H/2 - 10, 
    LVL_SEL_BUTTON_W, LVL_SEL_BUTTON_H, "level_2_disabled") 
LVL3_DISABLED_BTN = Button(
    SCREEN_W/2 - LVL_SEL_BUTTON_W/2 + 130, 
    SCREEN_H/2 - LVL_SEL_BUTTON_H/2 - 10, 
    LVL_SEL_BUTTON_W, LVL_SEL_BUTTON_H, "level_3_disabled")
LVL4_DISABLED_BTN = Button(
    SCREEN_W/2 - LVL_SEL_BUTTON_W/2 - 65, 
    SCREEN_H/2 - LVL_SEL_BUTTON_H/2 + 70, 
    LVL_SEL_BUTTON_W, LVL_SEL_BUTTON_H, "level_4_disabled")
LVL5_DISABLED_BTN = Button(
    SCREEN_W/2 - LVL_SEL_BUTTON_W/2 + 65, 
    SCREEN_H/2 - LVL_SEL_BUTTON_H/2 + 70, 
    LVL_SEL_BUTTON_W, LVL_SEL_BUTTON_H, "level_5_disabled")
LEVEL_BUTTONS = [LVL1_BTN, LVL2_BTN, LVL3_BTN, LVL4_BTN, LVL5_BTN]
# ===== timer =====
TIMER = Timer(20, 420, SCREEN_W - 30, 125)
TIMER_SPRITE = pg.sprite.GroupSingle(TIMER)