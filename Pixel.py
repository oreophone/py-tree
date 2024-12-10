from typing import Tuple

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



    ### INIT

    def __init__(self,
                 position: Tuple[int,int],
                 ch: str,
                 fg: int = -1, # 0 - 255
                 bg: int = -1, # 0 - 255
                 zLayer: int = 0
                 ):
        self.position = position
        self.ch = ch[0]
        if fg == -1:
            self.fg = None
        else:
            self.fg = fg

        if bg == -1:
            self.bg = None
        else:
            self.bg = bg

        self.zLayer = zLayer

    def __str__(self) -> str:
        return Pixel.FG(self.fg) + Pixel.BG(self.bg) + self.ch + Pixel.R

    ### COLOURS

    @staticmethod
    def rgbToAnsi(r: int, g: int, b: int) -> int:
        """
        Approximates the given RGB colour in the ansi-256 colour scheme.
        """
        return 0
