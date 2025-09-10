#! /usr/bin/python3
# -*- coding:utf8 -*-

# Copyright 2025 Robina Li. BSD 3-Clause License All Rights Reserved.
# @file : solution.py
# @desc : Solution for Leetcode
# Reference : https://leetcode.com/problems/subsets-ii/

from typing import List

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        rtn = []
        def backtrack(start: int, path: List[int]) -> None:
            rtn.append(path[:])
            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i - 1]:
                    continue
                path.append(nums[i])
                backtrack(i + 1, path)
                path.pop()
        backtrack(0, [])
        return rtn

if __name__ == '__main__':
    solution = Solution()

    rtn = solution.subsetsWithDup([1,2,2])
    print([[],[1],[1,2],[1,2,2],[2],[2,2]] == rtn)
    rtn = solution.subsetsWithDup([0])
    print([[],[0]] == rtn)