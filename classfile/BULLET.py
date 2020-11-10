import math
from components._CONSTANT import *
from components.LOADSPRITE import *

class _BULLET(pg.sprite.Sprite):
    # def __init__(self , x , y , speed):
    def __init__(self , x , y , angle, speed):
        pg.sprite.Sprite.__init__(self)

        # * SET Bullet's stat
        self.speed = 3;     self.radius = 2
        self.speedX = self.speed;   self.speedY = self.speed
        self.posX = x;      self.posY = y
        # * SET image
        self.image = spr_bullet
        self.rect = self.image.get_rect()
        self.rect.center = (x , y)

        angle = math.radians( -angle )
        self.speedX = speed * math.cos(angle)
        self.speedY = speed * math.sin(angle)


    def update(self):
        self.posX += self.speedX
        self.posY += self.speedY
        self.rect.center = ( int(self.posX) , int(self.posY) )

        if self.rect.top >= DOWN or self.rect.left > RIGHT or self.rect.right < LEFT or self.rect.bottom < TOP:
            self.kill()