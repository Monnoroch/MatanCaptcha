# -*- coding: utf-8 -*-

class Formula:
    """Abstract formula expression"""
    def texify(self):
        raise Exception("Abstract method \"Formula.texify\"")

    def __str__(self):
        return self.texify()
