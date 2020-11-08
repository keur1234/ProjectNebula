import pygame as pg
from components.LOADSPRITE import spr_overlay

class _OVERLAY(pg.sprite.Sprite):
    def __init__(self, x , y):

        pg.sprite.Sprite.__init__(self)

        self.image = spr_overlay
        self.rect = self.image.get_rect(topleft = (x , y))