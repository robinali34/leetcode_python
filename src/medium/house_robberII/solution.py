#! /usr/bin/python3
# -*- coding:utf8 -*-

# Copyright 2025 Robina Li. BSD 3-Clause License All Rights Reserved.
# @file : solution.py
# @desc : Solution for Leetcode
# Reference : https://leetcode.com/problems/house-robber/

from functools import cache
from typing import List

class Solution(object):
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1: return nums[0]
        @cache
        def dp(i: int, j: int) -> int:
            if j < i: return 0
            return max(nums[j] + dp(i, j - 2), dp(i, j - 1))
        return max(dp(0, n - 2), dp(1, n - 1))

if __name__ == '__main__':
    solution = Solution()
    rtn = solution.rob([2,3,2])
    print(3 == rtn)
    rtn = solution.rob([1,2,3,1])
    print(4 == rtn)
    rtn = solution.rob([1,2,3])
    print(3 == rtn)