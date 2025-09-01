#! /usr/bin/python3
# -*- coding:utf8 -*-

# Copyright 2025 Robina Li. BSD 3-Clause License All Rights Reserved.
# @file : solution.py
# @desc : Solution for Leetcode
# Reference : https://leetcode.com/problems/max-consecutive-ones-ii/

from functools import cache
from typing import List

class Solution(object):
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_len, hashmap = 0, {}
        start = 0
        for end in range(len(nums)):
            hashmap[nums[end]] = hashmap.get(nums[end], 0) + 1
            if hashmap.get(0, 0) <= 1:
                max_len = max(max_len, end - start + 1)
            while hashmap.get(0, 0) > 1:
                hashmap[nums[start]] -= 1
                start += 1
        return max_len

if __name__ == '__main__':
    solution = Solution()
    rtn = solution.findMaxConsecutiveOnes([1,0,1,1,0])
    print(4 == rtn)
    rtn = solution.findMaxConsecutiveOnes([1,0,1,1,0,1])
    print(4 == rtn)