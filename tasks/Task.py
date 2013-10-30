class Task:
    def solve(self):
        raise Exception("Abstract method \"Task.solve\"")

    def formula(self):
    	raise Exception("Abstract method \"Task.formula\"")

class DefaultTask(Task):
	def formula(self):
		return self._formula