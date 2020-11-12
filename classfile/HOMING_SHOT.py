
from .PLAYER import _PLAYER
from components._CONSTANT import *
from components.LOADSPRITE import *

class _HOMING_SHOT(pg.sprite.Sprite):
    def __init__(self, x, y):
        # * Init Sprite
        pg.sprite.Sprite.__init__(self)
        
        # * SET Shot's stat
        self.speed = 0.5
        self.posX = x;      self.posY = y

        # * SET image
        self.image = spr_shot
        self.rect = self.image.get_rect(center = (x, y))

    def update(self , player):
        playerX , playerY = _PLAYER.myPos(player)

        if self.posX < playerX: self.posX += self.speed
        if self.posX > playerX: self.posX -= self.speed
        if self.posY < playerY: self.posY += self.speed
        if self.posY > playerY: self.posY -= self.speed
        self.rect.center = ( int(self.posX) , int(self.posY) )

        # * IF it out of the screen, delete it.
        if self.rect.top >= DOWN or self.rect.left > RIGHT or self.rect.right < LEFT or self.rect.bottom < TOP:
            self.kill()