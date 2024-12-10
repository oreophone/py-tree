from Geometry import Geometry
from Line2D import Line2D
from typing import Generator, List, Tuple, Self

class Curve2D(Geometry):
    """
    A smooth curve built from a series of quadratic
    Bezier curves, designed for terminal use. Built from three main
    components:
        `points`: A list of `n` points in 2D space.
        `curveStart`: A point representing the midpoint of the first
        bezier curve.
        `curveStrengths`: A list of `n - 2` non-negative floats representing
        the strengths of each subsequent curve. These will be combined with
        `curveStart` to calculate each midpoint in a way that gives the
        smoothest combined curve possible.
    """
    def __init__(self,
                 points: List[Tuple[float,float]], # n
                 curveStart: Tuple[float,float], # 1
                 curveStrengths: List[float] # n - 2
                 ):
        super().__init__() 
        self.points = points
        self.curveStart = curveStart
        self.curveStrengths = curveStrengths
        self.calculateCurvePoints()

        pass

    def calculateCurvePoints(self):
        """
        Used by the initialiser to calculate the set of midpoints for
        each quadratic bezier curve.
        """
        self.curvePoints = [self.curveStart]
        for i in range(len(self.points) - 2):
            curPoint = self.points[i + 1]
            curCurvePt = self.curvePoints[-1]
            curStrength = self.curveStrengths[i]
            tangent = Line2D(curCurvePt, curPoint)
            tangent.extendLine(1,1 + curStrength)
            self.curvePoints.append(tangent.p2)

    ### HELPERS

    @staticmethod
    def quadraticBezier(p1: Tuple[int,int],
                        mid: Tuple[int,int],
                        p2: Tuple[int,int],
                        scaleForInterval: bool = True
                        ):
        """
        Returns a lambda function that takes a float `t` and returns
        the quadratic bezier curve defined by points `p1, mid, p2` at time `t`.
        If `scaleForInterval` (def. True) is true, adjusts the formula so that
        it returns the point dividing the curve with ratio `t:1-t`.
        """

        pass
    ### GEOMETRY

    def genPoints(self,
                  interval: Tuple[float,float] = (0.0,1.0)
                  ) -> Generator[Tuple[int,int]]:
        raise NotImplementedError("Curve2D.genPoints: Not implemented.")

    def getPoints(self,
                  interval: Tuple[float,float] = (0.0,1.0)
                  ) -> List[Tuple[int,int]]:
        raise NotImplementedError("Curve2D.getPoints: Not implemented.")

    def getPoint(self,
                 interval: float
                 ) -> Tuple[int, int]:
        raise NotImplementedError("Curve2D.getPoint: Not implemented.")
