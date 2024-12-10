from geometry.Geometry import Geometry
from Pixel import Pixel
from geometry.Line2D import Line2D
from typing import Generator, List, Tuple

class Drawer:
    """
    The primary class used to generate `Pixel`s to be drawn
    to the terminal, done by combining a `Geometry` with other
    stylistic options like thickness and colour.
    """

    def __init__(self,
                 geometry: Geometry,
                 ):
        pass

    def genPixels(self, **kwargs):
        """
        Creates a generator that outputs `Pixel`'s to be drawn
        to the terminal. The following parameters can be optionally set:
            `thickness=1`: The thickness of the resulting line
            # todo add more
        """
        pass
