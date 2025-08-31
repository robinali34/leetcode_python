#! /usr/bin/python3
# -*- coding:utf8 -*-

# Copyright 2025 Robina Li. BSD 3-Clause License All Rights Reserved.
# @file : solution.py
# @desc : Solution for Leetcode
# Reference : https://leetcode.com/problems/n-th-tribonacci-number/

from functools import cache

class Solution(object):
    @cache
    def tribonacci(self, n: int) -> int:
        if n == 0: return 0
        if n <= 2: return 1
        return sum(self.tribonacci(n - i - 1) for i in range(3))

if __name__ == '__main__':
    solution = Solution()
    rtn = solution.tribonacci(4)
    print(4 == rtn)
    rtn = solution.tribonacci(25)
    print(1389537 == rtn)