
import pygame as pg
from .PLAYER import _PLAYER
from .BACKGROUD import _BACKGROUND
from .OVERLAY import _OVERLAY
from .ENEMY import _ENEMY
from .TEXT import _TEXT
from .SCORE import _SCORE
from components._CONSTANT import *
from components.LOADSPRITE import MAP

# ! [CONTROL] Main Pipeline that control every single task
# !           in entire program.
class _CONTROL:
    def __init__(self):
        # * Screen
        self.screen = THISSCREEN;   self.isFullscreen = FULLSCREEN
        self.RUNNING = True

        # * Player
        self.myPlayer = _PLAYER();

        # * Init
        _BACKGROUND(32, 16, "BLOOD_MOON");      _OVERLAY(0 , 0)
        _ENEMY(200 , 50 , 0 , 0)
        texts.add(_TEXT(435 , 67, 'Score'));    scores.add(_SCORE(500 , 67, str(self.myPlayer.score)))
        texts.add(_TEXT(435 , 90, 'Life'));    lifes.add(_SCORE(500 , 90, str(self.myPlayer.hp)))

    def run_loop(self):
        while self.RUNNING:
            # * Set Window's Frame per second
            CLOCK.tick(FPS)
            
            # * INPUT listener [Not really input listener]
            keypressed = pg.key.get_pressed()
            if keypressed[pg.K_g]: self.myPlayer.score += 1

            for event in pg.event.get():
                # * QUIT GAME
                if event.type == pg.QUIT:
                    self.RUNNING = False

            # TODO : Collide checker [Hit or not]
            hits = pg.sprite.groupcollide(enemies, shots, True, True)
            
            hits = pg.sprite.groupcollide(players, enemies, True, True, pg.sprite.collide_circle)
            for hit in hits:
                self.myPlayer.hp -= 1
            hits = pg.sprite.groupcollide(players, bullets,  False, True, pg.sprite.collide_circle)
            for hit in hits:
                self.myPlayer.hp -= 1
            # hits = pg.sprite.groupcollide(players, homing_shots, True, True, pg.sprite.collide_circle)
            
            self.screen.fill(BLACK)
            # * Draw Background / Overlay
            # backgrounds.update(); // Our background don't have to update(No animation)       
            # Well, Have it now.
            backgrounds.update(self.screen);        overlays.draw(self.screen)
            texts.update(self.screen);              
            scores.update(self.screen , str(self.myPlayer.score))
            lifes.update(self.screen , str(self.myPlayer.hp))

            # * Draw Every sprite
            players.update();   shots.update()
            all_sprites.draw(self.screen)

            # * Draw Enemy
            enemies.update();   bullets.update()


            pg.display.flip()




