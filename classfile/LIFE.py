from components._CONSTANT import *

class _LIFE(pg.sprite.Sprite):
    def __init__(self, x , y, word):
        
        # * Init Sprite
        pg.sprite.Sprite.__init__(self)

        # create a font object. 
        # 1st parameter is the font file 
        # which is present in pygame. 
        # 2nd parameter is size of the font 
        self.font = pg.font.Font('freesansbold.ttf', 12) 
        
        # create a text suface object, 
        # on which text is drawn on it. 
        self.text = self.font.render(word , True, GREEN) 
        
        # create a rectangular object for the 
        # text surface object 
        self.textRect = self.text.get_rect(topleft = (x , y)) 

    def update(self, screen , score):
        
        self.text = self.font.render(score , True, GREEN) 
        screen.blit(self.text, self.textRect)

