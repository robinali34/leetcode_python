#! /usr/bin/python3
# -*- coding:utf8 -*-

# Copyright 2025 Robina Li. BSD 3-Clause License All Rights Reserved.
# @file : solution.py
# @desc : Solution for Leetcode
# Reference : https://leetcode.com/problems/combination-sum/

from functools import cache
from typing import List
import math

class Solution(object):
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        rtn = []
        def backtrack(start: int, path: list[int], total: int) -> None:
            if total == target:
                rtn.append(path[:])
                return
            if total > target:
                return
            for i in range(start, len(candidates)):
                path.append(candidates[i])
                backtrack(i, path, total + candidates[i])
                path.pop()
        backtrack(0, [], 0)
        return rtn
 
if __name__ == '__main__':
    solution = Solution()
    rtn = solution.combinationSum([2,3,6,7], 7)
    print([[2,2,3],[7]] == rtn)
    rtn = solution.combinationSum([2,3,5], 8)
    print([[2,2,2,2],[2,3,3],[3,5]] == rtn)
    rtn = solution.combinationSum([2], 1)
    print([] == rtn)