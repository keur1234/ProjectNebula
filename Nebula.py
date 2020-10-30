import pygame
'''

---- # TODO

= # ! Review your code
= # ! Add enemy 
= # ! Read how enemy bullet pattern work

= # TODO
= # ! Used some json or txt or some text file to used as a script
  # ! to make a stage or boss

'''

'''
---- # ? VARIABLE

= # ! SHOT is PLAYER's bullet
= # ! while BULLET is ENEMY & BOSS's bullet

= # !!! CONSTANT <-> UPPER CASE
  # !!! CLASS NAME <-> NORMAL CASE / FLEXIBLE
  # !!! METHOD NAME <-> LOWER CASE / FLEXIBLE

'''

def main():
    
    # * SET Constant
    WIDTH = 640;    HEIGHT = 480
    RESOLUTION = (WIDTH, HEIGHT)

    CENTER_X_PLAYER = 216;      CENTER_Y_PLAYER = 430
    PLAYER_CENTER = (CENTER_X_PLAYER , CENTER_Y_PLAYER)
    
    FPS = 60

    # * SET COLOR
    BLACK=(0,0,0);      GRAY=(127,127,127);     WHITE=(255,255,255)
    RED=(255,0,0);      GREEN=(0,255,0);        BLUE=(0,0,255)

    # ? Setting
    FULLSCREEN = False
    
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

    # * INIT pygame
    pg.init()

    # TODO : Init mixer
    pg.mixer.pre_init(44100, -16, 2, 2048)
    pg.mixer.init()

    # * SET Window's Caption
    pg.display.set_caption("Gensokyo")
    
    # TODO : Set Windows's Icon
    icon = load_sprite('icon.png')
    pg.display.set_icon(icon)
    
    # * SET to fullscreen or not
    if FULLSCREEN: # Yep, Fullscreen plz.
        screen = pg.display.set_mode(RESOLUTION , pg.FULLSCREEN)
    else: # No, Thanks.
        screen = pg.display.set_mode(RESOLUTION)

    # * SET Window's Clock 
    CLOCK = pg.time.Clock()

    # ? Load General Sprites

    
    # sheet_time_tunnel = pg.image.load('data/bck/time_tunnel.png').convert()
    # bck_time_tunnel_list=strip_from_sheet(sheet_time_tunnel,(0,0),(288,448),6,3)

    # * LOAD Overlay image [VISUAL]
    spr_overlay = pg.image.load('data/bck/overlay.png').convert();
    spr_overlay.set_colorkey(GREEN)

    # * LOAD Background image [VISUAL]
    # ? Size = 385 * 445 px
    green_palace = pg.image.load('data/bck/green_palace.png').convert() 

    # // LOAD Player's hitbox [PLAYER]
    # // spr_hitbox = load_sprite('spr_hitbox.png').convert_alpha()
    
    # * LOAD Player's sprite [PLAYER]
    # ? Size = 16 * 41
    spr_bluebox = load_sprite('spr_bluebox.png').convert_alpha()

    # sheet_shots=load_sprite('spr_shot.png').convert_alpha()
    # spr_shot=strip_from_sheet(sheet_shots,(0,0),(12,55),5)

    # * LOAD Shot's sprite [PLAYER]
    # ? Size = 12 * 55
    spr_shot = load_sprite('spr_shot.png').convert()
    spr_shot.set_colorkey(WHITE)

    # * LOAD Enemy's sprite [ENEMY]
    # ? Size = 38 * 34
    spr_enemy = load_sprite('spr_enemy.png').convert_alpha()

    # * LOAD Bullet's sprite [ENEMY]
    # ? Size = 9 * 9
    spr_bullet = load_sprite('spr_bullet.png').convert()


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

            # * CREATE Player's Sprite
            self.player_1 = _PLAYER()

            # * ADD Player's Sprite to all_sprites_list
            all_sprites.add(self.player_1)
        
    
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


    class _SHOT(pg.sprite.Sprite):
        def __init__(self, x, y):

            # * Init Sprite
            pg.sprite.Sprite.__init__(self)
            
            # * SET Shot's stat
            self.speed = 25

            # * SET image
            self.image = spr_shot
            self.rect = self.image.get_rect();
            
            # * SET where will they appear [x , y]
            self.rect.center = (x, y)

        def update(self):

            # * TRAVEL FROM DOWN TO TOP
            self.rect.y -= self.speed

            # * IF it out of the screen, delete it.
            if self.rect.bottom < 16:
                self.kill()

    class _BACKGROUND(pg.sprite.Sprite):
        def __init__(self, x, y, NAME_MAP):

            # * Init Sprite
            pg.sprite.Sprite.__init__(self)

            # ? These commented below used to make a animated background
            # self.list = background_list
            # self.image = self.list[0]
            # self.frame = 0
            # self.frame_rate = 30 * delay
            # self.last_update = pg.time.get_ticks()

            # * SET image
            self.image = MAP[NAME_MAP]
            self.rect = self.image.get_rect(topleft = (x , y))

        '''
        def update(self):
            self.image = self.image
            
            self.image = self.list[self.frame]    
            now = pg.time.get_ticks()
            if now - self.last_update > self.frame_rate:
                self.last_update = now
                self.frame += 1
                if self.frame == len(self.list):
                    self.image = self.list[0]
                    self.frame = 0
            
        '''
    class _OVERLAY(pg.sprite.Sprite):
        def __init__(self, x , y):

            pg.sprite.Sprite.__init__(self)

            self.image = spr_overlay
            self.rect = self.image.get_rect(topleft = (x , y))

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

        def shoot(self):

            # * CHECK Delay
            now = pg.time.get_ticks()
            if now - self.last_shot > self.delay:
                self.last_shot = now

                bullet1 = _BULLET(x = self.rect.centerx , y = self.rect.centery, speed = 1)

                bullets.add(bullet1)

                all_sprites.add(bullet1)
                '''
                for i in range(12):
                    bullet1 = _BULLET(x = self.rect.centerx , y = self.rect.centery, angle = (i * 15) + self.pattern, speed = 1)

                    bullets.add(bullet1)

                    all_sprites.add(bullet1)
                
                self.pattern = (self.pattern + 99) % 360
                '''
        '''
        def death(self):
            self.remove(all_sprites)
            nowEnemy = pg.time.get_ticks()
            if nowEnemy - self.death_time > 60:
                self.death_time = nowEnemy
                self.kill()
        '''
    '''
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
            if nowSpawn - self.spawn_new > 10 and self.counter < 20:
                self.spawn_new = nowSpawn
                self.counter += 1
                self.spawn()

        def spawn(self):
            spawnX = random.randint(40 , 450);      spawnY = 30
            enemy = _ENEMY(spawnX , spawnY)
            all_sprites.add(enemy)
            enemies.add(enemy)
    '''

    class _SPAWN_ENEMY(pg.sprite.Sprite):
        def __init__(self):
            pg.sprite.Sprite.__init__(self)

            self.image = pg.Surface( (1 , 1) )
            self.rect = self.image.get_rect()

        def spawn(self, x , y, spdX , spdY):
            
            enemy = _ENEMY(x , y , spdX , spdY)
            all_sprites.add(enemy)
            enemies.add(enemy)

    class _BULLET(pg.sprite.Sprite):
        def __init__(self , x , y , speed):
        # def __init__(self , x , y , angle, speed):
            pg.sprite.Sprite.__init__(self)

            self.speed = 3

            self.radius = 2

            self.image = spr_bullet
            self.rect = self.image.get_rect()

            self.rect.center = (x , y)

            # angle = math.radians( -angle )

            self.speedX = self.speed
            self.speedY = self.speed

            # self.speedX = speed * math.cos(angle)
            # self.speedY = speed * math.sin(angle)

            self.posX = x
            self.posY = y

        def update(self):

            # self.rect.y += self.speed
            # self.posX += self.speedX
            self.posY += self.speedY
            self.rect.center = ( int(self.posX) , int(self.posY) )

            if self.rect.top >= 470 or self.rect.left > 420 or self.rect.right < 40 or self.rect.bottom < 16:
                self.kill()

    # ? Something [Maybe Define all variable]
    
    all_sprites = pg.sprite.Group()

    backgrounds = pg.sprite.Group()

    
    MAP = {"GREEN_PALACE":green_palace}
    backgrounds.add( _BACKGROUND(32, 16, "GREEN_PALACE") )
    backgrounds.add( _OVERLAY(0 , 0) )

    players = pg.sprite.Group();    shots = pg.sprite.Group()      
    enemies = pg.sprite.Group();    bullets = pg.sprite.Group()

    control = CONTROL()
    control.create_players()

    
    # spawn = SpawnEnemy()
    # spawn.spawn()

    spawnSC = _SPAWN_ENEMY()
    spawnSC.spawn(x = 200, y = 200, spdX = 0, spdY = 0)

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
