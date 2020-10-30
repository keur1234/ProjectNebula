import pygame
'''

---- # TODO

= # ! Review your code
= # ! Add enemy 
= # ! Read how enemy bullet pattern work

'''

def main():
    
    # *** SET Constant [SYSTEM]
    
    # * RESOLUTION
    WIDTH = 640;    HEIGHT = 480
    RESOLUTION = (WIDTH, HEIGHT)

    # * PLAYER's CENTER location 
    CENTER_X_PLAYER = 216;      CENTER_Y_PLAYER = 430
    PLAYER_CENTER = (CENTER_X_PLAYER , CENTER_Y_PLAYER)
    
    # * Frame per second
    FPS = 60

    # ? Window's setting
    # * FULLSCREEN Boolean
    FULLSCREEN = False

    # TODO : Find some proper 'icon' and 'caption'
    ICON = "icon.png";       CAPTION = "Gensokyo"

    # * COLOR
    BLACK=(0,0,0);      GRAY=(127,127,127);     WHITE=(255,255,255)
    RED=(255,0,0);      GREEN=(0,255,0);        BLUE=(0,0,255)

    # *** SET Tool's function

    # TODO : For Load Image
    def load_sprite(image):
        img = pg.image.load("data/img/" + image)
        return img

    # TODO : For Load SFX
    def load_sound(sound):
        snd = pg.mixer.Sound("data/sfx" + sound)
        return snd
    
    # ! For Load sprite [Strip each sprite from sheet]
    def strip_from_sheet(sheet, start, size, columns, rows=1):
        sprites_list = []
        for j in range(rows):
            for i in range(columns):
                location=( start[0] + size[0] * i , start[1] + size[1] * j )
                sprites_list.append(sheet.subsurface(pg.Rect(location, size)))
        return sprites_list

    # *** SET SYSTEM's setting

    # * INIT pygame [SYSTEM]
    pg.init()

    # TODO : Init mixer
    pg.mixer.pre_init(44100, -16, 2, 2048)
    pg.mixer.init()

    # * SET Window's Caption [SYSTEM]
    pg.display.set_caption(CAPTION)
    
    # * Set Windows's Icon [SYSTEM]
    icon = load_sprite(ICON)
    pg.display.set_icon(icon)
    
    # * SET Fullscreen or not [SYSTEM]
    if FULLSCREEN: # Yep, Fullscreen plz.
        screen = pg.display.set_mode(RESOLUTION , pg.FULLSCREEN)
    else: # No, Thanks.
        screen = pg.display.set_mode(RESOLUTION)

    # * SET Window's Clock [SYSTEM]
    CLOCK = pg.time.Clock()

    # ? Load General Sprites

    # ! VISUAL -> PLAYER -> ENEMY
    
    # *** LOAD VISUAL's stuff
    # * LOAD Background image [VISUAL]
    # ? Size = 385 * 445 px
    green_palace = pg.image.load('data/bck/green_palace.png').convert() 

    # *** LOAD PLAYER's stuff

    # * LOAD Player's hitbox [PLAYER]
    spr_hitbox = load_sprite('spr_hitbox.png').convert_alpha()
    
    # * LOAD Player's sprite [PLAYER]
    spr_bluebox = load_sprite('spr_bluebox.png').convert_alpha()

    # ! Example of strip 'Whole sprite' to each smaller sprite
    # sheet_shots=load_sprite('spr_shot.png').convert_alpha()
    # spr_shot=strip_from_sheet(sheet_shots,(0,0),(12,55),5)

    # * LOAD Shot's sprite [PLAYER]
    # ? Size = 12 * 55 px
    spr_shot = load_sprite('spr_shot.png').convert_alpha()

    # sheet_time_tunnel = pg.image.load('data/bck/time_tunnel.png').convert()
    # bck_time_tunnel_list=strip_from_sheet(sheet_time_tunnel,(0,0),(288,448),6,3)

    # *** LOAD ENEMY's stuff

    # * LOAD Enemy's sprite [ENEMY]
    spr_enemy = load_sprite('spr_enemy.png').convert_alpha()


    '''
    # This area is to load every prepared

    # Load GUI

    # Load Player Title

    # Load General Sprites

    # Load Sprite Sheets

    # Sprite sheets to sprites

    # Load backgrounds

    # Load Boss backgrounds

    # Load Boss foregrounds

    # Load sounds

    # Define some functions

    # Define Classes [Lots of lot of lot of class]
    .
    .
    .
    # Create sprite
    
    # Load music
    pg.mixer.music.load("data/bgm/main.ogg")
    pg.mixer.music.play(loop = -1)

    # Load control
    control = CONTROL()

    # Menu arrow
    menuarrow = MenuArrow()

    # Selection screen
    selection = SelectionScreen()

    '''
    
    # TODO : Define Classes [Lots of lot of lot of class]
    
    # ! [CONTROL] Main Pipeline that control every single task
    # !           in entire program.
    class CONTROL:
        def __init__(self):
            self.screen = 0

        def create_players(self):
            self.player_1 = Player()
            all_sprites.add(self.player_1)
        
    
    # TODO : Player class
    class Player(pg.sprite.Sprite):
        def __init__(self):
            # ? Set Player's variable

            # * INIT Sprite
            pg.sprite.Sprite.__init__(self)
            
            # * SET Player's sprite
            self.image = spr_bluebox

            # * SET Player's stat
            self.hp = 5
            self.speed = 8
            self.shot_delay = 90
            self.last_shot = pg.time.get_ticks()

            self.mask = pg.mask.from_surface(spr_hitbox)
            
            self.rect = self.image.get_rect()
            self.left_limit = 31;       self.right_limit = 417
            self.rect.center = (PLAYER_CENTER);     

            self.key_left = pg.K_LEFT;      self.key_right = pg.K_RIGHT
            self.key_up = pg.K_UP;          self.key_down = pg.K_DOWN
            self.key_shoot = pg.K_z;        # self.key_charge = pg.K_x

            # * ADD Player's Sprite to players_sprite_list
            players.add(self)


        def update(self):
            keypressed = pg.key.get_pressed()
            if keypressed[self.key_left] and self.rect.left > self.left_limit:
                print("Left")
                self.rect.x -= self.speed
            if keypressed[self.key_right] and self.rect.right < self.right_limit:
                print("Right")
                self.rect.x += self.speed
            if keypressed[self.key_up] and self.rect.top > 16:
                print("Up")
                self.rect.y -= self.speed
            if keypressed[self.key_down] and self.rect.bottom < 461:
                print("Down")
                self.rect.y += self.speed
            if keypressed[self.key_shoot]:     
                print("Shoot")
                self.shoot()
            self.draw_hitbox()

        def draw_hitbox(self):
            hitbox = spr_hitbox
            hitbox_rect = hitbox.get_rect(center = self.rect.center)
            screen.blit(hitbox, hitbox_rect)

        def shoot(self):
            print("Shooting")
            now = pg.time.get_ticks()
            if now - self.last_shot > self.shot_delay:    
                self.last_shot = now
                shot1 = Shot(self.rect.centerx - 9, self.rect.centery)
                shot2 = Shot(self.rect.centerx + 9, self.rect.centery)
                shots.add(shot1 , shot2)
                all_sprites.add(shot1, shot2)


    class Shot(pg.sprite.Sprite):
        def __init__(self, x, y):

            # * Init Sprite
            pg.sprite.Sprite.__init__(self)
            
            self.speed = 25

            self.image = spr_shot
            self.rect = self.image.get_rect();
            self.rect.center = (x, y)

        def update(self):
            self.rect.y -= self.speed
            if self.rect.bottom < 16:
                self.kill()

    class Background(pg.sprite.Sprite):
        def __init__(self, background_list, x = 0, y = 0, delay = 1):

            # * Init Sprite
            pg.sprite.Sprite.__init__(self)

            # self.list = background_list
            # self.image = self.list[0]
            self.image = green_palace
            self.rect = self.image.get_rect(topleft = (x , y))
            # self.frame = 0
            # self.frame_rate = 30 * delay

            # self.last_update = pg.time.get_ticks()


        def update(self):
            self.image = self.image
            '''
            self.image = self.list[self.frame]    
            now = pg.time.get_ticks()
            if now - self.last_update > self.frame_rate:
                self.last_update = now
                self.frame += 1
                if self.frame == len(self.list):
                    self.image = self.list[0]
                    self.frame = 0
            '''


    class Enemy(pg.sprite.Sprite):
        def __init__(self, x ,y):

            # * Init Sprite
            pg.sprite.Sprite.__init__(self)


            self.frame = 0;     self.frame_rate = 90
            self.last_update = pg.time.get_ticks()
            self.image = spr_enemy
            self.rect = self.image.get_rect()
            self.rect.center = (x, y)
            self.radius = 4
            # self.speedX = 2
            # self.speedY = 2
            self.speedX = random.randint(0 , 7)
            self.speedY = random.randint(1 , 7)

        def update(self):
            self.image = self.image
            self.rect.x += self.speedX
            self.rect.y += self.speedY
            
            if self.rect.top >= 470 or self.rect.left > 420:
                self.kill()
        
        def death(self):
            self.remove(all_sprites)
            nowEnemy = pg.time.get_ticks()
            if nowEnemy - self.death_time > 60:
                self.death_time = nowEnemy
                self.kill()

    class SpawnEnemy(pg.sprite.Sprite):
        def __init__(self):

            # * Init Sprite
            pg.sprite.Sprite.__init__(self)

            
            self.image = pg.Surface((1 , 1))
            self.rect = self.image.get_rect()
            
            self.spawn_new = pg.time.get_ticks()
            self.counter = 0


        def update(self):
            nowSpawn = pg.time.get_ticks()
            if nowSpawn - self.spawn_new > 10 and self.counter < 1000:
                self.spawn_new = nowSpawn
                self.counter += 1
                self.spawn()

        def spawn(self):
            enemy = Enemy(70, 70)
            all_sprites.add(enemy)
            enemies.add(enemy)



    # ? Something [Maybe Define all variable]
    
    all_sprites = pg.sprite.Group()


    backgrounds = pg.sprite.Group()
    backgrounds.add(Background(None, 32, 16))

    shots = pg.sprite.Group()
    players = pg.sprite.Group()
    
    control = CONTROL()
    control.create_players()

    enemies = pg.sprite.Group()

    spawn = SpawnEnemy()
    # spawn.spawn()

    # * Define that game is still running.
    RUNNING = True

    # * Main loop
    while RUNNING:
        # * Set Window's Frame per second
        CLOCK.tick(FPS)

        # TODO : Main input listener
        for event in pg.event.get():
            
            # * QUIT GAME
            if event.type == pg.QUIT:
                RUNNING = False
            
            # * Player hit some key
            elif event.type == pg.KEYDOWN: # * Player hit some 'key'
                mod_bitmask = pg.key.get_mods()
                # ? If player hit 'ALT + ENTER' -> [FULLSCREEN]
                # ? or hit 'ALT + F4' -> [QUIT GAME]
                if mod_bitmask & pg.KMOD_ALT: # * Player hit 'ALT'
                    if event.key == pg.K_RETURN:
                        if FULLSCREEN: # * Set to 'Windows'
                            screen = pg.display.set_mode(RESOLUTION) 
                            FULLSCREEN = False 
                        else: # * Set to 'Fullscreen'
                            screen = pg.display.set_mode(RESOLUTION, pg.FULLSCREEN)
                            FULLSCREEN = True
                    elif event.key == pg.K_F4: # * QUIT GAME
                        RUNNING = False

           
            # players.update()


        # TODO : Collide checker [Hit or not]




        # TODO : Drawing every object
        screen.fill(BLACK)

        # * Draw Background
        backgrounds.update();       backgrounds.draw(screen)
        
        # * Draw Every sprite
        all_sprites.update();        all_sprites.draw(screen);

        # spawn.update()

        pg.display.flip()




















'''

class Game:
    # Defualt value

    def __init__(self):
        print("hello")




class Player:
    
    def __init__(self):

        
class Enemy:

    def __init__(self):

'''


if __name__ == '__main__':
    
    # TODO : Import
    import sys, math, random
    import pygame as pg

    pg.init()

    main()

    pg.quit()
    sys.exit()    
