import pygame as pg

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
