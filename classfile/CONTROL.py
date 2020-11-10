
import pygame as pg
from .PLAYER import _PLAYER
from .BACKGROUD import _BACKGROUND
from .OVERLAY import _OVERLAY
from components._CONSTANT import *
from components.LOADSPRITE import MAP

# ! [CONTROL] Main Pipeline that control every single task
# !           in entire program.
class _CONTROL:
    # def __init__(self):

    def create_players(self):

        # * CREATE Player's Sprite
        self.player_1 = _PLAYER()

        # * ADD Player's Sprite to all_sprites_list
        all_sprites.add(self.player_1)


    def run_loop(self):
        
        self.create_players()

        screen = THISSCREEN
        isFullscreen = FULLSCREEN
        RUNNING = True

        backgrounds.add( _BACKGROUND(32, 16, "GREEN_PALACE") )
        backgrounds.add( _OVERLAY(0 , 0) )

        while RUNNING:
            # * Set Window's Frame per second
            CLOCK.tick(FPS)
            
            # * INPUT listener [Not really input listener]
            for event in pg.event.get():
                # * QUIT GAME
                if event.type == pg.QUIT:
                    RUNNING = False

            # TODO : Collide checker [Hit or not]

            hits = pg.sprite.groupcollide(enemies, shots, True, True)
            hits = pg.sprite.groupcollide(players, enemies, True, True, pg.sprite.collide_circle)
            hits = pg.sprite.groupcollide(players, bullets, True, True, pg.sprite.collide_circle)

            # TODO : Drawing every object
            screen.fill(BLACK)

            # * Draw Background
            backgrounds.update();       
            backgrounds.draw(screen)

            # * Draw Every sprite
            all_sprites.update();        all_sprites.draw(screen);

            # * Draw Enemy
            # spawn.update()

            pg.display.flip()




