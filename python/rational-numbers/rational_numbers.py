from math import gcd, copysign


class Rational:
    def __init__(self, numer, denom=1):
        self.numer = numer
        self.denom = denom

        if denom == 0:
            raise ZeroDivisionError("Denominator cannot be zero.")

        self._reduce()

    def __eq__(self, other):
        return self.numer == other.numer and self.denom == other.denom

    def __repr__(self):
        return f"{self.numer}/{self.denom}"

    def __add__(self, other):
        return self.__class__(
            self.numer * other.denom + other.numer * self.denom,
            self.denom * other.denom,
        )

    def __sub__(self, other):
        return self + (-other)

    def __neg__(self):
        return self.__class__(-self.numer, self.denom)

    def __mul__(self, other):
        return self.__class__(
            self.numer * other.numer,
            self.denom * other.denom,
        )

    def __truediv__(self, other):
        return self * other.inverse()

    def __abs__(self):
        return self.__class__(
            abs(self.numer),
            abs(self.denom),
        )

    def __pow__(self, power):
        if isinstance(power, float):
            return self.numer**power / self.denom**power

        # else if integer
        if power < 0:
            base = self.inverse()
            n = abs(power)
        else:
            base = self
            n = power

        return self.__class__(
            base.numer**n,
            base.denom**n,
        )

    def __rpow__(self, base):
        return (base ** self.numer) ** (1 / self.denom)

    def _reduce(self):
        _gcd = gcd(self.numer, self.denom)
        self.numer //= _gcd
        self.denom //= _gcd

        self.numer = self.numer * int(copysign(1, self.denom))
        self.denom = abs(self.denom)

    def inverse(self):
        return self.__class__(self.denom, self.numer)


if __name__ == '__main__':
    r1 = Rational(2, 4)
    r2 = Rational(1, 3)
    print(r1 / r2)
    print(r1**2.5)
