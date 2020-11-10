import pygame as pg
from components._CONSTANT import *
from components.LOADSPRITE import spr_overlay

class _OVERLAY(pg.sprite.Sprite):
    def __init__(self, x , y):

        # * Init Sprite
        pg.sprite.Sprite.__init__(self)

        # * SET image
        self.image = spr_overlay
        self.rect = self.image.get_rect(topleft = (x , y))

        overlays.add( self )