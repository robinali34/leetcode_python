#! /usr/bin/python3
# -*- coding:utf8 -*-

# Copyright 2025 Robina Li. BSD 3-Clause License All Rights Reserved.
# @file : solution.py
# @desc : Solution for Leetcode
# Reference : https://leetcode.com/problems/house-robber/

from functools import cache
from typing import List
from collections import defaultdict

class Solution(object):
    def deleteAndEarn(self, nums: List[int]) -> int:
        houses = defaultdict(int)
        max_num = 0
        for x in nums:
            houses[x] += x
            max_num = max(max_num, x)
        @cache
        def dp(i: int) -> int:
            if i < 0: return 0
            return max(houses[i] + dp(i - 2), dp(i - 1))
        return dp(max_num)

if __name__ == '__main__':
    solution = Solution()
    rtn = solution.deleteAndEarn([3,4,2])
    print(6 == rtn)
    rtn = solution.deleteAndEarn([2,2,3,3,3,4])
    print(9 == rtn)