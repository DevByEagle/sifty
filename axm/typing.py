class Int:
    def __init__(self, value=0):
        if isinstance(value, int):
            self.value = value
        else:
            raise ValueError("Value must be an integer")

    def __repr__(self):
        return f"Int({self.value})"

    def __add__(self, other):
        if isinstance(other, Int):
            return Int(self.value + other.value)
        return NotImplemented

    def __sub__(self, other):
        if isinstance(other, Int):
            return Int(self.value - other.value)
        return NotImplemented

    def __mul__(self, other):
        if isinstance(other, Int):
            return Int(self.value * other.value)
        return NotImplemented

    def __truediv__(self, other):
        if isinstance(other, Int):
            if other.value == 0:
                raise ValueError("Cannot divide by zero")
            return Int(self.value // other.value)  # Integer division
        return NotImplemented

    def __eq__(self, other):
        if isinstance(other, Int):
            return self.value == other.value
        return NotImplemented

    def __lt__(self, other):
        if isinstance(other, Int):
            return self.value < other.value
        return NotImplemented

    def __le__(self, other):
        if isinstance(other, Int):
            return self.value <= other.value
        return NotImplemented

    def __gt__(self, other):
        if isinstance(other, Int):
            return self.value > other.value
        return NotImplemented

    def __ge__(self, other):
        if isinstance(other, Int):
            return self.value >= other.value
        return NotImplemented

    def __ne__(self, other):
        if isinstance(other, Int):
            return self.value != other.value
        return NotImplemented
