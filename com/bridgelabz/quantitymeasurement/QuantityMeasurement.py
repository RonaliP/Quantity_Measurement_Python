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

    def converttemperature(self, temp):

        if temp == Length.CELSIUS:
            return (temp * 9 / 5) + 32
        elif temp == Length.FAHRENHEIT:
            return temp * self.unit / 212
        return False

    def compareTemperatures(self, other):

        if isinstance(self.unit, Length) and isinstance(other.unit, Length):
            return Length.converttemperature(self.unit, self.value) == Length.converttemperature(other.unit, other.value)
        return False

    def addition(self, other):
        return Length.convert(self.unit, self.length) + Length.convert(other.unit, other.length)

class Length(enum.Enum):
    INCH = 1.0
    FEET = 12.0
    YARD = 36.0
    CM=0.4
    GALLON = 3.78
    LITRE = 1
    ML = 0.001
    KG = 1.0
    GRAMS = 0.001
    TONNE = 1000
    FAHRENHEIT = 212
    CELSIUS = 100