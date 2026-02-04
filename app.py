class Calculator:
    def add(self, a, b):
        return a + b

    def sub(self, a, b):
        return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return None
    return a / b


calc = Calculator()

print(calc.add(5, 3))
print(calc.sub(10, 4))
print(multiply(2, 6))
print(divide(10, 2))
