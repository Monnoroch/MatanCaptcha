# -*- coding: utf-8 -*-
"""Module with base MatanCaptchaTask class and some basic task classes"""

from tasks.captcha_task import CaptchaTask


class MatanCaptchaTask(CaptchaTask):
    """Base class for all matan tasks"""
    pass


class MatanFormulaCaptchaTask(MatanCaptchaTask):
    """Matan task with default representation as a formula"""

    _formula = None

    def get(self):
        return str(self._formula)

