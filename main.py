# -*- coding: utf-8 -*-

from flask import Flask, jsonify
from tasks import *


consoleMode = True

if consoleMode:
    def main():
        # 7   -- power of poly
        # -30 -- min coeff
        # 30  -- max coeff
        task = LimitPolynomTask("x", 7, -2, 2)
        print task.formula(), " -> ", task.solve()


    if __name__ == "__main__":
        main()

else:
    app = Flask(__name__)

    @app.route("/")
    def index():
        task = LimitPolynomTask("x", 7, -100, 100)
        return jsonify({"formula": task.formula().texify(), "solution": task.solve()})


    app.run()

