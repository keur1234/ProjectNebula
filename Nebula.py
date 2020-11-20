def main():

    # * SET Constant
    GAMECAPTIONS = "Gensokyo"
    FPS = 144
    WIDTH = 640;    HEIGHT = 480
    RESOLUTION = (WIDTH, HEIGHT)

    CENTER_X_PLAYER = 216;  CENTER_Y_PLAYER = 430
    PLAYER_CENTER = (CENTER_X_PLAYER, CENTER_Y_PLAYER)
    LEFT = 31;  RIGHT = 417;    TOP = 16;   DOWN = 461
    KEY_LEFT = pg.K_LEFT;   KEY_RIGHT = pg.K_RIGHT;     
    KEY_UP = pg.K_UP;       KEY_DOWN = pg.K_DOWN
    KEY_SHOOT = pg.K_z;     KEY_CHARGE = pg.K_x
    KEY_ENTER = pg.K_RETURN;    KEY_ESCAPE = pg.K_ESCAPE

    # * SET COLOR
    BLACK = (0, 0, 0);  GRAY = (127, 127, 127);     WHITE = (255, 255, 255)
    RED = (255, 0, 0);  GREEN = (0, 255, 0);        BLUE = (0, 0, 255)

    # ? Setting
    RUNNING = True;     CLOCK = pg.time.Clock()
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
                location = (start[0] + size[0] * i, start[1] + size[1] * j)
                sprites_list.append(sheet.subsurface(pg.Rect(location, size)))
        return sprites_list

    # * INIT pygame
    pg.init()

    # * SET Window's Caption / Window's Icon
    icon = load_sprite('icon.png'); pg.display.set_icon(icon)
    pg.display.set_caption("Gensokyo")

    # TODO : Init mixer
    pg.mixer.pre_init(44100, -16, 2, 2048); pg.mixer.init()

    # * SET to fullscreen or not
    if FULLSCREEN: screen = pg.display.set_mode(RESOLUTION, pg.FULLSCREEN)
    else: screen = pg.display.set_mode(RESOLUTION)

    # ? Load General Sprites
    # * LOAD CHARACTER's Portrait [VISUAL]
    port_rd = pg.image.load('data/img/red_stickman.png');   port_rd.set_colorkey(BLACK)
    port_gr = pg.image.load('data/img/green_stickman.png');   port_gr.set_colorkey(BLACK)

    # * LOAD CURSOR [SYSTEM]
    gui_main = pg.image.load('data/gui/main.png').convert();    gui_main_rect = gui_main.get_rect()
    gui_cursor = pg.image.load('data/gui/cursor.png').convert();    gui_cursor.set_colorkey(WHITE)
    gui_cursor_char_sel = pg.image.load('data/gui/gui_cursor_p1.png').convert();   gui_cursor_char_sel.set_colorkey(WHITE)
    #gui_select = pg.image.load('data/gui/selection.png').convert_alpha()
    #gui_select_rect = gui_select.get_rect(center = (WIDTH // 2, HEIGHT // 2))
    gui_char_sel = pg.image.load('data/gui/character_selection.png').convert();    gui_char_sel_rect = gui_char_sel.get_rect()
    gui_skill_sel = pg.image.load('data/gui/skill_selection.png').convert();    gui_skill_sel.set_colorkey(WHITE)

    # * LOAD Overlay image [VISUAL]
    spr_overlay = pg.image.load('data/bck/overlay.png').convert();  spr_overlay.set_colorkey(GREEN)

    # * LOAD Background image [VISUAL]
    # ? Size = 385 * 445 px
    green_palace = pg.image.load('data/bck/green_palace.png').convert()
    blood_moon = pg.image.load('data/bck/blood_moon.png').convert()
    character_background = pg.image.load('data/bck/character_background.png').convert()

    # * LOAD Player's sprite [PLAYER]
    # ? Size = 16 * 41
    spr_bluebox_idle = load_sprite('spr_bluebox.png').convert();        spr_bluebox_idle.set_colorkey(WHITE)
    spr_bluebox_left = load_sprite('spr_bluebox_left.png').convert();   spr_bluebox_left.set_colorkey(WHITE)
    spr_bluebox_right = load_sprite('spr_bluebox_right.png').convert(); spr_bluebox_right.set_colorkey(WHITE)
    spr_bluebox = [spr_bluebox_idle, spr_bluebox_left, spr_bluebox_right]

    # * LOAD Shot's sprite [PLAYER]
    # ? Size = 12 * 55
    spr_shot = load_sprite('spr_shot.png').convert();   spr_shot.set_colorkey(WHITE)

    # * LOAD Enemy's sprite [ENEMY]
    # ? Size = 38 * 34
    spr_enemy1 = load_sprite('spr_enemy.png').convert();    spr_enemy1.set_colorkey(GREEN)
    spr_enemy2 = load_sprite('spr_enemy.png').convert();    spr_enemy2.set_colorkey(GREEN)
    spr_enemy = [spr_enemy1, spr_enemy2]

    # * LOAD Bullet's sprite [ENEMY]
    # ? Size = 9 * 9
    spr_bullet = load_sprite('spr_bullet.png').convert();   spr_bullet.set_colorkey(WHITE)

    class _Control:
        def __init__(self):
            self.screen = 0

        def create_players(self):
            self.player = _Player()
            all_sprites.add(self.player)

    class _MenuArrow(pg.sprite.Sprite):
        def __init__(self):
            pg.sprite.Sprite.__init__(self)
            self.image = gui_cursor
            self.rect = self.image.get_rect()
            self.options = 0

        def update(self):
            if self.options > 2: self.options = 0
            if self.options < 0: self.options = 2
            if self.options == 0: self.rect.center = (417, 260)
            elif self.options == 1: self.rect.center = (417, 343)
            elif self.options == 2: self.rect.center = (417, 430)

        def enter(self):
            if self.options == 0: # ? GAME START
                control.screen += 1
                character_screen = _Background(character_background , 0 , 0)
                backgrounds.add(character_screen)
                self.kill()
            elif self.options == 2: # ? EXIT
                exit()
    
    class _SelectionScreen:
        def __init__(self):
            pg.sprite.Sprite.__init__(self)
            self.player_1_index = 0
            self.chooseSkill = False
            self.ready = False

        def update(self):
            if control.screen == 1:
                if not self.ready:
                    self.ready = True
                    self.charselcursor = _CursorCharSel(377, 393)
            if self.charselcursor.hasChosen:
                if not self.chooseSkill:
                    self.chooseSkill = True
                    self.skillcursor = _CursorSkillSel(38, 226)

        def start(self):
            #self.charselcursor.kill();  self.skillcursor.kill()
            backgrounds.empty();    all_sprites.empty()
            control.create_players()
            backgrounds.add( _Background(blood_moon , 32 , 16) )
            # self.testspawn=TestSpawn()

    class _CursorCharSel(pg.sprite.Sprite):
        def __init__(self, x, y):
            pg.sprite.Sprite.__init__(self)
            all_sprites.add(self)
            self.image = gui_cursor_char_sel
            self.rect = self.image.get_rect(topleft = (x , y))
            self.options = 0
            self.hasChosen = False
            self.update_timer = pg.time.get_ticks()

        def update(self):
            if self.options > 1: self.options = 0
            if self.options < 0: self.options = 1
            if self.options == 0:   
                screen.blit(port_rd, (0 , 0))
                text = _TEXT(400 , 400, 'Red stickman' , 20, RED);     
                screen.blit(text.texts , text.textRect)
            elif self.options == 1:	
                screen.blit(port_gr, (0 , 0))
                text = _TEXT(400 , 400, 'Green stickman' , 20, GREEN);    
                screen.blit(text.texts , text.textRect)
            
        def choose(self):
            self.hasChosen = True

        def unchoose(self):
            self.hasChosen = False
    
    class _CursorSkillSel(pg.sprite.Sprite):
        def __init__(self , x , y):
            pg.sprite.Sprite.__init__(self)
            all_sprites.add(self)
            self.image = gui_skill_sel
            self.rect = self.image.get_rect(topleft = (x , y))
            self.options = 0;
            self.update_timer = pg.time.get_ticks()

        def update(self):
            if self.options > 2: self.options = 0
            if self.options < 0: self.options = 1
            if self.options == 0:   
                screen.blit(gui_cursor, (38 , 249))
            elif self.options == 1:	
                screen.blit(gui_cursor, (38 , 337))
            elif self.options == 2:
                screen.blit(gui_cursor, (38 , 425))

            now = pg.time.get_ticks()
            if now - self.update_timer > 100:
                self.update_timer = now

                keystate = pg.key.get_pressed()
                if keystate[KEY_UP]:        self.options -= 1
                elif keystate[KEY_DOWN]:    self.options += 1
                elif keystate[KEY_SHOOT] or keystate[KEY_ENTER]:
                    control.screen = 2
                    selection.start()
                    self.kill()

    class _Player(pg.sprite.Sprite):
        def __init__(self):
            # * INIT Sprite
            pg.sprite.Sprite.__init__(self)

            # * SET Player's stat
            self.hp = 5;    self.speed = 2;     self.radius = 1
            self.shot_delay = 90;   self.last_shot = pg.time.get_ticks()
            self.frame = 0

            # * SET Player's object box with image
            self.image = spr_bluebox[self.frame]
            self.rect = self.image.get_rect(center=(PLAYER_CENTER))
            self.left_limit = LEFT;     self.right_limit = RIGHT;   
            self.top_limit = TOP;       self.bottom_limit = DOWN

            # * PLAYER's keys
            self.key_left = KEY_LEFT;       self.key_right = KEY_RIGHT
            self.key_up = KEY_UP;           self.key_down = KEY_DOWN
            self.key_shoot = KEY_SHOOT;     self.key_charge = KEY_CHARGE

            # * ADD Player's Sprite to 'Player Sprite List'
            players.add(self)

        def update(self):
            # * GET Player's key pressed
            keypressed = pg.key.get_pressed()
            
            # * Render frame
            self.image = spr_bluebox[self.frame]
            if keypressed[self.key_left] and self.rect.left > self.left_limit:  
                self.rect.x -= self.speed  # ? LEFT
                self.frame = 1
            if keypressed[self.key_right] and self.rect.right < self.right_limit:   
                self.rect.x += self.speed  # ? RIGHT
                self.frame = 2
            if keypressed[self.key_up] and self.rect.top > self.top_limit:  self.rect.y -= self.speed  # ? UP
            if keypressed[self.key_down] and self.rect.bottom < self.bottom_limit:  self.rect.y += self.speed  # ? DOWN
            if not keypressed[self.key_left] and not keypressed[self.key_right]:
                self.frame = 0
            
            if keypressed[self.key_shoot]: self.shoot()

        def shoot(self):
            now = pg.time.get_ticks()

            # * If interval of previous shot and now is more than delay, then shoot.
            if now - self.last_shot > self.shot_delay:
                self.last_shot = now

                # * CREATE Shot's sprite
                shot1 = _Shot(self.rect.centerx - 9, self.rect.centery - 41);    shots.add(shot1)
                shot2 = _Shot(self.rect.centerx + 9, self.rect.centery - 41);    shots.add(shot2)

                # * ADD Shot's Sprite to all_sprites
                all_sprites.add(shot1, shot2)

    class _Shot(pg.sprite.Sprite):
        def __init__(self, x, y):
            # * Init Sprite
            pg.sprite.Sprite.__init__(self)

            # * SET Shot's stat
            self.speed = 4
            self.posX = x;  self.posY = y

            # * SET image
            self.image = spr_shot
            self.rect = self.image.get_rect(center = (x, y))

        def update(self):
            self.posY -= self.speed
            self.rect.center = (int(self.posX), int(self.posY))

            # * IF it out of the screen, delete it.
            if self.rect.bottom < TOP:  self.kill()

    class _StartSpawn(pg.sprite.Sprite):
        def __init__(self):
            pg.sprite.Sprite.__init__(self)
            self.image = pg.Surface( (32 , 16) )
            self.rect = self.image.get_rect()





    class _Background(pg.sprite.Sprite):
        def __init__(self, name_map, x, y):
            pg.sprite.Sprite.__init__(self)
            self.image = name_map
            self.rect = self.image.get_rect(topleft = (x , y))
            self.xPos = x;      self.yPos = -890
            self.mapSpeed = 0.225
    
        def update(self):
            self.yPos += self.mapSpeed
            screen.blit(self.image , (self.xPos , self.yPos))
            if self.yPos >= 0:
                self.yPos = -890

    
    class _Overlay(pg.sprite.Sprite):
        def __init__(self, x , y):
            # * Init Sprite
            pg.sprite.Sprite.__init__(self)

            # * SET image
            self.image = spr_overlay
            self.rect = self.image.get_rect(topleft = (x , y))

    class _TEXT(pg.sprite.Sprite):
        def __init__(self, x , y, word, size , color):
            
            # * Init Sprite
            pg.sprite.Sprite.__init__(self)
            self.font = pg.font.Font('freesansbold.ttf', size) 
            self.texts = self.font.render(word , True, color) 
            self.textRect = self.texts.get_rect(topleft = (x , y)) 

    #spritegroups creations
    all_sprites = pg.sprite.Group();    backgrounds = pg.sprite.Group();    overlays = pg.sprite.Group()
    players = pg.sprite.Group();        shots = pg.sprite.Group()

    #first object placement
    control = _Control()
    menuarrow = _MenuArrow()
    selection = _SelectionScreen()
    all_sprites.add(menuarrow)

    while RUNNING:
        CLOCK.tick(FPS)
        for event in pg.event.get():
            if event.type == pg.QUIT: RUNNING = False
            elif event.type == pg.KEYDOWN:
                if control.screen==0:
                    if event.key == KEY_UP:     menuarrow.options -= 1  # ? UP
                    if event.key == KEY_DOWN:   menuarrow.options += 1  # ? DOWN
                    if event.key == KEY_SHOOT or event.key == KEY_ENTER:  menuarrow.enter()
                elif control.screen == 1:   # ? SELECT CHARACTER
                    if not selection.charselcursor.hasChosen:    
                        if event.key == KEY_LEFT:   selection.charselcursor.options -= 1
                        if event.key == KEY_RIGHT:  selection.charselcursor.options += 1
                        if event.key == KEY_SHOOT:  selection.charselcursor.choose()
                    else:
                        if event.key == KEY_CHARGE:	selection.charselcursor.unchoose()
                    if event.key == KEY_CHARGE or event.key == KEY_ESCAPE:
                        control.screen = 0
                        menuarrow = _MenuArrow();    all_sprites.add(menuarrow)
                        backgrounds.empty()
                        if selection.chooseSkill:
                            selection.skillcursor.kill()
                        selection.charselcursor.kill()
                        selection.ready = False; selection.chooseSkill = False
        
        # drawing functions
        screen.fill(BLACK)
        backgrounds.update();   
        if control.screen == 0:
            screen.blit(gui_main, gui_main_rect)
        elif control.screen == 1:
            selection.update()
            screen.blit(gui_char_sel, gui_char_sel_rect)
        elif control.screen == 2:
            screen.blit(spr_overlay, (0 , 0))
        all_sprites.update();   all_sprites.draw(screen)
        pg.display.flip()




if __name__ == '__main__':

    # TODO : Import
    import sys, math, random
    import pygame as pg

    pg.init()

    main()

    pg.quit()
    sys.exit()