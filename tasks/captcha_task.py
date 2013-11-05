# -*- coding: utf-8 -*-
"""Module with base CaptchaTask class and some basic task classes"""

class CaptchaTask:
    """Base class for all captcha tasks"""

    def get(self):
        """Get string representation"""
        raise Exception(
            "Attempt to call abstract method \"" +
            self.__class__.__name__ + ".get\"!"
        )

    def solution(self):
        """Get solution as a string"""
        raise Exception(
            "Attempt to call abstract method \"" +
            self.__class__.__name__ + ".solution\"!"
        )

    def verify(self, solution):
        """Verify solution"""
        raise Exception(
            "Attempt to call abstract method \"" +
            self.__class__.__name__ + ".verify\"!"
        )

    def __str__(self):
        return self.get()


class DefaultCaptchaTask(CaptchaTask):
    """CaptchaTask with default verify implementation"""

    def verify(self, solution):
        return solution == self.solution()
