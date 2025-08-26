#! /usr/bin/python3
# -*- coding:utf8 -*-

# Copyright 2025 Robina Li. BSD 3-Clause License All Rights Reserved.
# @file : solution.py
# @desc : Solution for Leetcode
# Reference : https://leetcode.com/problems/product-of-array-except-self

from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        size = len(nums)
        ans = [1] * size

        L = 1
        for i in range(size):
            ans[i] *= L
            L *= nums[i]
        R = 1
        for i in range(size - 1, -1, -1):
            ans[i] *= R
            R *= nums[i]

        return ans

    def productExceptSelf1(self, nums: List[int]) -> List[int]:
        size = len(nums)
        ans = [1] * size
        for i in range(size):
            for j in range(0, i):
                ans[i] *= nums[j]
            for j in range(i+1, len(nums)):
                ans[i] *= nums[j]
        return ans

    def productExceptSelf2(self, nums: List[int]) -> List[int]:
        size = len(nums)
        L, R, ans = [1] * size, [1] * size, [1] * size
        for i in range(1, size):
            L[i] = nums[i - 1] * L[i - 1]
            R[size - i - 1] = nums[size - i] * R[size - i]
        for i in range(size):
            ans[i] = L[i] * R[i]
        return ans

    def productExceptSelf3(self, nums: List[int]) -> List[int]:
        size = len(nums)
        ans = [1] * size

        for i in range(1, size):
            ans[i] = nums[i-1] * ans[i - 1]
        R = 1
        for i in range(size - 1, -1, -1):
            ans[i] *= R
            R *= nums[i]

        return ans

if __name__ == '__main__':
    solution = Solution()

    rtn = solution.productExceptSelf([1,2,3,4])
    print([24,12,8,6] == rtn)
    rtn = solution.productExceptSelf([-1,1,0,-3,3])
    print([0,0,9,0,0] == rtn)

    rtn = solution.productExceptSelf1([1,2,3,4])
    print([24,12,8,6] == rtn)
    rtn = solution.productExceptSelf1([-1,1,0,-3,3])
    print([0,0,9,0,0] == rtn)

    rtn = solution.productExceptSelf2([1,2,3,4])
    print([24,12,8,6] == rtn)
    rtn = solution.productExceptSelf2([-1,1,0,-3,3])
    print([0,0,9,0,0] == rtn)

    rtn = solution.productExceptSelf3([1,2,3,4])
    print([24,12,8,6] == rtn)
    rtn = solution.productExceptSelf3([-1,1,0,-3,3])
    print([0,0,9,0,0] == rtn)