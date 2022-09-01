import sys, pygame as pg

display_surf = pg.display.set_mode((500, 500))
clock = pg.time.Clock()

class Card(pg.sprite.Sprite):
    def __init__(self, pos, size):
        super().__init__()
        self.x, self.y = pos[0], pos[1]
        self.w, self.h = size[0], size[1]
        self.orig_image = pg.transform.scale(pg.image.load(
            "Assets/pineapple-card/flip-anim/pineapple-card1.png"), size).convert_alpha()
        self.image = self.orig_image
        self.rect = self.image.get_rect(topleft=pos)

    def enlarge(self):
        self.image = pg.transform.scale(self.orig_image, (self.w + 10, self.h + 10))
        self.rect.topleft = (self.x - 5, self.y - 5)

    def shrink(self):
        self.image = self.orig_image
        self.rect.topleft = (self.x, self.y)

    def update(self, mouse_pos):
        if self.rect.collidepoint(mouse_pos):
            self.enlarge()
        else:
            self.shrink()

def main():
    card1 = Card((50, 50), (150, 150))
    card2 = Card((200, 50), (150, 150))
    card_sprites = pg.sprite.Group(card1)

    while True:
        clock.tick(60)
        mouse_pos = pg.mouse.get_pos()
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()

        display_surf.fill((255, 255, 255))
        card_sprites.draw(display_surf)
        card_sprites.update(mouse_pos)
        pg.display.update()

if __name__ == "__main__":
    main()