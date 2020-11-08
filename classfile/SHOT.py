
from components._CONSTANT import *
from components.LOADSPRITE import *

class _SHOT(pg.sprite.Sprite):
    def __init__(self, x, y):

        # * Init Sprite
        pg.sprite.Sprite.__init__(self)
        
        # * SET Shot's stat
        self.speed = 25

        # * SET image
        self.image = spr_shot
        self.rect = self.image.get_rect();
        
        # * SET where will they appear [x , y]
        self.rect.center = (x, y)

    def update(self):

        # * TRAVEL FROM DOWN TO TOP
        self.rect.y -= self.speed

        # * IF it out of the screen, delete it.
        if self.rect.bottom < 16:
            self.kill()