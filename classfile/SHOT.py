
from components._CONSTANT import *
from components.LOADSPRITE import *

class _SHOT(pg.sprite.Sprite):
    def __init__(self, x, y):
        # * Init Sprite
        pg.sprite.Sprite.__init__(self)
        
        # * SET Shot's stat
        self.speed = 4
        self.posX = x;      self.posY = y

        # * SET image
        self.image = spr_shot
        self.rect = self.image.get_rect(center = (x, y))

    def update(self):
        self.posY -= self.speed
        self.rect.center = ( self.posX , int(self.posY) )

        # * IF it out of the screen, delete it.
        if self.rect.bottom < TOP: 
            self.kill()