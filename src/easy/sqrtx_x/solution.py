#! /usr/bin/python3
# -*- coding:utf8 -*-

# Copyright 2025 Robina Li. BSD 3-Clause License All Rights Reserved.
# @file : solution.py
# @desc : Solution for Leetcode
# Reference : https://leetcode.com/problems/sqrtx/

from typing import List
from functools import cache
from math import e, log

class Solution(object):

    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x
        left = int(e**(0.5 * log(x)))
        right = left + 1
        return left if right * right > x else right

    def mySqrt1(self, x: int) -> int:
        if x < 2:
            return x
        left, right = 2, x // 2
        while left <= right:
            pivot = left + (right - left) // 2
            num = pivot * pivot
            if num > x:
                right = pivot - 1
            elif num < x:
                left = pivot + 1
            else:
                return pivot
        return right

if __name__ == '__main__':
    solution = Solution()

    rtn = solution.mySqrt(4)
    print(2 == rtn)
    rtn = solution.mySqrt(8)
    print(2 == rtn)

    rtn = solution.mySqrt1(4)
    print(2 == rtn)
    rtn = solution.mySqrt1(8)
    print(2 == rtn)