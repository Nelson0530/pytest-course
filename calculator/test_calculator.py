import pytest
from calculator import Calculator, CalculatorError

def test_add():
    calculator = Calculator()
    result = calculator.add(3, 2)
    assert result == 5

def test_add_weird_stuff():
    calculator = Calculator()
    with pytest.raises(CalculatorError):
        result = calculator.add("three", 2)         # 測試確實出現error，傳出TypeError

def test_add_weirder_stuff():
    calculator = Calculator()
    with pytest.raises(CalculatorError):
        result = calculator.add("three", "two")     # Failed: DID NOT RAISE <class 'calculator.CalculatorError'>

def test_subtrack():
    calculator = Calculator()
    result = calculator.subtrack(9, 3)
    assert result == 6

def test_multiply():
    calculator = Calculator()
    result = calculator.multiply(9, 3)
    assert result == 27

def test_divide():
    calculator = Calculator()
    result = calculator.divide(9, 3)
    assert result == 3

def test_divide_by_zero_pass():                 # 有 CalculatorError就會 Passed!
    calculator = Calculator()
    with pytest.raises(CalculatorError):
        result = calculator.divide(9, 0)

def test_divide_by_zero_fail():            # Failed: DID NOT RAISE <class 'calculator.CalculatorError'> 並沒有CalculatorError 故測試fail
    calculator = Calculator()
    with pytest.raises(CalculatorError):
        result = calculator.divide(9, 3)
