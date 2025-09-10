#! /usr/bin/python3
# -*- coding:utf8 -*-

# Copyright 2025 Robina Li. BSD 3-Clause License All Rights Reserved.
# @file : solution.py
# @desc : Solution for Leetcode
# Reference : https://leetcode.com/problems/generate-parentheses/

from functools import cache
from typing import List
import math

class Solution(object):
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def backtrack(left: int, right: int, s: str) -> None:
            if len(s) == n * 2:
                res.append(s)
                return
            if left < n:
                backtrack(left + 1, right, s + '(')
            if left > right:
                backtrack(left, right + 1, s + ')')
        backtrack(0, 0, "")
        return res
        
    def generateParenthesis1(self, n: int) -> List[str]:
        res = []
        def backtrack(left: int, right: int, s: str) -> None:
            if len(s) == n * 2:
                res.append(s)
                return
            else:
                if left < n:
                    backtrack(left + 1, right, s + '(')
                if left > right:
                    backtrack(left, right + 1, s + ')')
        backtrack(0, 0, "")
        return res
 
if __name__ == '__main__':
    solution = Solution()
    rtn = solution.generateParenthesis(3)
    print(["((()))","(()())","(())()","()(())","()()()"] == rtn)
    rtn = solution.generateParenthesis(1)
    print(["()"] == rtn)

    rtn = solution.generateParenthesis1(3)
    print(["((()))","(()())","(())()","()(())","()()()"] == rtn)
    rtn = solution.generateParenthesis1(1)
    print(["()"] == rtn)