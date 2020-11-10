import pygame as pg
from components._CONSTANT import *
from components.LOADSPRITE import MAP

class _BACKGROUND(pg.sprite.Sprite):
    def __init__(self, x, y, NAME_MAP):

        # * Init Sprite
        pg.sprite.Sprite.__init__(self)

        # * SET image
        self.image = MAP[NAME_MAP]
        self.rect = self.image.get_rect(topleft = (x , y))
        self.xPos = x;      self.yPos = 0
        self.mapSpeed = 0.2

        # backgrounds.add( _BACKGROUND(32, 16, "GREEN_PALACE") )
        backgrounds.add( self )

    def update(self, screen):
        self.yPos -= self.mapSpeed
        screen.blit(self.image , (self.xPos , self.yPos))
