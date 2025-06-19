from ANSIColour import ANSIColour
from geometry.Geometry import Geometry
from Pixel import Pixel
from geometry.Line2D import Line2D
from typing import Generator, List, Tuple
import random

class Drawer:
    """
    The primary class used to generate `Pixel`s to be drawn
    to the terminal, done by combining a `Geometry` with other
    stylistic options like thickness and colour.

    TEMPLATE METHODS (may be overriden for alternate functionality):
    * `getNextChar`
    * `getNextColour`
    """

    def __init__(self,
                 geometry: Geometry,
                 charPalette: List[str],
                 colourPalette: List[ANSIColour],
                 charWeights: None | List[float] = None,
                 colourWeights: None | List[float] = None,
                 seed: int = -1
                 ):
        self.geometry = geometry
        self.charPalette = charPalette
        self.colourPalette = colourPalette
        if seed == -1:
            self.seed = random.randint(0,2 ** 32 - 1)
        else:
            self.seed = seed

    def genPixels(self, **kwargs) -> Generator[Pixel]:
        """
        Creates a generator that outputs `Pixel`'s to be drawn
        to the terminal. The following parameters can be optionally set:
            `thickness=1`: The thickness of the resulting line
            # todo add more
        """
        pass

    def getNextChar(self) -> str:
        """
        Generates the next character to be drawn. In the default implmentation, chooses
        uniformly randomly from the `charPalette` with weights `charWeights`.
        """
        raise NotImplementedError("Drawer.getNextChar: Not implemented.")
    
    def getNextColour(self) -> ANSIColour:
        """
        Generates the next colour to be used. In the default implementation, chooses uniformly
        randomly from the `colourPalette` with weights `colourWeights`.
        """
        raise NotImplementedError("Drawer.getNextColour: Not implemented.")
