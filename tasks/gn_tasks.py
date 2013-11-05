# -*- coding: utf-8 -*-
"""Some GN tasks"""

import random

from tasks.gn_captcha_task import GnCaptchaTask


class GnDictTask(GnCaptchaTask):
    """GN task with checking orphografy"""

    def __init__(self, dic, max_wc):
        self.dict = dic[:]
        self.max_wildcards = max_wc

        res = self.dict[random.randint(0, len(self.dict) - 1)]
        self._solution = res
        cnt = random.randint(1, self.max_wildcards)
        wcs = []
        for i in xrange(0, cnt):
            wcs.append(random.randint(0, len(res) - 1))
        for i in xrange(0, cnt):
            res = res[:wcs[i]] + "*" + res[wcs[i] + 1:]
        self.task = res

    def get(self):
        return self.task

    def solution(self):
        return self._solution

    def __str__(self):
        # workaround for unicode strings in python 2
        return '[' + str(self.task) + ', ' + str(self._solution) + ']'
