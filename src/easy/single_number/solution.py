#! /usr/bin/python3
# -*- coding:utf8 -*-

# Copyright 2025 Robina Li. BSD 3-Clause License All Rights Reserved.
# @file : solution.py
# @desc : Solution for Leetcode
# Reference : https://leetcode.com/problems/single-number/

from typing import List
import math

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        a = 0
        for i in nums:
            a ^= i
        return a

if __name__ == '__main__':
    solution = Solution()

    rtn = solution.singleNumber([2,2,1])
    print(1 == rtn)
    rtn = solution.singleNumber([4,1,2,1,2])
    print(4 == rtn)
    rtn = solution.singleNumber([1])
    print(1 == rtn)