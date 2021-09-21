#! /usr/bin/python3
# -*- coding:utf8 -*-

# Copyright 2021 Robina Li. BSD 3-Clause License All Rights Reserved.
# @file : solution.py
# @desc : Solution for Leetcode
# Reference : https://leetcode.com/problems/remove-duplicates-from-sorted-array/

from typing import List

class Solution(object):
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        idx = 0
        # Two pointers, i at original array index, idx at return index
        for i in range(1, n):
            if nums[idx] != nums[i]:
                idx += 1
                nums[idx] = nums[i]
        return idx + 1

if __name__ == '__main__':
    solution = Solution()
    print(2 == solution.removeDuplicates([1, 2, 2]))
    print(5 == solution.removeDuplicates([0,0,1,1,1,2,2,3,3,4]))