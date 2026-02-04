class Calculator:
    """Simple calculator for addition and subtraction"""

    def add(self, a, b):
        """Return sum of two numbers"""
        return self._validate(a) + self._validate(b)

    def sub(self, a, b):
        """Return difference of two numbers"""
        return self._validate(a) - self._validate(b)
        return self._validate(a) + self._validate(b)

    def sub(self, a, b):
        return self._validate(a) - self._validate(b)

    def _validate(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("Only numbers allowed")
        return value

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


calc = Calculator()

print(calc.add(5, 3))
print(calc.sub(10, 4))
print(multiply(2, 6))
print(divide(10, 2))
