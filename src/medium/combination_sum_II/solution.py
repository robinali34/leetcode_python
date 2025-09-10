#! /usr/bin/python3
# -*- coding:utf8 -*-

# Copyright 2025 Robina Li. BSD 3-Clause License All Rights Reserved.
# @file : solution.py
# @desc : Solution for Leetcode
# Reference : https://leetcode.com/problems/combination-sum-ii/

from functools import cache
from typing import List
import math

class Solution(object):
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        rtn = []

        def backtrack(start: int, path: List[int], total) -> None:
            if total == target:
                rtn.append(path[:])
                return
            if total > target:
                return
            for i in range(start, len(candidates)):
                # Remove duplicates: same element start used
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                path.append(candidates[i])
                backtrack(i + 1, path, total + candidates[i])
                path.pop()
        backtrack(0, [], 0)
        return rtn
 
if __name__ == '__main__':
    solution = Solution()
    rtn = solution.combinationSum2([10,1,2,7,6,1,5], 8)
    print([[1,1,6],[1,2,5],[1,7],[2,6]] == rtn)
    rtn = solution.combinationSum2([2,5,2,1,2], 5)
    print([[1,2,2],[5]] == rtn)