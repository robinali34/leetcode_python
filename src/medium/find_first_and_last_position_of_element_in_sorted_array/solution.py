#! /usr/bin/python3
# -*- coding:utf8 -*-

# Copyright 2025 Robina Li. BSD 3-Clause License All Rights Reserved.
# @file : solution.py
# @desc : Solution for Leetcode
# Reference : https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def bs(nums, target, find_first):
            left, right = 0, len(nums) -1
            rtn = -1
            while left <= right:
                mid = (left + right) //2
                if nums[mid] == target:
                    rtn = mid
                    if find_first:
                        right = mid -1
                    else:
                        left = mid + 1
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return rtn
        return [bs(nums, target, True), bs(nums, target, False)]


if __name__ == '__main__':
    solution = Solution()

    rtn = solution.searchRange([5,7,7,8,8,10], 8)
    print([3,4] == rtn)
    rtn = solution.searchRange([5,7,7,8,8,10], 6)
    print([-1,-1] == rtn)
    rtn = solution.searchRange([], 0)
    print([-1,-1] == rtn)