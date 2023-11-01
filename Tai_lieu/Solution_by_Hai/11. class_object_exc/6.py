class Fraction:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    def setNumerator(self, numerator):
        self.numerator = numerator

    def getNumerator(self):
        return self.numerator

    def setDenominator(self, denominator):
        self.denominator = denominator

    def getDenominator(self):
        return self.denominator

    def inputInfo(self):
        self.numerator = int(input("Nhập tử số: "))
        self.denominator = int(input("Nhập mẫu số: "))

    def printFraction(self):
        print(f"{self.numerator}/{self.denominator}")

    def gcd(self, a, b):
        if b == 0:
            return a
        else:
            return self.gcd(b, a % b)

    def rutGon(self):
        ucln = self.gcd(self.numerator, self.denominator)
        self.numerator //= ucln
        self.denominator //= ucln

    def nghichDao(self):
        temp = self.numerator
        self.numerator = self.denominator
        self.denominator = temp

    def add(self, otherFraction):
        resultNumerator = (self.numerator * otherFraction.denominator) + (otherFraction.numerator * self.denominator)
        resultDenominator = self.denominator * otherFraction.denominator
        return Fraction(resultNumerator, resultDenominator)

    def sub(self, otherFraction):
        resultNumerator = (self.numerator * otherFraction.denominator) - (otherFraction.numerator * self.denominator)
        resultDenominator = self.denominator * otherFraction.denominator
        return Fraction(resultNumerator, resultDenominator)

    def mul(self, otherFraction):
        resultNumerator = self.numerator * otherFraction.numerator
        resultDenominator = self.denominator * otherFraction.denominator
        return Fraction(resultNumerator, resultDenominator)

    def div(self, otherFraction):
        resultNumerator = self.numerator * otherFraction.denominator
        resultDenominator = self.denominator * otherFraction.numerator
        return Fraction(resultNumerator, resultDenominator)

fraction1 = Fraction(0, 0)
fraction1.inputInfo()
fraction1.rutGon()
print("Phân số sau khi rút gọn:")
fraction1.printFraction()
fraction1.nghichDao()
print("Phân số nghịch đảo:")
fraction1.printFraction()

fraction2 = Fraction(0, 0)
fraction2.inputInfo()
print("Phân số thứ nhất:")
fraction1.printFraction()
print("Phân số thứ hai:")
fraction2.printFraction()
print("Tổng hai phân số:")
(fraction1.add(fraction2)).printFraction()
print("Hiệu hai phân số:")
(fraction1.sub(fraction2)).printFraction()
print("Tích hai phân số:")
(fraction1.mul(fraction2)).printFraction()
print("Thương hai phân số:")
(fraction1.div(fraction2)).printFraction()
