from typing import Tuple, Literal

class Point2D:
    """
    A point in 2D space, designed for terminal use.
    """

    def __init__(self,
                 x: float,
                 y: float):
        self.x = x
        self.y = y

    @classmethod
    def zero(cls):
        return cls(0,0)
    
    @classmethod
    def sum(cls, *args):
        """
        Returns the sum of the given `Point2D`s as a new `Point2D`. Any non-point arguments are ignored.
        """
        x = 0
        y = 0

        for v in args:
            if type(v) != Point2D:
                continue
            x += v.x
            y += v.y

        return cls(x,y)


    def add(self, *args):
        """
        Adds the given `Point2D`s to this one in place. Any non-point arguments are ignored.
        """
        for v in args:
            if type(v) != Point2D:
                continue
            self.x += v.x
            self.y += v.y

    def scale(self, scalar: float):
        """
        Scales the `Point2D` by the given `scalar`.
        """
        self.x *= scalar
        self.y *= scalar

    def toIntegerPoint(self,
                       roundType: Literal["floor", "round", "ceil"] = "round") -> Tuple[int,int]:
        """
        Returns the closest integer point to this `Point2D`. the method of rounding `roundType` may
        be set to one of "floor", "round", or "ceil" (default "round").
        """
        if roundType == "round":
            return (round(self.x),round(self.y))
        elif roundType == "floor":
            return (int(self.x), int(self.y))
        elif roundType == "ceil":
            return (int(-(-self.x // 1)), int(-(-self.y // 1))) ## ceil
        else:
            return ValueError("Point2D.toIntegerPoint: invalid roundType (" + roundType + ")")
    
    ## OVERRIDES

    def __eq__(self, value: object) -> bool:
        if type(value) != Point2D:
            return False
        return value.x == self.x and value.y == self.y
    
    def __add__(self, other: object): # -> Self
        if type(other) != Point2D:
            raise ValueError("Point2D.__add__: type of other value is not Point2D")
        
        return Point2D.sum(self,other)
    
    def __iadd__(self, other: object):
        if type(other) != Point2D:
            raise ValueError("Point2D.__iadd__: type of other value is not Point2D")
        
        self.add(other)
    