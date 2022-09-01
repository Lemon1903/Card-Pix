import pygame as pg
import random
from Scripts.card import Card

class Level:
    def __init__(self, cards_in_lvl, pair_cards, height, width, card_names,
                rows, pos_x, pos_y,  padx, pady, *args, **kwargs):

        # user defined variables
        self.cards_in_lvl = cards_in_lvl
        self.pair_cards = pair_cards
        self.card_width = width
        self.card_height = height
        self.card_names = card_names
        self.rows = rows
        self.x, self.y = pos_x, pos_y
        self.padx, self.pady = padx, pady
        # level variables
        self.complete = False
        self.cards = []
        self.card_sprites = pg.sprite.Group()
        self.cards_init()

    # ===== level initialize =====
    def cards_init(self):
        name_idx, counter = 0, 1
        for _ in range(self.cards_in_lvl):
            self.cards.append(
                Card(self.card_width, self.card_height, self.card_names[name_idx]))
            if counter == self.pair_cards*2:
                counter = 1
                name_idx += 1
            else: 
                counter += 1

    def cards_sprites_init(self):
        random.shuffle(self.cards)
        x, y = self.x, self.y
        for i, card in enumerate(self.cards):
            card.reset()
            card.initialize_position(x, y)
            x += self.padx
            if (i+1) % (self.cards_in_lvl/self.rows) == 0:
                x = self.x
                y += self.pady
        self.card_sprites.add(self.cards)
        return self.card_sprites

    # ===== level state =====
    def is_completed(self):
        if len(self.card_sprites.sprites()) == 0:
            self.complete = True
        else:
            self.complete = False
        return self.complete

    