# -*- coding: utf-8 -*-

from flask import Flask, jsonify
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


app = Flask(__name__)

@app.route("/get")
def indexGet():
    task = taskBuilder.getTask("gn", 0)
    return jsonify({"task": str(task["task"]), "id": task["id"]})

@app.route("/verify")
def indexVerify():
    # TODO: get those
    uid = ""
    solution = ""
    return jsonify({"res": taskBuilder.verify(uid, solution)})

app.run()

