import sys
import pygame as pg
from colors import *
from constants import *

# ===== global variables =====
# game variables
clock = pg.time.Clock()
currentLvl, currentArt = None, ARTS_UI
lvl_complete, game_over, pause = False, False, False
get_pass, arts, sound_played = False, False, False
text_input = ""
# cards checking
first_card, second_card = None, None
enlarged_card, shaded_btn = None, None
# buttons sprites group
top_ui_buttons = pg.sprite.Group((TU_ARTS_BTN, TU_PAUSE_BTN))
pause_buttons = pg.sprite.Group((PA_RESTART_BTN, PA_RESUME_BTN, PA_HOME_BTN))
lc_buttons = pg.sprite.Group((LC_RESTART_BTN, LC_HOME_BTN, LC_NEXT_BTN))
go_buttons = pg.sprite.Group((GO_RESTART_BTN, GO_HOME_BTN))
ar_buttons = pg.sprite.Group([
    LVL1_DISABLED_BTN, LVL2_DISABLED_BTN, LVL3_DISABLED_BTN, 
    LVL4_DISABLED_BTN, LVL5_DISABLED_BTN
])

# ===== draw scene =====
def draw_window(WIN, cards_sprites):
    global lvl_complete, game_over, pause, get_pass, arts, sound_played, text_input
    WIN.blit(GAME_BG, (0, 0))
    top_ui_buttons.draw(WIN)
    cards_sprites.draw(WIN)
    cards_sprites.update()
    if lvl_complete:
        show_lvl_complete(WIN)
        score = SCORE_FONT.render(str(TIMER.time_solved), 1, LIGHTER_BLACK)
        WIN.blit(score,
            (SCREEN_W/2 - score.get_width()//2 + 35,
            SCREEN_H/2 - score.get_height()//2 + 20))
        if not sound_played:
            VICTORY_SOUND.play()
            sound_played = True
    elif game_over: 
        show_game_over(WIN)
        if not sound_played:
            GAMEOVER_SOUND.play()
            sound_played = True
    else:
        TIMER_SPRITE.draw(WIN)
        if get_pass:
            show_get_pass(WIN)
            password = PASSWORD_FONT.render(text_input, 1, LIGHTER_BLACK)
            WIN.blit(password, (PASSWORD_ENTRY_RECT.x+22, PASSWORD_ENTRY_RECT.y+15))
        elif arts:
            show_arts(WIN)
        elif pause:
            show_pause(WIN)
        else:
            text_input = ""
            TIMER_SPRITE.update()
    pg.display.update()

def show_pause(WIN):
    WIN.blit(PAUSE_UI, (0, 0))
    pause_buttons.draw(WIN)

def show_get_pass(WIN):
    WIN.blit(GET_PASS_UI, (0, 0))
    WIN.blit(PASSWORD_ENTRY, (PASSWORD_ENTRY_RECT))

def show_arts(WIN):
    global currentArt
    if currentArt == ARTS_UI:
        WIN.blit(currentArt, (0, 0))
        ar_buttons.draw(WIN)
    else:
        WIN.blit(currentArt, (SCREEN_W/2 - ARTS_W/2, 0))

def show_lvl_complete(WIN):
    WIN.blit(LEVEL_COMPLETE_UI, LEVEL_COMPLETE_UI_RECT)
    lc_buttons.draw(WIN)

def show_game_over(WIN):
    WIN.blit(GAME_OVER_UI, GAME_OVER_UI_RECT)
    go_buttons.draw(WIN)

# ===== checking =====
def check_mouse_collision(mouse_pos, cards=None, btn=False, 
                        pause=False, arts=False, top_ui=False):
    global lvl_complete, game_over
    buttons = {
        "pause": pause_buttons, "arts": ar_buttons, 
        "lvl complete": lc_buttons, "gameover": go_buttons
    }
    button_place = None
    if top_ui:
        for button in top_ui_buttons:
            if button.rect.collidepoint(mouse_pos):
                return button
    if btn:
        if pause: button_place = "pause"
        if arts: button_place = "arts"
        if lvl_complete: button_place = "lvl complete"
        if game_over: button_place = "gameover"
        if button_place is None: return None
        for button in buttons[button_place]:
            if button.rect.collidepoint(mouse_pos):
                return button
    else:
        for card in cards.sprites():
            if card.rect.collidepoint(mouse_pos):
                return card

def check_card_pair():
    global first_card, second_card, sound_played
    if first_card.name == second_card.name:
        first_card.animate_shrink()
        second_card.animate_shrink()
        TIMER.add_time(3)
        MATCH_SOUND.play()
    else:
        first_card.animate_flip()
        second_card.animate_flip()
        FLIP_SOUND.play()
    first_card = second_card = None

def check_cards_clicked(clicked_cards):
    global first_card, second_card
    # implemented a stack to check first clicked cards
    if len(clicked_cards) > 0:
        # check animation if done
        if not clicked_cards[0].is_animating_flip and first_card is None:
            first_card = clicked_cards[0]
            clicked_cards.pop(0)
        elif not clicked_cards[0].is_animating_flip and second_card is None:
            second_card = clicked_cards[0]
            clicked_cards.pop(0)
    # compare the two cards
    if first_card is not None and second_card is not None:
        check_card_pair()

def check_level_completeness():
    global lvl_complete, game_over, currentLvl, ar_buttons
    if Levels[currentLvl].is_completed():
        ar_buttons = pg.sprite.Group([
            LEVEL_BUTTONS[currentLvl-1] if i == currentLvl-1 
            else ar_buttons.sprites()[i] for i in range(len(ar_buttons.sprites())) 
        ])
        lvl_complete = True
    if TIMER.times_up:
        game_over = True

# ===== update game objects =====
def shade_hovered_button(button):
    global shaded_btn
    if shaded_btn is not None:
        shaded_btn.revert_to_original()
    if button is not None:
        button.shade()
        shaded_btn = button

def enlarge_hovered_card(card):
    global enlarged_card
    if enlarged_card is not None and not enlarged_card.is_animating_shrink:
        enlarged_card.shrink()
    if card is not None and not card.is_animating_shrink:
        card.enlarge()
        enlarged_card = card

def enlarge_all_cards(cards_sprites):
    if cards_sprites.sprites()[0].is_normal_size():
        return False
    if not cards_sprites.sprites()[0].is_animating_enlarge:
        for card in cards_sprites.sprites():
            card.animate_enlarge()
    return True

def shrink_all_cards(card_sprites):
    for card in card_sprites.sprites():
        card.animate_shrink()

# ===== update game =====
def game_status(mouse_pos, cards_sprites, clicked_cards, game_start):
    global lvl_complete, game_over, pause, get_pass, arts, sound_played
    button, card = None, None
    if game_start:
        game_start = enlarge_all_cards(cards_sprites)
    elif get_pass:
        button = check_mouse_collision(mouse_pos, btn=True, top_ui=True)
    elif arts:
        button = check_mouse_collision(mouse_pos, btn=True, arts=True, top_ui=True)
    elif pause:
        button = check_mouse_collision(mouse_pos, btn=True, pause=True, top_ui=True)
    elif lvl_complete:
        button = check_mouse_collision(mouse_pos, btn=True)
    elif game_over:
        button = check_mouse_collision(mouse_pos, btn=True)
        shrink_all_cards(cards_sprites)
    else:
        card = check_mouse_collision(mouse_pos, cards=cards_sprites)
        button = check_mouse_collision(mouse_pos, btn=True, top_ui=True)
        sound_played = False
        check_level_completeness()
        check_cards_clicked(clicked_cards)
        enlarge_hovered_card(card)
    shade_hovered_button(button) 
    return (game_start, button, card)

def function_button_clicked():
    global pause, get_pass, arts, currentLvl, currentArt
    ret = [currentLvl, None]
    # arts ui buttons
    for i, button in enumerate(LEVEL_BUTTONS):
        if button.is_activated: currentArt = ARTS[i]
    # top ui buttons
    if TU_PAUSE_BTN.is_activated:
        pause = True
        arts = get_pass = False
        currentArt = ARTS_UI
    elif TU_ARTS_BTN.is_activated:
        pause = False
        if arts and not get_pass: 
            currentArt = ARTS_UI
            arts = not arts
        else: 
            get_pass = not get_pass
    # other ui buttons
    if PA_RESUME_BTN.is_activated:
        pause = False
    elif LC_RESTART_BTN.is_activated or GO_RESTART_BTN.is_activated or PA_RESTART_BTN.is_activated:
        pause = False
        ret[1] = "Game"
    elif LC_HOME_BTN.is_activated or GO_HOME_BTN.is_activated or PA_HOME_BTN.is_activated:
        pause = False
        ret[1] = "Home"
    elif LC_NEXT_BTN.is_activated:
        ret[0] = currentLvl+1 if currentLvl < len(Levels)-1 else currentLvl
        ret[1] = "Game"
    return ret

# ===== main game function =====
def Game(WIN, level):
    global lvl_complete, game_over, get_pass, arts, text_input, currentLvl, first_card, second_card
    # default values
    clicked_cards, currentLvl, game_start = [], level, True
    cards_sprites = Levels[currentLvl].cards_sprites_init()
    # game loop
    while True:
        clock.tick(60)
        mouse_pos = pg.mouse.get_pos()
        game_start, button, card = game_status(mouse_pos, cards_sprites, clicked_cards, game_start)
        
        # events checking
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            if event.type == pg.MOUSEBUTTONDOWN:
                # activate button
                if button is not None:
                    button.activate()
                    CLICK_SOUND.play()
                # opens the card
                if card is not None and card.is_close():
                    card.animate_flip()
                    clicked_cards.append(card)
                    FLIP_SOUND.play()
            if event.type == pg.KEYDOWN and get_pass:
                if event.key == pg.K_RETURN:
                    get_pass = False
                    arts = text_input == PASSWORD
                    text_input = ""
                elif event.key == pg.K_BACKSPACE:
                    text_input = text_input[:-1]
                elif len(text_input) < 6:
                    text_input += event.unicode

        draw_window(WIN, cards_sprites)
        lvl, scene = function_button_clicked()
        if button is not None:
            button.is_activated = False
        if scene is not None:
            lvl_complete = game_over = False
            first_card = second_card = None
            TIMER.reset()
            return (lvl, scene)