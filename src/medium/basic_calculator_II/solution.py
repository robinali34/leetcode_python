#! /usr/bin/python3
# -*- coding:utf8 -*-

# Copyright 2025 Robina Li. BSD 3-Clause License All Rights Reserved.
# @file : solution.py
# @desc : Solution for Leetcode
# Reference : https://leetcode.com/problems/basic-calculator-ii/

from functools import cache
from typing import List
import math

class Solution(object):
    def calculate(self, s: str) -> int:
        if len(s) == 0: return 0
        cur = last = rtn = 0
        sign = '+'
        for i, cur_char in enumerate(s):
            if cur_char.isdigit():
                cur = cur* 10 + int(cur_char)
            if (not cur_char.isdigit() and not cur_char.isspace()) or i == len(s) - 1:
                if sign == '+':
                    rtn += last
                    last = cur
                elif sign == '-':
                    rtn += last
                    last = -cur
                elif sign == '*':
                    last *= cur
                elif sign == '/':
                    last = int(last / cur)
                sign = cur_char
                cur = 0
        rtn += last
        return rtn
 
if __name__ == '__main__':
    solution = Solution()
    rtn = solution.calculate("3+2*2")
    print(7 == rtn)
    rtn = solution.calculate(" 3/2 ")
    print(1 == rtn)
    rtn = solution.calculate(" 3+5 / 2 ")
    print(5 == rtn)