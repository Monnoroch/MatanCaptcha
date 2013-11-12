# -*- coding: utf-8 -*-
"""Simple flask server for captcha generation"""

import os
import urllib

from flask import Flask
from flask import jsonify
from flask import request
from flask import url_for

from tasks import *


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

app = Flask(__name__)


@app.route("/get")
def index_get():
    """/get?type=type"""
    ttype = request.args.get("type")
    task = task_builder.get(ttype, 0)
    fname = task["id"] + ".png"
    if ttype == "matan":
        stask = str(task["task"])
        url = "https://chart.googleapis.com/chart?" + urllib.urlencode({"cht": "tx", "chl": stask})
        sid = task["id"]
        img = "<img src=\"" + url + "\"/>"
        did = "<div>id = \"" + sid + "\"</div>"
        dtsk = "<div>tex = \"" + stask + "\"</div>"
        return "%s<br>%s<br>%s" % (img, did, dtsk)
    else:
        return jsonify({"task": str(task["task"]), "id": task["id"]})

@app.route("/verify")
def index_verify():
    """/verify?id=id&solution=solution"""
    uid = request.args.get("id")
    solution = request.args.get("solution", "string")
    return jsonify({"res": task_builder.verify(uid, solution)})

@app.route("/drop")
def index_drop():
    """/drop?id=id"""
    uid = request.args.get("id")
    task_builder.drop(uid)
    return ""


def main():
    """main"""
    task_builder.add_task_class("matan", LimitPolynomTask1, 1)
    task_builder.add_task_class("matan", MatrixKindaDiagDetTask1, 1)
    task_builder.add_task_class("gn", GnDictTask1, 2)
    app.run(debug=True)


if __name__ == "__main__":
    main()
