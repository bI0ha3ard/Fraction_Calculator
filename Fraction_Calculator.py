class Fraction:
    def __init__(self, num, den):
        self.num = num
        self.den = den

    def __add__(self, other):
        num = self.num * other.den + other.num * self.den
        den = self.den * other.den
        return Fraction(num, den)

    def __sub__(self, other):
        num = self.num * other.den - other.num * self.den
        den = self.den * other.den
        return Fraction(num, den)

    def __mul__(self, other):
        num = self.num * other.num
        den = self.den * other.den
        return Fraction(num, den)

    def __truediv__(self, other):
        num = self.num * other.den
        den = self.den * other.num
        return Fraction(num, den)

    def __str__(self):
        return "{}/{}".format(self.num, self.den)


def main():
    print("Fraction Calculator\n")
    num1 = int(input("Enter numerator of fraction 1: "))
    den1 = int(input("Enter denominator of fraction 1: "))
    f1 = Fraction(num1, den1)
    num2 = int(input("Enter numerator of fraction 2: "))
    den2 = int(input("Enter denominator of fraction 2: "))
    f2 = Fraction(num2, den2)
    print("\n{} + {} = {}".format(f1, f2, f1 + f2))
    print("{} - {} = {}".format(f1, f2, f1 - f2))
    print("{} * {} = {}".format(f1, f2, f1 * f2))
    print("{} / {} = {}".format(f1, f2, f1 / f2))


if __name__ == "__main__":
    main()
