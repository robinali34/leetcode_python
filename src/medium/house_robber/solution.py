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
        #Max value from 0 to i
        @cache
        def dp(i: int) -> int:
            if i < 0: return 0
            return max(nums[i] + dp(i - 2), dp(i - 1))
        return dp(len(nums) - 1)


if __name__ == '__main__':
    solution = Solution()
    rtn = solution.rob([1,2,3,1])
    print(4 == rtn)
    rtn = solution.rob([2,7,9,3,1])
    print(12 == rtn)