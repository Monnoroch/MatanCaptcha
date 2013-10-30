# -*- coding: utf-8 -*-

class CaptchaTask:
	def getTask(self):
		raise Exception("Attempt to call abstract method \"" + x.__class__.__name__ + ".getTask\"!")

	def getSolution(self):
		raise Exception("Attempt to call abstract method \"" + x.__class__.__name__ + ".getSolution\"!")

	def verify(self, solution):
		raise Exception("Attempt to call abstract method \"" + x.__class__.__name__ + ".verify\"!")		
