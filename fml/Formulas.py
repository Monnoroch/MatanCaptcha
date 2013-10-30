from Formula import Formula

class Rational(Formula):
    """Rational expression"""
    def __init__(self, f1, f2):
        self.f1 = f1
        self.f2 = f2

    def texify(self):
        return "\\frac{" + self.f1.texify() + "}{" + self.f2.texify() + "}"

class Limit(Formula):
    """Limit expression"""
    def __init__(self, variable, limit, fml):
        self.variable = variable
        self.limit = limit
        self.fml = fml

    def texify(self):
        return "\\lim_{" + self.variable.texify() + " \\to " + self.limit.texify() + "} " + self.fml.texify()

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
        for p in xrange(0, self.cnt):
            cf = self.coeffs[p]

            if cf == 0:
                continue
            # [-][cf ][x][^{}]

            if p == self.cnt - 1:
                if cf < 0:
                    res += " - "
                else:
                    res += " + "
                res += str(abs(cf))
            else:
                if cf < 0:
                    if p == 0:
                        res += "-"
                    else:
                        res += " - "
                elif p != 0:
                    res += " + "
                if abs(cf) != 1:
                    res += str(abs(cf))
                res += self.variable.texify()
                if self.cnt - p - 1 > 1:
                    res += "^{" + str(self.cnt - p - 1) + "}"
        return res
