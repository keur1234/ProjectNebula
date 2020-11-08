
import pygame as pg
from components._CONSTANT import *
from components.LOADSPRITE import *
from .SHOT import _SHOT

# TODO : Player class
class _PLAYER(pg.sprite.Sprite):
    def __init__(self):
        # ? Set Player's variable

        # * INIT Sprite
        pg.sprite.Sprite.__init__(self)
        
        # * SET Player's sprite
        self.image = spr_bluebox

        # * SET Player's stat
        self.hp = 5
        self.speed = 8

        # * Delay each Shot
        
        self.shot_delay = 500 # 90
        self.last_shot = pg.time.get_ticks()

        # ? READ pygame.mask
        # self.mask = pg.mask.from_surface(spr_hitbox)

        # * SET Player hitbox radius
        self.radius = 10        

        # * SET Player's object box with image
        self.rect = self.image.get_rect()
        self.rect.center = (PLAYER_CENTER);     

        # * HOW LEFT & RIGHT PLAYER can go
        self.left_limit = 31;       self.right_limit = 417

        # * PLAYER's keys            
        self.key_left = pg.K_LEFT;      self.key_right = pg.K_RIGHT
        self.key_up = pg.K_UP;          self.key_down = pg.K_DOWN
        self.key_shoot = pg.K_z;        # self.key_charge = pg.K_x

        # * ADD Player's Sprite to players_sprite_list
        players.add(self)


    def update(self):
        
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

        # * SHOOT'EM
        if keypressed[self.key_shoot]:     
            # print("Shoot")
            self.shoot()


        # self.draw_hitbox()
    '''
    def draw_hitbox(self):
        hitbox = spr_hitbox
        hitbox_rect = hitbox.get_rect(center = self.rect.center)
        screen.blit(hitbox, hitbox_rect)
    '''
    def shoot(self):
        # print("Shooting")
        now = pg.time.get_ticks()

        # * CHECK Delay
        # ? If interval of previous shot and now is more than delay, then shoot.
        if now - self.last_shot > self.shot_delay:    
            self.last_shot = now

            # * CREATE Shot's sprite
            shot1 = _SHOT(self.rect.centerx - 9, self.rect.centery - 41)
            shot2 = _SHOT(self.rect.centerx + 9, self.rect.centery - 41)

            # * ADD Shot's Sprite to shots_sprite_list
            shots.add(shot1 , shot2)

            # * ADD Shot's Sprite to all_sprites
            all_sprites.add(shot1, shot2)