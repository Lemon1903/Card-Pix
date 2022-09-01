import pygame as pg


class Timer(pg.sprite.Sprite):
    def __init__(self, pos_x, pos_y, width, height):
        super().__init__()

        # constants
        self.one_second = 1000
        self.sprites_size = 61
        self.sprites = [pg.transform.scale(
                pg.image.load(f"Assets/timer/timer-bar{i}.png"),
                (width, height)) for i in range(1, self.sprites_size + 1)]
        # timer state
        self.times_up = False
        self.is_paused = False
        self.no_time = self.sprites_size - 1
        self.current_sprite = 0
        # time checking
        self.current_time = pg.time.get_ticks()
        self.previous_time = 0
        self.time_solved = 0
        # sprite
        self.image = self.sprites[0]
        self.rect = self.image.get_rect(x=pos_x, y=pos_y)

    # ===== timer state =====
    def pause(self):
        self.is_paused = True

    def resume(self):
        self.is_paused = False
        
    # ===== update timer =====
    def add_time(self, time_added):
        # add time to timer
        if self.current_sprite <= time_added: 
            self.current_sprite = 0
        else:
            self.current_sprite -= time_added
        # check time added if greater than time solved
        if self.time_solved <= time_added:
            self.time_solved = 0
        else:
            self.time_solved -= time_added
        self.image = self.sprites[self.current_sprite]

    def reset(self):
        self.current_sprite = 0
        self.image = self.sprites[0]
        self.time_solved = 0
        self.times_up = False

    def update(self):
        if not self.times_up or not self.is_paused:
            self.current_time = pg.time.get_ticks()
            time_diff = self.current_time - self.previous_time
            if time_diff >= self.one_second:
                self.time_solved += 1
                self.current_sprite += 1
                self.previous_time = self.current_time
                self.image = self.sprites[self.current_sprite]
                if self.current_sprite == self.no_time:
                    self.current_sprite = 0
                    self.times_up = True