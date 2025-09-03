#! /usr/bin/python3
# -*- coding:utf8 -*-

# Copyright 2025 Robina Li. BSD 3-Clause License All Rights Reserved.
# @file : solution.py
# @desc : Solution for Leetcode
# Reference : https://leetcode.com/problems/3sum-closest/

from typing import List

class Solution(object):
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        closest = float('inf')
        for i in range(len(nums) - 2):
            left, right = i + 1, len(nums) - 1
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if abs(target - total) < abs(target - closest):
                    closest = total
                if total < target:
                    left += 1
                elif total > target:
                    right -= 1
                else:
                    return total
        return closest
 
if __name__ == '__main__':
    solution = Solution()
    rtn = solution.threeSumClosest([-1,2,1,-4], 1)
    print(2 == rtn)
    rtn = solution.threeSumClosest([0,0,0], 1)
    print(0 == rtn)