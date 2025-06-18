from typing import Tuple, List, Generator

class Geometry(object):
    """
    An abstract class that holds the basic methods required
    by `Drawer` for use in the terminal.

    ABSTRACT METHODS:
    * `genPoints`
    * `getPoints`
    * `getPoint`
    """

    def genPoints(self,
                  interval: Tuple[float,float] = (0.0,1.0)
                  ) -> Generator[Tuple[int,int]]:
        """
        Returns an iterator that generates the points of this path within the specified `interval`.

        Required to be implemented by all subclasses.
        """
        raise NotImplementedError("Geometry.genPoints: Not implemented.")

    def getPoints(self,
                  interval: Tuple[float,float] = (0.0,1.0)
                  ) -> List[Tuple[int,int]]:
        """
        Returns a list of points on this path within the specified `interval`.

        Required to be implemented by all subclasses.
        """
        raise NotImplementedError("Geometry.getPoints: Not implemented.")

    def getPoint(self,
                 interval: float
                 ) -> Tuple[int, int]:
        """
        Returns the point on this path at the given `interval`.

        Required to be implemented by all subclasses.
        """
        raise NotImplementedError("Geometry.getPoint: Not implemented.")
