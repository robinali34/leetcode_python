#! /usr/bin/python3
# -*- coding:utf8 -*-

# Copyright 2025 Robina Li. BSD 3-Clause License All Rights Reserved.
# @file : solution.py
# @desc : Solution for Leetcode
# Reference : https://leetcode.com/problems/min-cost-climbing-stairs/description/

from functools import cache
from typing import List

class Solution(object):
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        @cache
        def dp(i: int) -> int:
            if i<= 1: return 0
            return min(dp(i - 1) + cost[i - 1], dp(i - 2) + cost[i - 2])
        return dp(len(cost))

if __name__ == '__main__':
    solution = Solution()
    rtn = solution.minCostClimbingStairs([10,15,20])
    print(15 == rtn)
    rtn = solution.minCostClimbingStairs([1,100,1,1,1,100,1,1,100,1])
    print(6 == rtn)