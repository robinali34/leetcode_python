#! /usr/bin/python3
# -*- coding:utf8 -*-

# Copyright 2025 Robina Li. BSD 3-Clause License All Rights Reserved.
# @file : solution.py
# @desc : Solution for Leetcode
# Reference : https://leetcode.com/problems/3sum/

from functools import cache
from typing import List
import math

class Solution(object):
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            j, k = i + 1, len(nums) - 1
            while j < k:
                total = nums[i] + nums[j] + nums[k]
                if total > 0:
                    k -= 1
                elif total < 0:
                    j+= 1
                else:
                    ans.append([nums[i], nums[j], nums[k]])
                    while j < k and nums[j] == nums[j + 1]:
                        j += 1
                    while j < k and nums[k] == nums[k - 1]:
                        k -= 1
                    j += 1
                    k -= 1
        return ans
 
if __name__ == '__main__':
    solution = Solution()
    rtn = solution.threeSum([-1,0,1,2,-1,-4])
    print([[-1,-1,2],[-1,0,1]] == rtn)
    rtn = solution.threeSum([0,1,1])
    print([] == rtn)
    rtn = solution.threeSum([0,0,0])
    print([[0,0,0]] == rtn)