#! /usr/bin/python3
# -*- coding:utf8 -*-

# Copyright 2025 Robina Li. BSD 3-Clause License All Rights Reserved.
# @file : solution.py
# @desc : Solution for Leetcode
# Reference : https://leetcode.com/problems/remove-element/

from typing import List
from functools import cache

class Solution(object):
    def removeElement(self, nums: List[int], val: int) -> int:
        left = 0
        for right in range(len(nums)):
            if nums[right] != val:
                nums[left] = nums[right]
                left += 1
        return left

if __name__ == '__main__':
    solution = Solution()

    nums = [3,2,2,3]
    k = solution.removeElement(nums, 3)
    print([2,2] == nums[:k])
    nums = [0,1,2,2,3,0,4,2]
    k = solution.removeElement(nums, 2)
    print([0,1,3,0,4] == nums[:k])