from Geometry import Geometry
from typing import Generator, List, Tuple, Self

class Circle2D(Geometry):
    """
    A circle defined by a center and radius, designed
    for terminal use.
    """

    def __init__(self):
        super().__init__()
        pass

    # TODO everything

    ### GEOMETRY

    def genPoints(self,
                  interval: Tuple[float,float] = (0.0,1.0)
                  ) -> Generator[Tuple[int,int]]:
        raise NotImplementedError("Circle2D.genPoints: Not implemented.")

    def getPoints(self,
                  interval: Tuple[float,float] = (0.0,1.0)
                  ) -> List[Tuple[int,int]]:
        raise NotImplementedError("Circle2D.getPoints: Not implemented.")

    def getPoint(self,
                 interval: float
                 ) -> Tuple[int, int]:
        raise NotImplementedError("Circle2D.getPoint: Not implemented.")
