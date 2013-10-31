# -*- coding: utf-8 -*-

import uuid, random

from LimitPolynomTask import LimitPolynomTask
from GnDictTask import GnDictTask


class LimitPolynomTask1(LimitPolynomTask):
    def __init__(self):
        LimitPolynomTask.__init__(self, "x", 7, -3, 3)


class GnDictTask1(GnDictTask):
    def __init__(self):
        GnDictTask.__init__(self, ["привет", "пока"])


def weightedChoice(weights):
    rnd = random.random() * sum(weights)
    for i, w in enumerate(weights):
        rnd -= w
        if rnd < 0:
            return i


class CaptchaTaskBuilder:

	# {type: list of (task class, weight for random picking)}
	tasksTable = {
		"matan": [("LimitPolynomTask1", 2)],
		"gn":    [("GnDictTask1", 1)]
	}

	# тут хранятся активные таски: те, на которые не запрашивали проверку
	# проверенные таски удаляются
	tasks = {}
	# тут храним всю инфу о тасках и решениях
	log = {}

	def __init__(self):
		self.tasksTableWeights = {}
		for x in self.tasksTable.keys():
			val = []
			for (n, w) in self.tasksTable[x]:
				val.append(w)
			self.tasksTableWeights[x] = val

	def getTask(self, mode, diff):
		task = self._getTask(mode, diff)
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

	def _getTask(self, mode, diff):
		tasks = self.tasksTable[mode]
		(n, w) = tasks[weightedChoice(self.tasksTableWeights[mode])]
		return globals()[n]()
