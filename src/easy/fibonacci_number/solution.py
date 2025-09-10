#! /usr/bin/python3
# -*- coding:utf8 -*-

# Copyright 2025 Robina Li. BSD 3-Clause License All Rights Reserved.
# @file : solution.py
# @desc : Solution for Leetcode
# Reference : https://leetcode.com/problems/fibonacci-number/

from typing import List
from functools import cache

class Solution(object):
    @cache
    def fib(self, n: int) -> int:
        if n <= 1: return n
        return self.fib(n - 1) + self.fib(n - 2)

    def __init__(self):
        self.cache = dict()
    def fib1(self, n: int) -> int:
        if n in self.cache:
            return self.cache[n]
        if n < 2:
            rtn = n
        else:
            rtn = self.fib(n - 1) + self.fib(n - 2)
        self.cache[n] = rtn
        return rtn

if __name__ == '__main__':
    solution = Solution()
    rtn = solution.fib(2)
    print(1 == rtn)
    rtn = solution.fib(3)
    print(2 == rtn)
    rtn = solution.fib(4)
    print(3 == rtn)

    rtn = solution.fib1(2)
    print(1 == rtn)
    rtn = solution.fib1(3)
    print(2 == rtn)
    rtn = solution.fib1(4)
    print(3 == rtn)