import numbers

class CalculatorError(Exception):
    """for calculator error"""

class Calculator:
    def add(self, a, b):
        self._check_operand(a)
        self._check_operand(b)
        # try:
        return a + b
        # except TypeError as ex:
        #     raise CalculatorError("You can't add by str!") from ex

    def subtrack(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        try:
            return a / b
        except ZeroDivisionError as ex:
            raise CalculatorError("You can't divide by zero") from ex

    def _check_operand(self, operand):
        if not isinstance(operand, numbers.Number):
            raise CalculatorError(f"{operand} is not a number!")
