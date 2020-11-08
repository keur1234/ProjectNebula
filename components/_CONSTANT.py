import pygame as pg

# * SYSTEM CONSTANT
GAMECAPTIONS = "Gensokyo"
WIDTH = 640;    HEIGHT = 480
RESOLUTION = (WIDTH, HEIGHT)
FULLSCREEN = False;      FPS = 60
CLOCK = pg.time.Clock()

# * SET to fullscreen or not
if FULLSCREEN: # Yep, Fullscreen plz.
    THISSCREEN = pg.display.set_mode(RESOLUTION , pg.FULLSCREEN)
else: # No, Thanks.
    THISSCREEN = pg.display.set_mode(RESOLUTION)

# * PLAER CONSTANT
CENTER_X_PLAYER = 216;      CENTER_Y_PLAYER = 430
PLAYER_CENTER = (CENTER_X_PLAYER , CENTER_Y_PLAYER)

# * COLOR CONSTANT
BLACK = (0,0,0);      GRAY = (127,127,127);     WHITE = (255,255,255)
RED = (255,0,0);      GREEN = (0,255,0);        BLUE = (0,0,255)

# * GAME VARIABLE
all_sprites = pg.sprite.Group();    backgrounds = pg.sprite.Group()
players = pg.sprite.Group();        shots = pg.sprite.Group()      
enemies = pg.sprite.Group();        bullets = pg.sprite.Group()

