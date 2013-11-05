# -*- coding: utf-8 -*-

import uuid, random


def weighted_choice(weights):
    rnd = random.random() * sum(weights)
    for i, w in enumerate(weights):
        rnd -= w
        if rnd < 0:
            return i


class CaptchaTaskBuilder:

	# {type: list of (task class, weight for random picking)}
	tasks_table = {
		"matan": [],
		"gn":    []
	}

	# тут хранятся активные таски: те, на которые не запрашивали проверку
	# проверенные таски удаляются
	tasks = {}
	# тут храним всю инфу о тасках и решениях
	log = {}

	def __init__(self):
		self._recalc_weights()

	def get(self, mode, diff):
		task = self._get(mode, diff)
		uid = str(uuid.uuid4())
		self.tasks[uid] = {"diff": diff, "mode": mode, "task": task}
		self.log[uid] = {"diff": diff, "mode": mode, "className": task.__class__.__name__, "task": str(task)}
		return {"task": task, "id": uid}

	def solution(self, uid):
		return self.tasks[uid]["task"].solution()

	def verify(self, uid, solution):
		obj = self.tasks[uid]
		task = obj["task"]
		res = task.verify(solution)
		logobj = self.log[uid]
		logobj["result"] = res
		if not res:
			logobj["solution"] = solution
		self.drop(uid)
		return res

	def _get(self, mode, diff):
		(n, w) = self.tasks_table[mode][weighted_choice(self.tasks_table_weights[mode])]
		return n()

	def add_task_class(self, mode, cls, weight):
		self.tasks_table[mode].append((cls, weight))
		self._recalc_weights()

	def _recalc_weights(self):
		self.tasks_table_weights = {}
		for x in self.tasks_table.keys():
			val = []
			for (n, w) in self.tasks_table[x]:
				val.append(w)
			self.tasks_table_weights[x] = val

	def drop(self, uid):
		del self.tasks[uid]
