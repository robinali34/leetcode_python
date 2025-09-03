#! /usr/bin/python3
# -*- coding:utf8 -*-

# Copyright 2025 Robina Li. BSD 3-Clause License All Rights Reserved.
# @file : solution.py
# @desc : Solution for Leetcode
# Reference : https://leetcode.com/problems/trapping-rain-water/

from typing import List

class Solution(object):
    def trap(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        left_max = right_max = water = 0
        while left < right:
            if height[left] < height[right]:
                if height[left] >= left_max:
                    left_max = height[left]
                else:
                    water += left_max - height[left]
                left += 1
            else:
                if height[right] >= right_max:
                    right_max = height[right]
                else:
                    water += right_max - height[right]
                right -= 1
        return water
 
if __name__ == '__main__':
    solution = Solution()
    rtn = solution.trap([0,1,0,2,1,0,1,3,2,1,2,1])
    print(6 == rtn)
    rtn = solution.trap([4,2,0,3,2,5])
    print(9 == rtn)