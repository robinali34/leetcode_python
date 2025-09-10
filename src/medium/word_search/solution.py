#! /usr/bin/python3
# -*- coding:utf8 -*-

# Copyright 2025 Robina Li. BSD 3-Clause License All Rights Reserved.
# @file : solution.py
# @desc : Solution for Leetcode
# Reference : https://leetcode.com/problems/word-search/

from functools import cache
from typing import List
import math

class Solution(object):
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])

        def backtrack(r: int, c: int, i: int) -> None:
            if i == len(word):
                return True
            if r < 0 or r >= rows or c < 0 or c >= cols or board[r][c] != word[i]:
                return False
            tmp = board[r][c]
            board[r][c] = '#'

            found = backtrack(r + 1, c, i + 1) or \
                    backtrack(r, c + 1, i + 1) or \
                    backtrack(r - 1, c, i + 1) or \
                    backtrack(r, c - 1, i + 1)
            board[r][c] = tmp
            return found
        
        for r in range(rows):
            for c in range(cols):
                if backtrack(r, c, 0):
                    return True
        return False

if __name__ == '__main__':
    solution = Solution()
    rtn = solution.exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCCED")
    print(True == rtn)
    rtn = solution.exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "SEE")
    print(True == rtn)
    rtn = solution.exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCB")
    print(False == rtn)