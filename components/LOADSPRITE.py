import pygame as pg
import os
from .TOOLS import load_sprite
from ._CONSTANT import BLACK , GRAY , WHITE , RED , GREEN, BLUE

# ? Load General Sprites
# sheet_time_tunnel = pg.image.load('data/bck/time_tunnel.png').convert()
# bck_time_tunnel_list=strip_from_sheet(sheet_time_tunnel,(0,0),(288,448),6,3)

pathIMG = os.path.join('data' , 'img')
pathBCK = os.path.join('data' , 'bck')

# * LOAD Overlay image [VISUAL]
spr_overlay = pg.image.load(os.path.join(pathBCK , 'overlay.png')).convert();
spr_overlay.set_colorkey(GREEN)

# * LOAD Background image [VISUAL]
# ? Size = 385 * 445 px
green_palace = pg.image.load(os.path.join(pathBCK , 'green_palace.png')).convert() 
blood_moon = pg.image.load(os.path.join(pathBCK , 'blood_moon.png')).convert() 
MAP = {"GREEN_PALACE":green_palace , "BLOOD_MOON":blood_moon}

# * LOAD Player's sprite [PLAYER]
# ? Size = 16 * 41
spr_bluebox_idle = load_sprite('spr_bluebox.png').convert_alpha()
spr_bluebox_left = load_sprite('spr_bluebox_left.png').convert_alpha()
spr_bluebox_right = load_sprite('spr_bluebox_right.png').convert_alpha()
spr_bluebox = [ spr_bluebox_idle , spr_bluebox_left , spr_bluebox_right]

# sheet_shots=load_sprite('spr_shot.png').convert_alpha()
# spr_shot=strip_from_sheet(sheet_shots,(0,0),(12,55),5)

# * LOAD Shot's sprite [PLAYER]
# ? Size = 12 * 55
spr_shot = load_sprite('spr_shot.png').convert();       spr_shot.set_colorkey(WHITE)

# * LOAD Enemy's sprite [ENEMY]
# ? Size = 38 * 34
spr_enemy = load_sprite('spr_enemy.png').convert_alpha()

# * LOAD Bullet's sprite [ENEMY]
# ? Size = 9 * 9
spr_bullet = load_sprite('spr_bullet.png').convert()
