#! /usr/bin/python3
# -*- coding:utf8 -*-

# Copyright 2025 Robina Li. BSD 3-Clause License All Rights Reserved.
# @file : solution.py
# @desc : Solution for Leetcode
# Reference : https://leetcode.com/problems/subsets/

from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        rtn = []
        def backtrack(start: int, path: List[int]) -> None:
            rtn.append(path[:])
            for i in range(start, len(nums)):
                path.append(nums[i])
                backtrack(i+1, path)
                path.pop()
        backtrack(0, [])
        return rtn

if __name__ == '__main__':
    solution = Solution()

    rtn = solution.subsets([1,2,3])
    print([[],[1],[1,2],[1,2,3],[1,3],[2],[2,3],[3]] == rtn)
    rtn = solution.subsets([0])
    print([[],[0]] == rtn)