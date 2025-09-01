#! /usr/bin/python3
# -*- coding:utf8 -*-

# Copyright 2025 Robina Li. BSD 3-Clause License All Rights Reserved.
# @file : solution.py
# @desc : Solution for Leetcode
# Reference : https://leetcode.com/problems/maximum-average-subarray-i/

from typing import List
from functools import cache
import math

class Solution(object):
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        sum_, max_avg = 0, -math.inf

        start = 0
        for end in range(len(nums)):
            sum_ += nums[end]
            if end - start + 1 == k:
                max_avg = max(max_avg, sum_/k)
            if end >= k - 1:
                sum_ -= nums[start]
                start += 1
        return max_avg

if __name__ == '__main__':
    solution = Solution()

    rtn = solution.findMaxAverage([1,12,-5,-6,50,3], 4)
    print(12.75000 == rtn)
    rtn = solution.findMaxAverage([5], 1)
    print(5.00000 == rtn)