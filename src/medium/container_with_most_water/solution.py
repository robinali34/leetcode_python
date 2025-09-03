#! /usr/bin/python3
# -*- coding:utf8 -*-

# Copyright 2025 Robina Li. BSD 3-Clause License All Rights Reserved.
# @file : solution.py
# @desc : Solution for Leetcode
# Reference : https://leetcode.com/problems/container-with-most-water/

from typing import List

class Solution(object):
    def maxArea(self, height: List[int]) -> int:
        max_water, left, right = 0, 0, len(height) - 1
        while left < right:
            width = right - left
            max_water = max(max_water, min(height[left], height[right]) * width)
            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1
        return max_water

if __name__ == '__main__':
    solution = Solution()
    rtn = solution.maxArea([1,8,6,2,5,4,8,3,7])
    print(49 == rtn)
    rtn = solution.maxArea([1,1])
    print(1 == rtn)