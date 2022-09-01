import pygame as pg

class Card(pg.sprite.Sprite):
    def __init__(self, width, height, card_name):
        super().__init__()
        
        # user defined variables
        self.width = width
        self.height = height
        self.name = card_name
        # constants
        self.flip_sprites_size = 37
        self.shrink_sprites_size = 12
        self.enlarge_sprites_size = 11
        self.flip_sprites = [pg.transform.scale(
                pg.image.load(f"Assets/{card_name}/flip-anim/{card_name}{i}.png"),
                (width, height)).convert_alpha() for i in range(1, self.flip_sprites_size+1)]
        self.shrink_sprites = [pg.transform.scale(
                pg.image.load(f"Assets/{card_name}/shrink-anim/{card_name}-shrink{i}.png"),
                (width, height)).convert_alpha() for i in range(1, self.shrink_sprites_size+1)]
        self.enlarge_sprites = [pg.transform.scale(
                pg.image.load(f"Assets/Others/card-enlarge-anim/card-enlarge{i}.png"),
                (width, height)).convert_alpha() for i in range(1, self.enlarge_sprites_size+1)]
        # card state
        self.normal_size_card = self.enlarge_sprites_size-1
        self.card_gone = self.shrink_sprites_size-1
        self.closed_card = [0, self.flip_sprites_size-1]
        self.opened_card = 18
        # animation trigger
        self.is_animating_enlarge = False
        self.is_animating_flip = False
        self.is_animating_shrink = False
        # animation sprite index
        self.current_enlarge_sprite = 0
        self.current_flip_sprite = 0
        self.current_shrink_sprite = 0
        # sprite
        self.image = self.flip_sprites[0]
        self.rect = self.image.get_rect()

    # ===== hovering card =====
    def enlarge(self):
        self.image = pg.transform.scale(self.image, (self.width+10, self.height+10))
        self.rect = self.image.get_rect(x=self.x-5, y=self.y-5)

    def shrink(self):
        self.rect = self.image.get_rect(x=self.x, y=self.y)
        self.image = self.flip_sprites[int(self.current_flip_sprite)]

    # ===== start card animation =====
    def animate_enlarge(self):
        self.is_animating_enlarge = True

    def animate_flip(self):
        self.is_animating_flip = True

    def animate_shrink(self):
        self.is_animating_shrink = True

    # ===== card state ===== 
    def is_normal_size(self):
        return self.current_enlarge_sprite == self.normal_size_card

    def is_close(self):
        return self.current_flip_sprite in self.closed_card

    def is_open(self):
        return self.current_flip_sprite == self.opened_card

    # ===== other functions =====
    def initialize_position(self, pos_x, pos_y):
        self.x, self.y = pos_x, pos_y
        self.rect.x = pos_x
        self.rect.y = pos_y

    def reset(self):
        self.current_enlarge_sprite = 0
        self.current_flip_sprite = 0
        self.current_shrink_sprite = 0
        self.is_animating_flip = False
        self.is_animating_enlarge = False
        self.is_animating_shrink = False
        self.image = self.flip_sprites[0]

    def update(self):
        if self.is_animating_flip:
            self.current_flip_sprite += 1
            self.image = self.flip_sprites[int(self.current_flip_sprite)]

            # stop animation if card is opened or closed
            if self.is_open():
                self.is_animating_flip = False
            elif self.is_close():
                self.current_flip_sprite = 0
                self.is_animating_flip = False
            
        if self.is_animating_shrink:
            self.current_shrink_sprite += 1
            self.image = self.shrink_sprites[int(self.current_shrink_sprite)]

            # stop animation if card is gone
            if self.current_shrink_sprite == self.card_gone:
                self.is_animating_shrink = False
                self.kill()

        if self.is_animating_enlarge:
            self.current_enlarge_sprite += 1
            self.image = self.enlarge_sprites[int(self.current_enlarge_sprite)]

            # stop animation if card is normal size
            if self.is_normal_size():
                self.is_animating_enlarge = False