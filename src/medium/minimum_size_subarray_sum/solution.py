#! /usr/bin/python3
# -*- coding:utf8 -*-

# Copyright 2025 Robina Li. BSD 3-Clause License All Rights Reserved.
# @file : solution.py
# @desc : Solution for Leetcode
# Reference : https://leetcode.com/problems/minimum-size-subarray-sum/

from functools import cache
from typing import List
import math

class Solution(object):
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_len, sum_ = math.inf, 0
        start = 0
        for end in range(len(nums)):
            sum_+= nums[end]
            if sum_>= target:
                min_len = min(min_len, end - start + 1)
            while sum_ >= target:
                min_len = min(min_len, end - start + 1)
                sum_ -= nums[start]
                start += 1
        if min_len == math.inf:
            return 0
        return min_len
 
if __name__ == '__main__':
    solution = Solution()
    rtn = solution.minSubArrayLen(7, [2, 3, 1, 2, 4, 3])
    print(2 == rtn)
    rtn = solution.minSubArrayLen(4, [1, 4, 4])
    print(1 == rtn)
    rtn = solution.minSubArrayLen(11, [1, 1, 1, 1, 1, 1, 1, 1])
    print(0 == rtn)