# -*- coding: utf-8 -*-

import uuid

from LimitPolynomTask import LimitPolynomTask
from GnDictTask import GnDictTask


class CaptchaTaskBuilder:
	types = {"matan": "_getMatanTask", "gn": "_getGnTask"}

	# тут хранятся активные таски: те, на которые не запрашивали проверку
	# проверенные таски удаляются
	tasks = {}
	# тут храним всю инфу о тасках и решениях
	log = {}

	def __init__(self):
		pass

	def getTask(self, mode, diff):
		task = getattr(self, self.types[mode])(diff)
		uid = uuid.uuid4()
		self.tasks[uid] = {"diff": diff, "mode": mode, "task": task}
		self.log[uid] = {"diff": diff, "mode": mode, "className": task.__class__.__name__, "task": str(task)}
		return {"task": task, "id": uid}

	def getSolution(self, uid):
		return self.tasks[uid]["task"].getSolution()

	def verify(self, uid, solution):
		res = self.tasks[uid]["task"].verify(solution)
		logobj = self.log[uid]
		logobj["result"] = res
		if not res:
			logobj["solution"] = solution
		del self.tasks[uid]
		return res

	def _getMatanTask(self, diff):
		return LimitPolynomTask("x", 7, -3, 3)

	def _getGnTask(self, diff):
		return GnDictTask(["привет", "пока"])
