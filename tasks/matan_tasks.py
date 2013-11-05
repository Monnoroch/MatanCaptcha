# -*- coding: utf-8 -*-
"""Some matan tasks"""

import random

from fml import *
from tasks.matan_captcha_task import MatanFormulaCaptchaTask


def nod(num1, num2):
    """Calculate NOD of two numbers"""
    num1 = abs(num1)
    num2 = abs(num2)
    while num1 != 0 and num2 != 0:
        if num1 > num2:
            num1 = num1 % num2
        else:
            num2 = num2 % num1
    return num1 + num2


class LimitPolynomTask(MatanFormulaCaptchaTask):
    """Matan task with formula lim_{x->inf} P1(x)/P2(x)"""

    def __init__(self, variable, coeffs1, cmin1 = None, cmax1 = None,
        coeffs2 = None, cmin2 = None, cmax2 = None):
        self.variable = Variable(variable)
        if coeffs2 is None:
            coeffs2 = coeffs1
        if cmin2 is None:
            cmin2 = cmin1
        if cmax2 is None:
            cmax2 = cmax1

        if type(coeffs1) is int:
            self.coeffs1 = self._gen_coeffs(coeffs1, cmin1, cmax1)
        else:
            self.coeffs1 = coeffs1[:]

        if type(coeffs2) is int:
            self.coeffs2 = self._gen_coeffs(coeffs2, cmin1, cmax1)
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
        if self.coeffs1[0] % self.coeffs2[0] == 0:
            self._solution = str(self.coeffs1[0] / self.coeffs2[0])
        else:
            vnod = nod(self.coeffs1[0], self.coeffs2[0])
            num = self.coeffs1[0]/vnod
            den = self.coeffs2[0]/vnod
            smun = str(abs(num))
            sden = str(abs(den))
            self._solution = (num * den < 0 and "-" or "") + smun + "/" + sden

    def solution(self):
        return self._solution

    def _gen_coeffs(self, cnt, vmin, vmax):
        """Generate random coeffs array"""
        res = []
        for _ in xrange(0, cnt):
            res.append(random.randint(vmin, vmax))
        return res
