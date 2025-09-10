#! /usr/bin/python3
# -*- coding:utf8 -*-

# Copyright 2025 Robina Li. BSD 3-Clause License All Rights Reserved.
# @file : solution.py
# @desc : Solution for Leetcode
# Reference : https://leetcode.com/problems/permutations-ii/

from typing import List

class Solution(object):

    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        rtn = []
        def backtrack(path: List[int], used: List[bool]) -> None:
            if len(path) == len(nums):
                rtn.append(path[:])
                return
            for i in range(len(nums)):
                if used[i]:
                    continue
                if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]:
                    continue
                used[i] = True
                path.append(nums[i])
                backtrack(path, used)
                path.pop()
                used[i] = False
        backtrack([], [False] * len(nums))
        return rtn

if __name__ == '__main__':
    solution = Solution()
    rtn = solution.permuteUnique([1,1,2])
    print([[1,1,2],[1,2,1],[2,1,1]] == rtn)
    rtn = solution.permuteUnique([1,2,3])
    print([[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]] == rtn)
