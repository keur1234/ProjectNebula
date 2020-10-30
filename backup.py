class Game:
    screen = None
    aliens = []
    bullets = []
    lost = False

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.screen = pg.display.set_mode( (width, height) )
        self.clock = pg.time.Clock()
        done = False
        
        hero = Hero(self, width / 2, height - 20, 5) 
        generator = Generator(self, 1)
        bullet = None

        while not done:
            if len(self.aliens) == 0:
                self.displayText("VICTORY ACHIEVED")

            pressed = pg.key.get_pressed()
            if pressed[pg.K_LEFT] and pressed[pg.K_UP]:
                hero.x -= hero.speedX if hero.x > 20 else 0
                hero.y -= hero.speedY if hero.y > 20 else 0
            elif pressed[pg.K_RIGHT] and pressed[pg.K_UP]:
                hero.x += hero.speedX if hero.x < width - 20 else 0
                hero.y -= hero.speedY if hero.y > 20 else 0
            elif pressed[pg.K_LEFT] and pressed[pg.K_DOWN]:
                hero.x -= hero.speedX if hero.x > 20 else 0
                hero.y -= hero.speedY if hero.y > 20 else 0
            elif pressed[pg.K_RIGHT] and pressed[pg.K_DOWN]:
                hero.x += hero.speedX if hero.x < width - 20 else 0
                hero.y += hero.speedY if hero.y < height - 20 else 0
            elif pressed[pg.K_LEFT]:
                hero.x -= hero.speedX if hero.x > 20 else 0
            elif pressed[pg.K_RIGHT]:
                hero.x += hero.speedX if hero.x < width - 20 else 0
            elif pressed[pg.K_UP]:
                hero.y -= hero.speedY if hero.y > 20 else 0
            elif pressed[pg.K_DOWN]:
                hero.y += hero.speedY if hero.y < height - 20 else 0

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    done = True
                if event.type == pg.KEYDOWN and event.key == pg.K_SPACE:
                    self.bullets.append(Bullet(self, hero.x, hero.y))

            
            pg.display.flip()
            self.clock.tick(60)
            self.screen.fill( (0, 0, 0) ) # Fill with white

            for alien in self.aliens:
                alien.draw()
                alien.checkCollision(self)
                if(alien.y > height):
                    self.lost = True
                    done = True
                    self.displayText("YOU DIED")

            for bullet in self.bullets:
                bullet.draw()

            if not self.lost: 
                hero.draw()

    def displayText(self, text):
        pg.font.init()
        font = pg.font.SysFont('Arial', 50)
        text = font.render(text, False, (44, 0, 62))
        self.screen.blit(text, (110, 160))

class Alien:
    def __init__(self, game, x, y, speed):
        self.x = x
        self.game = game
        self.y = y
        self.speedX = speed
        self.speedY = speed
        self.size = 10
    
    def draw(self):
        pg.draw.rect(self.game.screen, (255, 0, 0), pg.Rect(self.x, self.y, self.size, self.size))
        self.y += self.speedY

    def checkCollision(self, game):
        for bullet in game.bullets:
            if(bullet.x < self.x + self.size and 
                    bullet.x > self.x - self.size and
                    bullet.y < self.y + self.size and
                    bullet.y > self.y - self.size):
                game.bullets.remove(bullet)
                game.aliens.remove(self)

class Hero:
    def __init__(self, game, x, y, speed):
        self.x = x
        self.game = game
        self.y = y
        self.speedX = speed
        self.speedY = speed
    

    def draw(self):
        pg.draw.rect(self.game.screen, (0, 255, 0), pg.Rect(self.x, self.y, 8, 8))

class Generator: 
    def __init__(self, game, speed):
        margin = 30
        width = 15
        for x in range(margin, game.width - margin, width):
            for y in range(margin, int(game.height / 2), width):
                game.aliens.append(Alien(game, x, y, speed))

class Bullet:
    def __init__(self, game, x, y) -> None:
        self.x = x
        self.y = y
        self.game = game

    def draw(self):
        pg.draw.rect(self.game.screen, (0, 255, 255), pg.Rect(self.x, self.y, 2, 4) )

        self.y -= 10


if __name__ == '__main__':

    import sys
    import pygame as pg

    pg.init()
    game = Game(480, 640)
    pg.quit()
    sys.exit()

