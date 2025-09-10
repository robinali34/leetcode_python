#! /usr/bin/python3
# -*- coding:utf8 -*-

# Copyright 2025 Robina Li. BSD 3-Clause License All Rights Reserved.
# @file : solution.py
# @desc : Solution for Leetcode
# Reference : https://leetcode.com/problems/search-in-rotated-sorted-array-ii/

from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        left, right = 0, len(nums) - 1
        while left <= right:
            pivot = (left + right) >> 1
            if nums[pivot] == target:
                return True
            elif nums[pivot] > nums[left]:
                if nums[left] <= target and nums[pivot] > target:
                    right = pivot - 1
                else:
                    left = pivot + 1
            elif nums[pivot] < nums[left]:
                if nums[right] >= target and nums[pivot] < target:
                    left = pivot + 1
                else:
                    right = pivot - 1
            else:
                left += 1
        return False


if __name__ == '__main__':
    solution = Solution()

    rtn = solution.search([2,5,6,0,0,1,2], 0)
    print(True == rtn)
    rtn = solution.search([2,5,6,0,0,1,2], 3)
    print(False == rtn)