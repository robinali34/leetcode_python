#! /usr/bin/python3
# -*- coding:utf8 -*-

# Copyright 2025 Robina Li. BSD 3-Clause License All Rights Reserved.
# @file : solution.py
# @desc : Solution for Leetcode
# Reference : https://leetcode.com/problems/combination-sum-iii/

from functools import cache
from typing import List
import math

class Solution(object):
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        rtn = []
        def backtrack(start: int, path: List[int], total: int) -> None:
            if len(path) == k:
                if total == n:
                    rtn.append(path[:])
                return
            for i in range(start, 10):
                if total + i > n:
                    break
                path.append(i)
                backtrack(i + 1, path, total + i)
                path.pop()
        backtrack(1, [], 0)
        return rtn
 
if __name__ == '__main__':
    solution = Solution()
    rtn = solution.combinationSum3(3, 7)
    print([[1,2,4]] == rtn)
    rtn = solution.combinationSum3(3, 9)
    print([[1,2,6],[1,3,5],[2,3,4]] == rtn)
    rtn = solution.combinationSum3(4, 1)
    print([] == rtn)