import pygame as pg

class Button(pg.sprite.Sprite):
    def __init__(self, pos_x, pos_y, width, height, button_name):
        super().__init__()

        self.name = button_name
        self.is_activated = False
        # enlarge button variables
        self.width = width
        self.height = height
        self.x = pos_x
        self.y = pos_y
        # shade button variables
        self.original_image = pg.transform.scale(
            pg.image.load(f"Assets/Others/{button_name}.png"), (width, height))
        try:
            self.shaded_image = pg.transform.scale(
                pg.image.load(f"Assets/Others/{button_name}_shaded.png"), (width, height))
        except FileNotFoundError: self.shaded_image = None
        # sprite
        self.image = self.original_image
        self.rect = self.image.get_rect(x=pos_x, y=pos_y)

    # ===== for shading button animation =====
    def revert_to_original(self):
        self.image = self.original_image

    def shade(self):
        if self.shaded_image is not None:
            self.image = self.shaded_image

    # ===== for enlarging button animation =====
    def enlarge(self):
        self.image = pg.transform.scale(
            self.image, (self.width + 10, self.height + 10)
        )
        self.rect = self.image.get_rect(x=self.x - 5, y=self.y - 5)

    def shrink(self):
        self.image = self.original_image
        self.rect = self.image.get_rect(x=self.x, y=self.y)

    # ===== for activating button =====
    def activate(self):
        self.is_activated = True