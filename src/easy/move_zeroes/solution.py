#! /usr/bin/python3
# -*- coding:utf8 -*-

# Copyright 2025 Robina Li. BSD 3-Clause License All Rights Reserved.
# @file : solution.py
# @desc : Solution for Leetcode
# Reference : https://leetcode.com/problems/move-zeroes/description/

from typing import List
from functools import cache

class Solution(object):
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left = 0
        for right in range(len(nums)):
            if nums[right] != 0:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1

if __name__ == '__main__':
    solution = Solution()

    nums = [0,1,0,3,12]
    solution.moveZeroes(nums)
    print([1,3,12,0,0] == nums)
    nums = [0]
    solution.moveZeroes(nums)
    print([0] == nums)