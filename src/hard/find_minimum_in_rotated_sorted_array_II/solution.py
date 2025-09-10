#! /usr/bin/python3
# -*- coding:utf8 -*-

# Copyright 2025 Robina Li. BSD 3-Clause License All Rights Reserved.
# @file : solution.py
# @desc : Solution for Leetcode
# Reference : https://leetcode.com/problems/find-minimum-in-rotated-sorted-array-ii/

from typing import List

class Solution(object):
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        while left < right:
            pivot = (left + right) >> 1
            if nums[pivot] < nums[right]:
                right = pivot
            elif nums[pivot] > nums[right]:
                left = pivot + 1
            else:
                right -= 1
        return nums[left]
 
if __name__ == '__main__':
    solution = Solution()
    rtn = solution.findMin([1,3,5])
    print(1 == rtn)
    rtn = solution.findMin([2,2,2,0,1])
    print(0 == rtn)