# -*- coding: utf-8 -*-

from tasks import *


def main():
    # 7   -- power of poly
    # -30 -- min coeff
    # 30  -- max coeff
    task = LimitPolynomTask("x", 7, -2, 2)
    print task.formula(), " -> ", task.solve()


if __name__ == "__main__":
    main()

