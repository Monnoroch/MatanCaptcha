# -*- coding: utf-8 -*-

from tasks import *


class LimitPolynomTask1(LimitPolynomTask):
    def __init__(self):
        LimitPolynomTask.__init__(self, "x", 7, -3, 3)


class GnDictTask1(GnDictTask):
    gnWords = [line.strip() for line in open('data/russian_words_dictionary.txt')]

    def __init__(self):
        GnDictTask.__init__(self, self.gnWords, 2)


taskBuilder = CaptchaTaskBuilder()
taskBuilder.addTaskClass("matan", LimitPolynomTask1, 1)
taskBuilder.addTaskClass("gn", GnDictTask1, 2)


def test(taskData):
    task = taskData["task"]
    uid = taskData["id"]
    # TODO: get solution from user
    solution = task.getSolution()
    res = taskBuilder.verify(uid, solution)
    print str(task), "->", str(solution) + "; (" + str(res) + ")"


def main():
    # Matan capcha test
    test(taskBuilder.getTask("matan", 0))
    # Gn capcha test
    test(taskBuilder.getTask("gn", 0))


if __name__ == "__main__":
    main()
