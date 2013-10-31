# -*- coding: utf-8 -*-

import os

from flask import Flask, jsonify, request, url_for
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
    ttype = request.args.get("type")
    task = taskBuilder.getTask(ttype, 0)
    fname = task["id"] + '.png'
    if ttype == "matan":
        Mathtex(r"$" + str(task["task"]) + r"$").save("static/" + fname, 'png')
        return "<img src=\"" + url_for('static', filename=fname) + "\"/>" + "<br><div>id = \"" + task["id"] + "\"</div><div>tex = \"" + str(task["task"]) + "\"</div>"
    else:
        return jsonify({"task": str(task["task"]), "id": task["id"]})

@app.route("/verify")
def indexVerify():
    uid = request.args.get("id")
    solution = request.args.get("solution", "string")
    return jsonify({"res": taskBuilder.verify(uid, solution)})

app.run()

