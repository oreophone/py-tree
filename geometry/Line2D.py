"""
A small class used to represent 2D lines for use in terminals.
Supports 2-point, as well as centre/angle representations.
"""

from typing import Tuple, List, Generator, Self
from geometry.Geometry import Geometry
from geometry.Point2D import Point2D
import math
class Line2D(Geometry):
    """
    A 2D line defined by 2 points, designed for terminal use.
    """

    ### UTILS

    def __init__(self,
                 p1: Point2D,
                 p2: Point2D):
        """
        Creats a Line2D instance from 2 points.
        """
        super().__init__() # most likely not required
        self.p1 = p1
        self.p2 = p2
        pass

    def __str__(self):
        return f"{self.p1} --> {self.p2}"

    @classmethod
    def fromPoints(cls,
                   p1: Point2D,
                   p2: Point2D):
        """
        Creates a Line2D instance from 2 points.
        """

        return cls(p1,p2)

    @classmethod
    def fromAngle(cls,
                  c: Point2D,
                  length: float,
                  theta: float,
                  isDegrees: bool = True):
        """
        Creates a Line2D instance from a centre point and an angle 
        (default degrees). Resulting endpoints are an approximation, hence
        `self.getAngle` may return different results.
        """

        p1 = c
        if isDegrees:
            angle = theta * (math.pi / 180)
        else:
            angle = theta

        p2x: float = length * math.cos(angle) + p1.x
        p2y: float = length * math.sin(angle) + p1.y

        p2 = Point2D(p2x,p2y)
        return cls(p1,p2)

    @classmethod
    def fromDiameter(cls,
                     center: Point2D,
                     radius: float,
                     theta: float,
                     isDegrees: bool = True):
        """
        Creates a Line2D instance representing a diameter of a circle with
        a given `center` and `radius`, with angle `theta` (default degrees).

        TODO
        """
        return cls(Point2D.zero(),Point2D.zero())
    
    ### GETTERS 

    def getAngle(self,
                 isDegrees: bool = True,
                 centerIsP1: bool = True) -> float:
        """
        Caclulates the angle of the line (default degrees), with 0 degrees
        pointing right ( --> ). By default, the first point specified `p1` is
        treated as the center.
        """

        lengthX = self.p2.x - self.p1.x
        lengthY = self.p2.y - self.p1.y

        if lengthX == 0:
            angleRads = math.pi/2 if lengthY > 0 else -math.pi/2
        elif lengthY == 0:
            angleRads = math.pi if lengthX < 0 else 0

        angleRads = math.atan(lengthY / lengthX)
        if not centerIsP1:
            angleRads = math.pi - angleRads
        if isDegrees:
            return angleRads * (180 / math.pi)
        return angleRads 

    def getLength(self,
                  returnSquare: bool = False,
                  useTaxicabDistance: bool = False) -> float:
        """
        Calculates the length of the line. If `returnSquare` is true,
        returns the square of the length. If `useTaxicabDistance` is true,
        returns the length in taxicab geometry.
        """

        lengthX = abs(self.p2.x - self.p1.x)
        lengthY = abs(self.p2.x - self.p1.y)
        if useTaxicabDistance:
            return float(lengthX + lengthY)

        lengthSquared = lengthX * lengthX + lengthY * lengthY
        if returnSquare:
            return lengthSquared
        return math.sqrt(lengthSquared)

    def genPoints(self,
                  interval: Tuple[float,float] = (0.0,1.0)
                  )-> Generator[Tuple[int,int]]:
        """
        Generates the points of the line from `p1` to `p2`, for use
        in iterators. If `interval` is provided, returns points on the line
        within that range. Raises an exception if the specified `interval`
        has start/end points outside the range [0,1]. A backwards interval
        (e.g [1,0]) will generate the points in reverse.
        """

        lineRise = int(self.p2.y) - int(self.p1.y)
        lineRun = int(self.p2.x) - int(self.p1.x)
        taxicabDist = abs(lineRise) + abs(lineRun)
        if taxicabDist == 0:
            yield self.p1.toIntegerPoint()
            return

        if interval[0] < 0 or interval[0] > 1:
            raise IndexError(f"""self.genPoints: interval startpoint is outside
                             range! {interval}""")
        if interval[1] < 0 or interval[1] > 1:
            raise IndexError(f"""self.genPoints: interval endpoint is outside
                             range! {interval}""")

        start = interval[0] if interval[0] <= interval[1] else interval[1]
        end = interval[1] if interval[0] <= interval[1] else interval[0]

        yStep = lineRise/taxicabDist
        xStep = lineRun/taxicabDist

        startIndex = math.floor(start * taxicabDist)
        endIndex = math.floor(end * taxicabDist + end)

        if startIndex == endIndex:
            return

        if startIndex > endIndex:
            indexRange = reversed(range(endIndex, startIndex))
        else:
            indexRange = range(startIndex, endIndex)

        for i in indexRange:
            yield (int(self.p1.x + math.floor(xStep * i)),
                   int(self.p1.y + math.floor(yStep * i)))

    def getPoint(self, interval: float) -> Tuple[int,int]:
        """
        Returns the point at the specified `interval` from point 1.
        Returns `p1` if `interval` <= 0, and `p2` if `interval` >= 1.
        """
        
        if interval <= 0:
            return (int(self.p1.x), int(self.p1.y))
        if interval >= 1:
            return (int(self.p2.x), int(self.p2.y))

        lineGen = self.genPoints((interval,1.0))
        return next(lineGen)

    ### COMPARISONS

    def intersects(self, 
                   rhs: Self) -> bool:
        """
        Returns true if the line `rhs` intersects this line. 
        """

        return False # TODO

    def pointDistance(self,
                      point: Point2D,
                      returnSquare: bool = False,
                      useTaxicabDistance: bool = False
                      ) -> float:
        """
        Returns the length of the shortest line from the given `point` 
        to this line. If `useTaxicabDistance` is True, determines the 
        closest point on this line to the `point` and returns the distance
        in taxicab geometry.
        """
        return 0.0 # TODO

    ### MISC

    def extendLine(self,
                   ratioStart: float = 1,
                   ratioEnd: float = 1
                   ) -> None:
        """
        Extends the line in each direction by their respective ratios
        from the centre of the line. For example, setting 
        `ratioStart = ratioEnd = 2` will double the length of the line while
        preserving the centre, whereas `ratioStart = 1, ratioEnd = 3` will
        double the length and set the center to the previous end point. 
        """

        if ratioStart < 0: ratioStart = 0
        if ratioEnd < 0: ratioEnd = 0

        lineRadius = self.getLength() / 2
        rise = (self.p2.y - self.p1.y) / 2
        run = (self.p2.x - self.p1.x) / 2
        centreX = self.p1.x + run
        centreY = self.p1.y + rise
        # p1
        startDelta = (ratioStart - 1) * lineRadius
        p2dx = (-self.p1.x + centreX) * startDelta / lineRadius
        p2dy = (-self.p1.y + centreY) * startDelta / lineRadius
        self.p1 = (self.p1.x - p2dx,
                   self.p1.y - p2dy)
        # p2
        endDelta = (ratioEnd - 1) * lineRadius
        p2dx = (self.p2.x - centreX) * endDelta / lineRadius
        p2dy = (self.p2.y - centreY) * endDelta / lineRadius
        self.p2 = (self.p2.x + p2dx,
                   self.p2.y + p2dy)



        
