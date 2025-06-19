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
        if len(charPalette) == 0:
            raise ValueError("Drawer: empty charPalette")
        if len(colourPalette) == 0:
            raise ValueError("Drawer: empty colourPalette")
        if charWeights is not None and len(charWeights) != len(charPalette):
            raise ValueError("Drawer: lengths of charWeights and charPalette do not match")
        if colourWeights is not None and len(colourWeights) != len(colourPalette):
            raise ValueError("Drawer: lengths of colourWeights and colourPalette do not match")

        self.geometry = geometry
        self.charPalette = charPalette
        self.colourPalette = colourPalette
        self.charWeights = charWeights
        self.colourWeights = colourWeights

        if seed == -1:
            self.seed = random.randint(0,2 ** 32 - 1)
        else:
            self.seed = seed

        # private RNG
        self._rng = random.Random(self.seed)

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
        if len(self.charPalette) == 1:
            return self.charPalette[0]
        return self._rng.choices(self.charPalette, self.charWeights)[0]

    
    def getNextColour(self) -> ANSIColour:
        """
        Generates the next colour to be used. In the default implementation, chooses uniformly
        randomly from the `colourPalette` with weights `colourWeights`.
        """
        if len(self.colourPalette) == 1:
            return self.colourPalette[0]
        return self._rng.choices(self.colourPalette, self.colourWeights)[0]
