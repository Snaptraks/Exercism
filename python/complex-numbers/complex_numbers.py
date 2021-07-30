import math


def _unpack(z1, z2):
    return z1.real, z1.imaginary, z2.real, z2.imaginary


class ComplexNumber:
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __eq__(self, other):
        return (self.real == other.real) and (self.imaginary == other.imaginary)

    def __repr__(self):
        return f"{self.real}{self.imaginary:+d}i"

    def __add__(self, other):
        return self.__class__(
            self.real + other.real,
            self.imaginary + other.imaginary,
        )

    def __mul__(self, other):
        a, b, c, d = _unpack(self, other)

        return self.__class__(
            a * c - b * d,
            b * c + a * d,
        )

    def __sub__(self, other):
        return self + (-other)

    def __neg__(self):
        return self.__class__(
            -self.real,
            -self.imaginary,
        )

    def __truediv__(self, other):
        a, b, c, d = _unpack(self, other)
        denom = c**2 + d**2

        return self.__class__(
            (a * c + b * d) / denom,
            (b * c - a * d) / denom,
        )

    def __abs__(self):
        return math.sqrt(self.real**2 + self.imaginary**2)

    def conjugate(self):
        return self.__class__(
            self.real,
            -self.imaginary,
        )

    def exp(self):
        exp_a = math.exp(self.real)
        return self.__class__(
            exp_a * math.cos(self.imaginary),
            exp_a * math.sin(self.imaginary),
        )
