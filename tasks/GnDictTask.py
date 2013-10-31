# -*- coding: utf-8 -*-

import random

from GnCaptchaTask import GnCaptchaTask


class GnDictTask(GnCaptchaTask):
	random.seed()

	def __init__(self, dic):
		self.dict = dic[:]
		self.maxWildcards = 3

		res = self.dict[random.randint(0, len(self.dict) - 1)]
		self.solution = res
		cnt = random.randint(1, self.maxWildcards)
		wcs = []
		for i in xrange(0, cnt):
			wcs.append(random.randint(0, len(res)))
		for i in xrange(0, cnt):
			res = res[:wcs[i]] + "*" + res[wcs[i] + 1:]
		self.task = res

	def getTask(self):
		return self.task

	def getSolution(self):
		return self.solution

	def verify(self, sol):
		return self.solution == sol

	def __str__(self):
		return str([self.task, self.solution])
