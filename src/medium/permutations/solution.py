#! /usr/bin/python3
# -*- coding:utf8 -*-

# Copyright 2025 Robina Li. BSD 3-Clause License All Rights Reserved.
# @file : solution.py
# @desc : Solution for Leetcode
# Reference : https://leetcode.com/problems/permutations/

from typing import List

class Solution(object):
    def permute(self, nums: List[int]) -> List[List[int]]:
        rtn = []
        def backtrack(path: List[int], used: List[bool]) -> None:
            if len(path) == len(nums):
                rtn.append(path[:])
                return
            for i in range(len(nums)):
                if not used[i]:
                    used[i] = True
                    path.append(nums[i])
                    backtrack(path, used)
                    path.pop()
                    used[i] = False
        backtrack([], [False] * len(nums))
        return rtn

    def permute1(self, nums: List[int]) -> List[List[int]]:
        res = []
        def dfs(start: int) -> None:
            if start == len(nums):
                res.append(nums[:])
                return
            for i in range(start, len(nums)):
                nums[start], nums[i] = nums[i], nums[start]
                dfs(start + 1)
                nums[start], nums[i] = nums[i], nums[start]
        dfs(0)
        return res
 
    def permute2(self, nums: List[int]) -> List[List[int]]:
        res = []
        used = [False] * len(nums)
        def backtrack(path):
            if len(path) == len(nums):
                res.append(path[:])
                return
            for i in range(len(nums)):
                if used[i]:
                    continue
                used[i] = True
                path.append(nums[i])
                backtrack(path)
                path.pop()
                used[i] = False
        backtrack([])
        return res

if __name__ == '__main__':
    solution = Solution()
    rtn = solution.permute([1,2,3])
    print([[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]] == rtn)
    rtn = solution.permute([0,1])
    print([[0,1],[1,0]] == rtn)
    rtn = solution.permute([1])
    print([[1]] == rtn)

    rtn = solution.permute1([1,2,3])
    print([[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]] == rtn)
    rtn = solution.permute1([0,1])
    print([[0,1],[1,0]] == rtn)
    rtn = solution.permute1([1])
    print([[1]] == rtn)

    rtn = solution.permute2([1,2,3])
    print([[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]] == rtn)
    rtn = solution.permute2([0,1])
    print([[0,1],[1,0]] == rtn)
    rtn = solution.permute2([1])
    print([[1]] == rtn)