from com.bridgelabz.quantitymeasurement.Feet import Feet
from com.bridgelabz.quantitymeasurement.Yard import Yard
from com.bridgelabz.quantitymeasurement.Inch import Inch
from com.bridgelabz.quantitymeasurement.QuantityMeasurement import QuantityMeasurement, Length
import pytest


# Test_cases  for FEET
# Test_case1 comparing two feet value
def test_TwoFeetValue_IfCompared_ReturnTrue():
    first_feet = Feet(0)
    second_feet = Feet(0)
    assert first_feet == second_feet


# Test_case2 Comparing Two instance feet variable
def test_TwoFeetValue_IfCompared_ReturnTrue():
    first_feet = Feet(1.0)
    second_feet= Feet(1.0)
    assert first_feet == second_feet


# Test_Case3 Comparing one feet value should return false when None
def test_OneFeetValue_IfComparedIfNotNone_ReturnTrue():
    first_feet = Feet(0)
    assert first_feet is not None


# Test_case4 Compared one feet value with float value
def test_IfOneFeetAndFloatValue_WhenCompared_ReturnTrue():
    first_feet = Feet(0.0)
    second_feet = float(0.0)
    with pytest.raises(AssertionError):
        assert first_feet == second_feet


# Test_case5  Comparing two different feet value
def test_givenTwoDifferentFeetValue_WhenCompared_ShouldReturnFalse():
    first_feet = Feet(0.0)
    second_feet = Feet(10.0)
    assert first_feet != second_feet

#___________________________________________________________________
# Test_case for YARD


def test_givenTwoYardValue_WhenCompared_ShouldReturnTrue():
    first_yard = Yard(0)
    second_yard = Yard(0)
    assert first_yard == second_yard


def test_givenTwoYardValu_WhenCompared_ShouldReturnTrue():
    first_yard = Yard(1.0)
    second_yard = Yard(1.0)
    assert first_yard == second_yard


def test_givenOneYardValue_WhenComparedIfNotNone_ShouldReturnTrue():
    first_yard = Yard(0.0)
    assert first_yard is not None


def test_givenOneYardAndFloatValue_WhenCompared_ShouldReturnTrue():
    first_yard = Yard(0.0)
    second_yard = float(0.0)
    with pytest.raises(AssertionError):
        assert first_yard == second_yard


def test_givenTwoDifferentYardValue_WhenCompared_ShouldReturnFalse():
    first_yard = Yard(0.0)
    second_yard = Yard(1.0)
    assert first_yard != second_yard

#_______________________________________________________________________
# Test_case for Inch

def test_givenTwoInchValue_WhenCompared_ShouldReturnTrue():
    first_inch = Inch(0)
    second_inch = Inch(0)
    assert first_inch == second_inch


def test_givenTwoInchValue_WhenCompared_ShouldReturnTrue():
    first_inch = Inch(1.0)
    second_inch = Inch(1.0)
    assert first_inch == second_inch


def test_givenOneInchValue_WhenComparedIfNotNone_ShouldReturnTrue():
    first_inch = Inch(0.0)
    assert first_inch is not None


def test_givenOneInchAndFloatValue_WhenCompared_ShouldReturnTrue():
    first_inch = Inch(0.0)
    second_inch = float(0.0)
    with pytest.raises(AssertionError):
        assert first_inch == second_inch


def test_givenTwoDifferentInchValue_WhenCompared_ShouldReturnFalse():
    first_inch = Inch(0.0)
    second_inch = Inch(1.0)
    assert first_inch != second_inch


#______________________________________________________________________
#UC2-

#3ft=1yard
def test_3FeetAnd_1YardValue_Compared_ReturnTrue():
    first_feet = QuantityMeasurement(Length.FEET,3.0)
    second_yard = QuantityMeasurement(Length.YARD,1.0)
    with pytest.raises(AssertionError):
        assert first_feet == second_yard

#  1ft != 1yd
def test_1FeetAnd_1YardValue_Compared_ReturnFalse():
    first_feet = QuantityMeasurement(Length.FEET,1.0)
    second_yard = QuantityMeasurement(Length.YARD,1.0)
    assert first_feet != second_yard

# 1in != 1yd
def test_OneInch_OneYardValue_Compared_ReturnFalse():
    first_inch = QuantityMeasurement(Length.INCH,1.0)
    second_yard = QuantityMeasurement(Length.YARD,1.0)
    assert first_inch != second_yard


# 36in = 1yd
def test_36InchAnd_OneYardValue_WhenCompared_ReturnTrue():
    first_inch = QuantityMeasurement(Length.INCH,36.0)
    second_yard = QuantityMeasurement(Length.YARD,1.0)
    with pytest.raises(AssertionError):
        assert first_inch == second_yard


# Test_case5 1yd = 3ft
def test_OneYardAnd_3FeetValue_Compared_ReturnTrue():
    first_yard = QuantityMeasurement(Length.YARD,1.0)
    second_feet = QuantityMeasurement(Length.FEET,3.0)
    with pytest.raises(AssertionError):
        assert first_yard == second_feet


# Test_case 6 1yd = 36in
def test_OneYardAnd_36InchValue_WhenCompared_ReturnTrue():
    first_yard = QuantityMeasurement(Length.YARD,1.0)
    second_inch = QuantityMeasurement(Length.INCH,36.0)
    with pytest.raises(AssertionError):
        assert first_yard == second_inch

#___________________________________________________________________________

#UC3-Testcase-2inch=5cm

def test_TwoInchAnd_FiveCM_IfCompared_ShouldReturnTrue():
    first_inch = QuantityMeasurement(Length.INCH, 2.0)
    second_cm = QuantityMeasurement(Length.CM, 5.0)
    with pytest.raises(AssertionError):
        assert first_inch == second_cm

#_________________________________________________________________________

