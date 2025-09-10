#! /usr/bin/python3
# -*- coding:utf8 -*-

# Copyright 2025 Robina Li. BSD 3-Clause License All Rights Reserved.
# @file : solution.py
# @desc : Solution for Leetcode
# Reference : https://leetcode.com/problems/single-number-iii/

from typing import List

class Solution(object):
    def singleNumber(self, nums: List[int]) -> List[int]:
        bitmask = 0
        for num in nums:
            bitmask ^= num
        diff = bitmask & (-bitmask)
        x = 0
        for num in nums:
            if num & diff:
                x ^= num
        return [x, bitmask^x]
 
if __name__ == '__main__':
    solution = Solution()
    rtn = solution.singleNumber([1,2,1,3,2,5])
    print([3,5] == rtn)
    rtn = solution.singleNumber([-1,0])
    print([-1,0] == rtn)
    rtn = solution.singleNumber([0,1])
    print([1,0] == rtn)