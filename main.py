# -*- coding: utf-8 -*-

from tasks import *


taskBuilder = CaptchaTaskBuilder()


def main():
    taskData = taskBuilder.getTask("matan", 0)
    task = taskData["task"]
    uid = taskData["id"]
    # TODO: get solution from user
    solution = task.getSolution()
    res = taskBuilder.verify(uid, solution)
    print task, "->", str(solution) + "; (" + str(res) + ")"


if __name__ == "__main__":
    main()

