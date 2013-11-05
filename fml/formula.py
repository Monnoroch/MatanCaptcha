# -*- coding: utf-8 -*-
"""Module with base Formula class"""

class Formula:
    """Abstract formula expression"""

    def texify(self):
        """Get formula as TeX string"""
        raise Exception("Abstract method \"Formula.texify\"")

    def __str__(self):
        return self.texify()
