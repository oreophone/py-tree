class ANSIColour:
    """
    Represents an ANSI256-compatible colour as
    an RGB triple. Includes functions to convert a standard RGB colour
    to the closest valid value.
    """

    def __init__(self,
                 r: int,
                 g: int,
                 b: int):
        if r < 0 or r > 5:
            raise ValueError("ANSIColour: r not in range [0,5]: " + str(r))
        if g < 0 or g > 5:
            raise ValueError("ANSIColour: g not in range [0,5]: " + str(g))
        if b < 0 or b > 5:
            raise ValueError("ANSIColour: b not in range [0,5]: " + str(b))
        self.r = r
        self.g = g
        self.b = b
        self._code = self.getCode()

    @classmethod
    def fromCode(cls,
                 code: int):
        """
        Initialises `ANSIColour` from a raw code in the range [0,255].
        """
        new = cls(0,0,0)
        new._code = code
        new.r = -1
        new.g = -1
        new.b = -1
        return new


    @classmethod
    def fromRGB(cls,
                r: int,
                g: int,
                b: int):
        """
        Initialises `ANSIColour` from an RGB-triple. Values outside the range [0,255] will
        be moved into the range.
        """
        raise NotImplementedError("ANSIColour.fromRGB: Not implemented.")
    

    def getCode(self) -> int:
        """
        Returns the code of this colour as per ANSI specifications.
        """
        if self.r == -1 or self.g == -1 or self.b == -1:
            return self._code

        self._code = 16 + 36 * self.r + 6 * self.g + self.b
        return self._code

    
