import pygame as pg
from components._CONSTANT import *
from components.LOADSPRITE import *

class _ENEMY(pg.sprite.Sprite):
    def __init__(self, x ,y, spdX, spdY):

        # * Init Sprite
        pg.sprite.Sprite.__init__(self)

        # * SHOOT Delay
        self.delay = 300
        self.last_shot = pg.time.get_ticks()

        # self.frame = 0;     self.frame_rate = 90
        # self.last_update = pg.time.get_ticks()

        # * SET Enemy's image
        self.image = spr_enemy
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

        # * SET Enemy's hitbox radius
        self.radius = 10

        # * SET SPEED
        self.speed = 5

        # * HOW LEFT & RIGHT PLAYER can go
        self.left_limit = 31;       self.right_limit = 417

        # * SET ENEMY'S Key
        self.key_left = pg.K_a;      self.key_right = pg.K_d
        self.key_up = pg.K_w;          self.key_down = pg.K_s
        self.key_shoot = pg.K_x;        # self.key_charge = pg.K_x

        # * RANDOM SPEED X, Y so they look more lively
        self.speedX = spdX # random.randint(-4 , 4)
        self.speedY = spdY # random.randint(1 , 3)
        
        # FIXED SPEED
        # self.speedX = 2
        # self.speedY = 2

        # self.pattern = 5

        enemies.add(self)

    def update(self):
        
        # ? Do not need to update the same image
        # ? EXCEPT! if there some animation.
        # self.image = self.image

        # * GET Player's key pressed
        keypressed = pg.key.get_pressed()

        # * 4 Direction [2 button combine = 8 total direction]
        if keypressed[self.key_left] and self.rect.left > self.left_limit:
            # print("Left")
            self.rect.x -= self.speed
        if keypressed[self.key_right] and self.rect.right < self.right_limit:
            # print("Right")
            self.rect.x += self.speed
        if keypressed[self.key_up] and self.rect.top > 16:
            # print("Up")
            self.rect.y -= self.speed
        if keypressed[self.key_down] and self.rect.bottom < 461:
            # print("Down")
            self.rect.y += self.speed            

        # * TRAVEL FROM TOP TO DOWN
        # self.rect.x += self.speedX
        # self.rect.y += self.speedY
        
        # * IF it out of the screen, delete it.
        if self.rect.top >= 470 or self.rect.left > 420 or self.rect.right < 40 or self.rect.bottom < 16:
            self.kill()

        # * SHOOT bullet
        if keypressed[self.key_shoot]:     
            # print("Shoot")
            self.shoot()
    '''
    def shoot(self):

        # * CHECK Delay
        now = pg.time.get_ticks()
        if now - self.last_shot > self.delay:
            self.last_shot = now

            bullet1 = _BULLET(x = self.rect.centerx , y = self.rect.centery, speed = 1)

            bullets.add(bullet1)

            all_sprites.add(bullet1)
            for i in range(12):
                bullet1 = _BULLET(x = self.rect.centerx , y = self.rect.centery, angle = (i * 15) + self.pattern, speed = 1)

                bullets.add(bullet1)

                all_sprites.add(bullet1)
            
            self.pattern = (self.pattern + 99) % 360
            
    def death(self):
        self.remove(all_sprites)
        nowEnemy = pg.time.get_ticks()
        if nowEnemy - self.death_time > 60:
            self.death_time = nowEnemy
            self.kill()
    '''
    