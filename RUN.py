import sys, math, random
import pygame as pg

from classfile.CONTROL import _CONTROL
from components._CONSTANT import GAMECAPTIONS
from components.TOOLS import load_sprite 

def main():
    # * INIT pygame
    pg.init()

    # TODO : Init mixer // Find soundtrack
    pg.mixer.pre_init(44100, -16, 2, 2048)
    pg.mixer.init()

    # * SET Window's Caption
    pg.display.set_caption(GAMECAPTIONS)

    # TODO : Set Windows's Icon // Find new icon
    icon = load_sprite('icon.png')
    pg.display.set_icon(icon)

    # ! ADD MENU HERE



    # ? AFTER DONE WITH MENU
    # ? IT WILL GO STRAIGHT INTO THE GAME
    control = _CONTROL()
    control.run_loop()

    