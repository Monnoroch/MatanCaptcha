# -*- coding: utf-8 -*-

from tasks import *


class LimitPolynomTask1(LimitPolynomTask):
    def __init__(self):
        LimitPolynomTask.__init__(self, "x", 7, -3, 3)


class GnDictTask1(GnDictTask):
    def __init__(self):
        GnDictTask.__init__(self, ["привет", "пока"])


taskBuilder = CaptchaTaskBuilder()
taskBuilder.addTaskClass("matan", LimitPolynomTask1, 1)
taskBuilder.addTaskClass("gn", GnDictTask1, 2)


def main():
    taskData = taskBuilder.getTask("matan", 0)
    task = taskData["task"]
    uid = taskData["id"]
    # TODO: get solution from user
    solution = task.getSolution()
    res = taskBuilder.verify(uid, solution)
    print str(task), "->", str(solution) + "; (" + str(res) + ")"


if __name__ == "__main__":
    main()
