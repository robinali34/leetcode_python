#! /usr/bin/python3
# -*- coding:utf8 -*-

# Copyright 2025 Robina Li. BSD 3-Clause License All Rights Reserved.
# @file : solution.py
# @desc : Solution for Leetcode
# Reference : https://leetcode.com/problems/n-queens/

from typing import List

class Solution(object):
    def solveNQueens(self, n: int) -> List[List[str]]:
        rtn = []
        def backtrack(row: int, cols: List[int], pos_diags: List[int], neg_diags: List[int], board: List[List[str]]) -> None:
            if row == n:
                rtn.append(["".join(r) for r in board])
                return
            for col in range(n):
                if col in cols or (row + col) in pos_diags or (row - col) in neg_diags:
                    continue
                board[row][col] = 'Q'
                cols.add(col)
                pos_diags.add(row + col)
                neg_diags.add(row - col)
                
                backtrack(row + 1, cols, pos_diags, neg_diags, board)

                board[row][col] = '.'
                cols.remove(col)
                pos_diags.remove(row + col)
                neg_diags.remove(row - col)
        empty_board = [["."] * n for _ in range(n)]
        backtrack(0, set(), set(), set(), empty_board)
        return rtn

if __name__ == '__main__':
    solution = Solution()
    rtn = solution.solveNQueens(4)
    print([[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]] == rtn)
    rtn = solution.solveNQueens(1)
    print([["Q"]] == rtn)