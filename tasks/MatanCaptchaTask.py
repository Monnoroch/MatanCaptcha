# -*- coding: utf-8 -*-

from CaptchaTask import CaptchaTask


class MatanCaptchaTask(CaptchaTask):
	pass

class MatanFormulaCaptchaTask(MatanCaptchaTask):
	def getTask(self):
		return self._formula

	def __str__(self):
		return str(self._formula)
