
import pygame as pg
from .PLAYER import _PLAYER
from .BACKGROUD import _BACKGROUND
from .OVERLAY import _OVERLAY
from .ENEMY import _ENEMY
from components._CONSTANT import *
from components.LOADSPRITE import MAP

# ! [CONTROL] Main Pipeline that control every single task
# !           in entire program.
class _CONTROL:
    def __init__(self):
        
        self.screen = THISSCREEN
        self.isFullscreen = FULLSCREEN
        self.RUNNING = True
        self.create_players()
        _BACKGROUND(32, 16, "BLOOD_MOON")
        _OVERLAY(0 , 0)
        _ENEMY(200 , 50 , 0 , 0)

    def create_players(self):

        # * CREATE Player's Sprite
        self.player_1 = _PLAYER()

        # * ADD Player's Sprite to all_sprites_list
        all_sprites.add(self.player_1)


    def run_loop(self):
        while self.RUNNING:
            # * Set Window's Frame per second
            CLOCK.tick(FPS)
            
            # * INPUT listener [Not really input listener]
            for event in pg.event.get():
                # * QUIT GAME
                if event.type == pg.QUIT:
                    self.RUNNING = False

            # TODO : Collide checker [Hit or not]
            hits = pg.sprite.groupcollide(enemies, shots, True, True)
            hits = pg.sprite.groupcollide(players, enemies, True, True, pg.sprite.collide_circle)
            hits = pg.sprite.groupcollide(players, bullets, True, True, pg.sprite.collide_circle)
            
            self.screen.fill(BLACK)
            # * Draw Background / Overlay
            # backgrounds.update(); // Our background don't have to update(No animation)       
            # Well, Have it now.
            backgrounds.update(self.screen);       # backgrounds.draw(self.screen)
            overlays.draw(self.screen)

            # * Draw Every sprite
            all_sprites.update();       all_sprites.draw(self.screen);

            # * Draw Enemy
            enemies.update();       enemies.draw(self.screen)


            pg.display.flip()




