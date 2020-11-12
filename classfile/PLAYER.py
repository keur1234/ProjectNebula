
import pygame as pg
from components._CONSTANT import *
from components.LOADSPRITE import spr_bluebox
from .SHOT import _SHOT

# TODO : Player class
class _PLAYER(pg.sprite.Sprite):
    def __init__(self):
        # ? Set Player's variable

        # * INIT Sprite
        pg.sprite.Sprite.__init__(self)
        
        # * SET Player's stat
        self.hp = 5;            self.speed = 2
        self.left_limit = LEFT;   self.right_limit = RIGHT;     self.top_limit = TOP;    self.bottom_limit = DOWN
        self.shot_delay = 90;   self.last_shot = pg.time.get_ticks()
        self.radius = 7
        self.frame = 0;     self.frame_rate = 90
        self.last_time = pg.time.get_ticks()

        # * SET Player's object box with image
        self.image = spr_bluebox[self.frame]
        self.rect = self.image.get_rect()
        self.rect.center = (PLAYER_CENTER);     

        # * PLAYER's keys            
        self.key_left = pg.K_LEFT;      self.key_right = pg.K_RIGHT
        self.key_up = pg.K_UP;          self.key_down = pg.K_DOWN
        self.key_shoot = pg.K_z;        # self.key_charge = pg.K_x

        # * ADD Player's Sprite to 'Player Sprite List'
        players.add(self)


    def update(self):
        # now = pg.time.get_ticks()
        # if now - self.last_time > self.frame_rate:
        self.image = spr_bluebox[self.frame]


        # * GET Player's key pressed
        keypressed = pg.key.get_pressed()

        # * 4 Direction [2 button combine = 8 total direction]
        if keypressed[self.key_left] and self.rect.left > self.left_limit:      
            self.rect.x -= self.speed   # ? LEFT
            self.frame = 1
        if keypressed[self.key_right] and self.rect.right < self.right_limit:   
            self.rect.x += self.speed   # ? RIGHT
            self.frame = 2
        if keypressed[self.key_up] and self.rect.top > self.top_limit:          self.rect.y -= self.speed   # ? UP
        if keypressed[self.key_down] and self.rect.bottom < self.bottom_limit:  self.rect.y += self.speed   # ? DOWN

        if not keypressed[self.key_left] and not keypressed[self.key_right]:
            self.frame = 0

        # ? SHOOT'EM
        if keypressed[self.key_shoot]: self.shoot()

    def shoot(self):
        now = pg.time.get_ticks()

        # ? If interval of previous shot and now is more than delay, then shoot.
        if now - self.last_shot > self.shot_delay:    
            self.last_shot = now

            # * CREATE Shot's sprite
            shot1 = _SHOT(self.rect.centerx - 9, self.rect.centery - 41)
            shot2 = _SHOT(self.rect.centerx + 9, self.rect.centery - 41)
            shots.add(shot1 , shot2)
            
            # * ADD Shot's Sprite to all_sprites
            all_sprites.add(shot1, shot2)


    def myPos(self):
        return self.rect.centerx , self.rect.centery