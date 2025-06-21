from typing import Tuple
from display.ANSIColour import ANSIColour

class Pixel:
    """
    Used to represent the values of each pixels drawn to the terminal,
    e.g. position, character, color. 
    """

    ### CONSTANTS
    E = "\033[" # ] vim keeps on indenting open brackets ):
    R = E + "0m"
    FG = lambda x: Pixel.E + f"38;5;{x}m" if x != None else ""
    BG = lambda x: Pixel.E + f"48;5;{x}m" if x != None else ""
    FG_DEFAULT = ANSIColour(5,5,5) # white
    BG_DEFAULT = ANSIColour.fromCode(0) # transparent


    ### INIT

    def __init__(self,
                 position: Tuple[int,int],
                 ch: str,
                 fg: ANSIColour = FG_DEFAULT,
                 bg: ANSIColour = BG_DEFAULT, 
                 zLayer: int = 0
                 ):
        self.position = position
        self.ch = ch[0]
        self.fg = fg
        self.bg = bg
        self.zLayer = zLayer

    def __str__(self) -> str:
        return Pixel.FG(self.fg.getCode()) + Pixel.BG(self.bg.getCode()) + self.ch + Pixel.R
    
