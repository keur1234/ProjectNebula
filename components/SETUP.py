from .TOOLS import *
from ._CONSTANT import *

def __init__():
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

