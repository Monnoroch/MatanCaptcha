# -*- coding: utf-8 -*-
"""Module with basic formulas"""

from fml.formula import Formula


class RawExpression(Formula):
    """Raw text expression"""
    def __init__(self, expr):
        self.expr = expr

    def texify(self):
        return str(self.expr)


class Variable(RawExpression):
    """Variable expression"""
    def __init__(self, name):
        RawExpression.__init__(self, name)


class Infinity(Formula):
    """Infinity expression"""
    def __init__(self):
        pass

    def texify(self):
        return "\\infty"
