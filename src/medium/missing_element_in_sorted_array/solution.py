#! /usr/bin/python3
# -*- coding:utf8 -*-

# Copyright 2025 Robina Li. BSD 3-Clause License All Rights Reserved.
# @file : solution.py
# @desc : Solution for Leetcode
# Reference : https://leetcode.com/problems/missing-element-in-sorted-array/

from typing import List

class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:
        def missing(i: int) -> int:
            return nums[i] - nums[0] - i

        n = len(nums)
        
        if k > missing(n - 1):
            return nums[-1] + k - missing(n - 1)
        
        left, right = 0, n - 1
        while left < right:
            pivot = left + (right - left) // 2
            if missing(pivot) < k:
                left = pivot + 1
            else:
                right = pivot

        return nums[left - 1] + k - missing(left - 1)

if __name__ == '__main__':
    solution = Solution()
    nums = [4, 7, 9, 10]
    rtn = solution.missingElement(nums, 1)
    print(5 == rtn)
    nums = [4,7,9,10]
    rtn = solution.missingElement(nums, 3)
    print(8 == rtn)
    nums = [1,2,4]
    rtn = solution.missingElement(nums, 3)
    print(6 == rtn)