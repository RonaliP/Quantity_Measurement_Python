import enum
class QuantityMeasurement:
    def __init__(self, unit, length):
        self.unit = unit
        self.length = length

    def __eq__(self, other):
        if isinstance(other, QuantityMeasurement):
            return self.unit == other.unit and other.length == self.length
        if isinstance(self.unit, Length) and isinstance(other.unit, Length):
            if Length.convert(self.unit, self.length) == Length.convert(other.unit, other.length):
                return True
        return False

    def convert(self, length):
        return self.unit * length

    def addition(self, other):
        return Length.convert(self.unit, self.length) + Length.convert(other.unit, other.length)

class Length(enum.Enum):
    INCH = 1.0
    FEET = 12.0
    YARD = 36.0
    CM=0.4

