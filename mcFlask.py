# -*- coding: utf-8 -*-

from flask import Flask, jsonify
from tasks import *


taskBuilder = CaptchaTaskBuilder()

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

