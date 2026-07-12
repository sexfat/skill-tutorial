def add(a, b):
    return a + b


def multiply(a, b):
    return a * b


class Calculator:
    def __init__(self):
        self.history = []

    def compute(self, op, a, b):
        if op == "add":
            result = add(a, b)
        elif op == "multiply":
            result = multiply(a, b)
        else:
            raise ValueError(f"Unknown op: {op}")
        self.history.append((op, a, b, result))
        return result
