#! /usr/bin/python3
# -*- coding:utf8 -*-

# Copyright 2025 Robina Li. BSD 3-Clause License All Rights Reserved.
# @file : solution.py
# @desc : Solution for Leetcode
# Reference : https://leetcode.com/problems/single-number-ii/

from typing import List

class Solution(object):
    def singleNumber(self, nums: List[int]) -> int:
        return (3 * sum(set(nums)) - sum(nums)) >> 1
 
if __name__ == '__main__':
    solution = Solution()
    rtn = solution.singleNumber([2,2,3,2])
    print(3 == rtn)
    rtn = solution.singleNumber([0,1,0,1,0,1,99])
    print(99 == rtn)