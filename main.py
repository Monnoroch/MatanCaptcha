# -*- coding: utf-8 -*-
"""main"""

from tasks import *
from fml import *


class LimitPolynomTask1(LimitPolynomTask):
    """Custom implementation of LimitPolynomTask"""
    def __init__(self):
        LimitPolynomTask.__init__(self, "x", 7, -3, 3)


class GnDictTask1(GnDictTask):
    """Custom implementation of GnDictTask"""
    with open("data/russian_words_dictionary.txt") as dict_file:
        gn_words = [line.strip() for line in  dict_file]

    def __init__(self):
        GnDictTask.__init__(self, self.gn_words, 2)

class MatrixDiagDetTask1(MatrixDiagDetTask):
    """Custom implementation of MatrixDiagDetTask"""

    def __init__(self):
        MatrixDiagDetTask.__init__(self, 4)

class MatrixKindaDiagDetTask1(MatrixKindaDiagDetTask):
    """Custom implementation of MatrixKindaDiagDetTask"""

    def __init__(self):
        MatrixKindaDiagDetTask.__init__(self, 4)


task_builder = CaptchaTaskBuilder()


def test(task_data):
    """test a task"""
    task = task_data["task"]
    uid = task_data["id"]
    # TODO: get solution from user
    solution = task.solution()
    res = task_builder.verify(uid, solution)
    print str(task), "->", str(solution) + "; (" + str(res) + ")"


def main():
    """main"""
    task_builder.add_task_class("matan", LimitPolynomTask1, 1)
    task_builder.add_task_class("matan", MatrixKindaDiagDetTask1, 1)
    task_builder.add_task_class("gn", GnDictTask1, 2)
    # Matan capcha test
    test(task_builder.get("matan", 0))
    # Gn capcha test
    test(task_builder.get("gn", 0))


if __name__ == "__main__":
    main()
