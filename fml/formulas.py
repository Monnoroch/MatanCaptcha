# -*- coding: utf-8 -*-
"""Module with formulas"""

from fml.formula import Formula


class Rational(Formula):
    """Rational expression"""
    def __init__(self, num, den):
        self.num = num
        self.den = den

    def texify(self):
        return "\\frac{%s}{%s}" % (self.num.texify(), self.den.texify())


class Limit(Formula):
    """Limit expression"""
    def __init__(self, variable, limit, fml):
        self.variable = variable
        self.limit = limit
        self.fml = fml

    def texify(self):
        vart = self.variable.texify()
        limt = self.limit.texify()
        fmlt = self.fml.texify()
        return "\\lim_{%s\\to%s} %s" % (vart, limt, fmlt)


class PolynomNum(Formula):
    """Polynom with number coefficients expression"""
    def __init__(self, variable, coeffs):
        self.variable = variable
        self.coeffs = coeffs[:]
        self.cnt = len(self.coeffs)

    def __len__(self):
        return self.cnt

    def texify(self):
        res = ""
        for pos in xrange(0, self.cnt):
            coeff = self.coeffs[pos]

            if coeff == 0:
                continue
            # [-][coeff ][x][^{}]

            if pos == self.cnt - 1:
                if coeff < 0:
                    res += " - "
                else:
                    res += " + "
                res += str(abs(coeff))
            else:
                if coeff < 0:
                    if pos == 0:
                        res += "-"
                    else:
                        res += " - "
                elif pos != 0:
                    res += " + "
                if abs(coeff) != 1:
                    res += str(abs(coeff))
                res += self.variable.texify()
                if self.cnt - pos - 1 > 1:
                    res += "^{" + str(self.cnt - pos - 1) + "}"
        return res


class MatrixNum(Formula):
    """Matrix with numeric coefficients"""
    def __init__(self, rows):
        self.rows = rows[:]
        self.n = len(rows)
        self.k = len(rows[0])
        for row in rows:
            assert(len(row) == self.k)

    def texify(self):
        data = ""
        for ind1 in xrange(self.n):
            row = self.rows[ind1]
            for ind2 in xrange(self.k):
                num = row[ind2]
                data += str(num)
                if ind2 != self.k - 1:
                    data += " & "
            if ind1 != self.n - 1:
                data += " \\\\ "
        return "\\left(\\begin{matrix} %s \\end{matrix}\\right)" % data

class Determinant(Formula):
    """Det of a matrix"""

    def __init__(self, matr):
        self.matr = matr

    def texify(self):
        return "det \\left| " + self.matr.texify()[6:-7] + " \\right|"
