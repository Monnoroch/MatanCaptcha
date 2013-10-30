# -*- coding: utf-8 -*-

from Formula import Formula


class RawExpression(Formula):
    """Raw text expression"""
    def __init__(self, expr):
        self.expr = expr

    def texify(self):
        return str(self.expr)


class Variable(RawExpression):
    """Variable expression"""
    def __init__(self, name):
        self.expr = name

class Infinity(Formula):
    def texify(self):
        return "\\infty"
