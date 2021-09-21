#! /usr/bin/python3
# -*- coding:utf8 -*-

# Copyright 2021 Robina Li. BSD 3-Clause License All Rights Reserved.
# @file : solution.py
# @desc : Solution for Leetcode
# Reference : https://leetcode.com/problems/rotate-array

from typing import List

class Solution(object):
    def rotate(self,nums:List[int], k: int) -> None:
        # In-place modification
        k = k % len(nums)
        if k != 0: nums[:] = nums[-k :] + nums[:len(nums) - k]

    def rotate1(self, nums: List[int], k: int) -> None:
        # Rotate:
        # 1. Revert all
        # 2. Revert idx 0 to k - 1
        # 3. Revert k to end
        n = len(nums)
        k = k % n
        self._revert(nums, 0, n -1)
        self._revert(nums, k, n -1)
        self._revert(nums, 0, k - 1)

    @staticmethod
    def _revert(nums: List[int], start:int, end:int) -> None:
        while (start < end):
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1


if __name__ == '__main__':
    solution = Solution()
    nums = [1,2,3,4,5,6,7]
    solution.rotate(nums, 3)
    print([5,6,7,1,2,3,4] == nums)
    nums = [-1,-100,3,99]
    solution.rotate(nums, 2)
    print([3,99,-1,-100] == nums)