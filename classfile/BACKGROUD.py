import pygame as pg
from components.LOADSPRITE import MAP

class _BACKGROUND(pg.sprite.Sprite):
    def __init__(self, x, y, NAME_MAP):

        # * Init Sprite
        pg.sprite.Sprite.__init__(self)

        # ? These commented below used to make a animated background
        # self.list = background_list
        # self.image = self.list[0]
        # self.frame = 0
        # self.frame_rate = 30 * delay
        # self.last_update = pg.time.get_ticks()

        # * SET image
        self.image = MAP[NAME_MAP]
        self.rect = self.image.get_rect(topleft = (x , y))