#! /usr/bin/python3
# -*- coding:utf8 -*-

# Copyright 2025 Robina Li. BSD 3-Clause License All Rights Reserved.
# @file : solution.py
# @desc : Solution for Leetcode
# Reference : https://leetcode.com/problems/palindrome-partitioning/

from functools import cache
from typing import List
import math

class Solution(object):
    def partition(self, s: str) -> List[List[str]]:
        rtn = []

        def is_palindrome(sub: str) -> None:
            return sub == sub[::-1]

        def backtrack(start: int, path: List[str]) -> None:
            if start == len(s):
                rtn.append(path[:])
                return
            for end in range(start, len(s)):
                substr = s[start: end + 1]
                if is_palindrome(substr):
                    path.append(substr)
                    backtrack(end + 1, path)
                    path.pop()
        backtrack(0, [])
        return rtn

if __name__ == '__main__':
    solution = Solution()
    rtn = solution.partition("aab")
    print([["a","a","b"],["aa","b"]] == rtn)
    rtn = solution.partition("a")
    print([["a"]] == rtn)