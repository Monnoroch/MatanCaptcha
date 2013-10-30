# -*- coding: utf-8 -*-

from flask import Flask, jsonify
from tasks import *


taskBuilder = CaptchaTaskBuilder()

app = Flask(__name__)

@app.route("/get")
def indexGet():
    return jsonify(taskBuilder.getTask("matan", 0))

@app.route("/verify")
def indexVerify():
    # TODO: get those
    uid = ""
    solution = ""
    return jsonify({"res": taskBuilder.verify(uid, solution)})

app.run()

