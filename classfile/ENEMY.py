import pygame as pg
from .BULLET import _BULLET
from components._CONSTANT import *
from components.LOADSPRITE import *
from .HOMING_SHOT import _HOMING_SHOT

class _ENEMY(pg.sprite.Sprite):
    def __init__(self, x ,y, SpdX , SpdY):

        # * Init Sprite
        pg.sprite.Sprite.__init__(self)

        # * SET Enemy's stat
        self.speed = 1
        self.speedX = SpdX;        self.speedY = SpdY  
        self.left_limit = LEFT;   self.right_limit = RIGHT;     self.top_limit = TOP;    self.bottom_limit = DOWN
        self.shot_delay = 80;  self.last_shot = pg.time.get_ticks()
        self.radius = 17
        self.frame = 0;     self.frame_rate = 90
        self.last_update = pg.time.get_ticks()
        self.pattern = 0

        # * SET Enemy's image
        self.image = spr_enemy[self.frame]
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

        # * SET ENEMY'S Key
        self.key_left = pg.K_a;     self.key_right = pg.K_d
        self.key_up = pg.K_w;       self.key_down = pg.K_s
        self.key_shoot = pg.K_f;    # self.key_charge = pg.K_x
        
        # * ADD Enemy's Sprite to 'Enemy Sprite List'
        enemies.add(self)

    def update(self):
        '''now = pg.time.get_ticks()
        if now - self.last_update > self.frame_rate:
            self.frame += 1
            self.frame %= 2
            self.image = spr_enemy[self.frame]
        '''
        self.rect.x += self.speedX
        self.rect.y += self.speedY
        # * IF it out of the screen, delete it.
        if (self.rect.top >= self.bottom_limit or 
                self.rect.left > self.right_limit or 
                self.rect.right < self.left_limit or 
                self.rect.bottom < self.top_limit):
            self.kill()

        keypressed = pg.key.get_pressed()

        if keypressed[self.key_left] and self.rect.left > self.left_limit:      self.rect.x -= self.speed   # ? LEFT
        if keypressed[self.key_right] and self.rect.right < self.right_limit:   self.rect.x += self.speed   # ? RIGHT
        if keypressed[self.key_up] and self.rect.top > self.top_limit:          self.rect.y -= self.speed   # ? UP
        if keypressed[self.key_down] and self.rect.bottom < self.bottom_limit:  self.rect.y += self.speed   # ? DOWN

        if keypressed[self.key_shoot]:
            self.shoot()
    
    def shoot(self):

        # * CHECK Delay
        now = pg.time.get_ticks()
        # if now - self.last_shot > self.shot_delay and self.pattern != 360:
        if now - self.last_shot > self.shot_delay:    
            self.last_shot = now

            #bullet1 = _BULLET(x = self.rect.centerx , y = self.rect.centery, speed = 1)

            #bullets.add(bullet1)

            #all_sprites.add(bullet1)
            
            for i in range(3):
                bullet1 = _BULLET(self.rect.centerx , self.rect.centery, (i * 15) + self.pattern, 1)
                bullets.add(bullet1)
                all_sprites.add(bullet1)
            for i in range(12,15):
                bullet1 = _BULLET(self.rect.centerx , self.rect.centery, (i * 15) + self.pattern, 1)
                bullets.add(bullet1)
                all_sprites.add(bullet1)

            self.pattern += 15
            
            #homing = _HOMING_SHOT(self.rect.centerx , self.rect.centery)
            #homing_shots.add(homing)
    '''
    def death(self):
        self.remove(all_sprites)
        nowEnemy = pg.time.get_ticks()
        if nowEnemy - self.death_time > 60:
            self.death_time = nowEnemy
            self.kill()
    '''
    