from typing import Tuple, List, Generator

class Geometry(object):
    """
    An abstract class that holds the basic methods required
    by `Drawer` for use in the terminal.
    """

    def genPoints(self,
                  interval: Tuple[float,float] = (0.0,1.0)
                  ) -> Generator[Tuple[int,int]]:
        raise NotImplementedError("Geometry.genPoints: Not implemented.")

    def getPoints(self,
                  interval: Tuple[float,float] = (0.0,1.0)
                  ) -> List[Tuple[int,int]]:
        raise NotImplementedError("Geometry.getPoints: Not implemented.")

    def getPoint(self,
                 interval: float
                 ) -> Tuple[int, int]:
        raise NotImplementedError("Geometry.getPoint: Not implemented.")
