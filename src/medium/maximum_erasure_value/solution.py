#! /usr/bin/python3
# -*- coding:utf8 -*-

# Copyright 2025 Robina Li. BSD 3-Clause License All Rights Reserved.
# @file : solution.py
# @desc : Solution for Leetcode
# Reference : https://leetcode.com/problems/maximum-erasure-value/

from functools import cache
from typing import List

class Solution(object):
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        sum_, max_sum, hashmap = 0, 0, {}
        start = 0
        for end in range(len(nums)):
            sum_ += nums[end]
            hashmap[nums[end]] = hashmap.get(nums[end], 0) + 1
            if end - start + 1 == len(hashmap):
                max_sum = max(max_sum, sum_)
            while end - start + 1 > len(hashmap):
                hashmap[nums[start]] -= 1
                if hashmap[nums[start]] == 0:
                    del hashmap[nums[start]]
                sum_ -= nums[start]
                start += 1
        return max_sum
 
if __name__ == '__main__':
    solution = Solution()
    rtn = solution.maximumUniqueSubarray([4,2,4,5,6])
    print(17 == rtn)
    rtn = solution.maximumUniqueSubarray([5,2,1,2,5,2,1,2,5])
    print(8 == rtn)