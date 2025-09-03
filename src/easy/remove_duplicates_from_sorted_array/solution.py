#! /usr/bin/python3
# -*- coding:utf8 -*-

# Copyright 2025 Robina Li. BSD 3-Clause License All Rights Reserved.
# @file : solution.py
# @desc : Solution for Leetcode
# Reference : https://leetcode.com/problems/remove-duplicates-from-sorted-array/

from typing import List

class Solution(object):
    def removeDuplicates(self, nums: List[int]) -> int:
        left = 1
        for right in range(1, len(nums)):
            if nums[right - 1] != nums[right]:
                nums[left] = nums[right]
                left += 1
        return left

    def removeDuplicates1(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        idx = 0
        # Two pointers, i at original array index, idx at return index
        for i in range(1, n):
            if nums[idx] != nums[i]:
                idx += 1
                nums[idx] = nums[i]
        return idx + 1

if __name__ == '__main__':
    solution = Solution()

    nums = [1,1,2]
    k = solution.removeDuplicates(nums)
    print([1,2] == nums[:k])
    nums = [0,0,1,1,1,2,2,3,3,4]
    k = solution.removeDuplicates(nums)
    print([0,1,2,3,4] == nums[:k])

    nums = [1,1,2]
    k = solution.removeDuplicates1(nums)
    print([1,2] == nums[:k])
    nums = [0,0,1,1,1,2,2,3,3,4]
    k = solution.removeDuplicates1(nums)
    print([0,1,2,3,4] == nums[:k])