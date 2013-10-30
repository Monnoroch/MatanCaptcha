# -*- coding: utf-8 -*-

from flask import Flask, jsonify
from tasks import *


app = Flask(__name__)

@app.route("/")
def index():
    task = LimitPolynomTask("x", 7, -100, 100)
    return jsonify({"formula": task.formula().texify(), "solution": task.solve()})


app.run()

