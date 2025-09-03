#! /usr/bin/python3
# -*- coding:utf8 -*-

# Copyright 2025 Robina Li. BSD 3-Clause License All Rights Reserved.
# @file : solution.py
# @desc : Solution for Leetcode
# Reference : https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

from functools import cache
from typing import List

class Solution(object):
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) -1
        while left < right:
            sum_ = numbers[left] + numbers[right]
            if sum_ == target:
                return [left + 1, right + 1]
            elif sum_ < target:
                left += 1
            else:
                right -= 1

if __name__ == '__main__':
    solution = Solution()
    rtn = solution.twoSum([2,7,11,15], 9)
    print([1,2] == rtn)
    rtn = solution.twoSum([2,3,4], 6)
    print([1,3] == rtn)
    rtn = solution.twoSum([-1,0], -1)
    print([1,2] == rtn)