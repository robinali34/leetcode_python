#! /usr/bin/python3
# -*- coding:utf8 -*-

# Copyright 2025 Robina Li. BSD 3-Clause License All Rights Reserved.
# @file : solution.py
# @desc : Solution for Leetcode
# Reference : https://leetcode.com/problems/binary-search/

from typing import List
import math

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 0:
            return -1
        left, right = 0, len(nums) -1
        while left <= right:
            pivot = (left + right) // 2
            if nums[pivot] == target:
                return pivot
            elif nums[pivot] < target:
                left = pivot + 1
            else:
                right = pivot - 1
        return -1

if __name__ == '__main__':
    solution = Solution()

    rtn = solution.search([-1,0,3,5,9,12], 9)
    print(4 == rtn)
    rtn = solution.search([-1,0,3,5,9,12], 2)
    print(-1 == rtn)