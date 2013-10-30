import random
from fml import *
from Task import DefaultTask

def NOD(a, b):
    a = abs(a)
    b = abs(b)
    while a != 0 and b != 0:
        if a > b:
            a = a % b
        else:
            b = b % a
    return a + b


class LimitPolynomTask(DefaultTask):
    random.seed()

    def __init__(self, variable, coeffs1, cmin1 = None, cmax1 = None, coeffs2 = None, cmin2 = None, cmax2 = None):
        self.variable = Variable(variable)
        if coeffs2 is None:
            coeffs2 = coeffs1
        if cmin2 is None:
            cmin2 = cmin1
        if cmax2 is None:
            cmax2 = cmax1

        if type(coeffs1) is int:
            self.coeffs1 = self.genCoeffs(coeffs1, cmin1, cmax1)
        else:
            self.coeffs1 = coeffs1[:]

        if type(coeffs2) is int:
            self.coeffs2 = self.genCoeffs(coeffs2, cmin1, cmax1)
        else:
            self.coeffs2 = coeffs2[:]

        # NOTE: for simplicity
        if self.coeffs1[0] == 0:
            self.coeffs1[0] = 1

        if self.coeffs2[0] == 0:
            self.coeffs2[0] = 1

        self._formula = Limit(self.variable, Infinity(),
            Rational(
                PolynomNum(self.variable, self.coeffs1),
                PolynomNum(self.variable, self.coeffs2)
            )
        )

    def solve(self):
        if self.coeffs1[0] % self.coeffs2[0] == 0:
            self.solution = self.coeffs1[0] / self.coeffs2[0]
        else:
            nod = NOD(self.coeffs1[0], self.coeffs2[0])
            num = self.coeffs1[0]/nod
            den = self.coeffs2[0]/nod
            self.solution = (num * den < 0 and "-" or "") + str(abs(num)) + "/" + str(abs(den))
        return self.solution

    def genCoeffs(self, cnt, min, max):
        res = []
        for i in xrange(0, cnt):
            res.append(random.randint(min, max))
        return res

