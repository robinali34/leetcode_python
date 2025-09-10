#! /usr/bin/python3
# -*- coding:utf8 -*-

# Copyright 2025 Robina Li. BSD 3-Clause License All Rights Reserved.
# @file : solution.py
# @desc : Solution for Leetcode
# Reference : https://leetcode.com/problems/n-queens/

from typing import List

class Solution(object):

    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        empty_cells = []
        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if val == ".":
                    empty_cells.append((r, c))
                else:
                    rows[r].add(val)
                    cols[c].add(val)
                    box_idx = (r // 3) * 3 + (c // 3)
                    boxes[box_idx].add(val)
        def backtrack(i):
            if i == len(empty_cells):
                return True
            r, c = empty_cells[i]
            box_idx = (r // 3) * 3 + (c // 3)
            for num in '123456789':
                if num not in rows[r] and num not in cols[c] \
                    and num not in boxes[box_idx]:
                    board[r][c] = num
                    rows[r].add(num)
                    cols[c].add(num)
                    boxes[box_idx].add(num)
                    if backtrack(i + 1):
                        return True
                    board[r][c] = "."
                    rows[r].remove(num)
                    cols[c].remove(num)
                    boxes[box_idx].remove(num)
            return False
        backtrack(0)

    def solveSudoku1(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        empty_cells = []
        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if val == ".":
                    empty_cells.append((r, c))
                else:
                    rows[r].add(val)
                    cols[c].add(val)
                    box_idx = (r // 3) * 3 + (c // 3)
                    boxes[box_idx].add(val)
        def backtrack(i):
            if i == len(empty_cells):
                return True
            r, c = empty_cells[i]
            box_idx = (r // 3) * 3 + (c // 3)
            for num in '123456789':
                if num not in rows[r] and num not in cols[c] \
                    and num not in boxes[box_idx]:
                    board[r][c] = num
                    rows[r].add(num)
                    cols[c].add(num)
                    boxes[box_idx].add(num)
                    if backtrack(i + 1):
                        return True
                    board[r][c] = "."
                    rows[r].remove(num)
                    cols[c].remove(num)
                    boxes[box_idx].remove(num)
            return False
        backtrack(0)

if __name__ == '__main__':
    solution = Solution()

    board = [[".",".",".",".",".",".",".",".","."],[".","9",".",".","1",".",".","3","."],[".",".","6",".","2",".","7",".","."],[".",".",".","3",".","4",".",".","."],["2","1",".",".",".",".",".","9","8"],[".",".",".",".",".",".",".",".","."],[".",".","2","5",".","6","4",".","."],[".","8",".",".",".",".",".","1","."],[".",".",".",".",".",".",".",".","."]]
    solution.solveSudoku(board)
    print([['7', '2', '1', '8', '5', '3', '9', '4', '6'], ['4', '9', '5', '6', '1', '7', '8', '3', '2'], ['8', '3', '6', '4', '2', '9', '7', '5', '1'], ['9', '6', '7', '3', '8', '4', '1', '2', '5'], ['2', '1', '4', '7', '6', '5', '3', '9', '8'], ['3', '5', '8', '2', '9', '1', '6', '7', '4'], ['1', '7', '2', '5', '3', '6', '4', '8', '9'], ['6', '8', '3', '9', '4', '2', '5', '1', '7'], ['5', '4', '9', '1', '7', '8', '2', '6', '3']] == board)

    board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
    rtn = solution.solveSudoku(board)
    print([["5","3","4","6","7","8","9","1","2"],["6","7","2","1","9","5","3","4","8"],["1","9","8","3","4","2","5","6","7"],["8","5","9","7","6","1","4","2","3"],["4","2","6","8","5","3","7","9","1"],["7","1","3","9","2","4","8","5","6"],["9","6","1","5","3","7","2","8","4"],["2","8","7","4","1","9","6","3","5"],["3","4","5","2","8","6","1","7","9"]] == board)

    board = [[".",".",".",".",".",".",".",".","."],[".","9",".",".","1",".",".","3","."],[".",".","6",".","2",".","7",".","."],[".",".",".","3",".","4",".",".","."],["2","1",".",".",".",".",".","9","8"],[".",".",".",".",".",".",".",".","."],[".",".","2","5",".","6","4",".","."],[".","8",".",".",".",".",".","1","."],[".",".",".",".",".",".",".",".","."]]
    solution.solveSudoku1(board)
    print([['7', '2', '1', '8', '5', '3', '9', '4', '6'], ['4', '9', '5', '6', '1', '7', '8', '3', '2'], ['8', '3', '6', '4', '2', '9', '7', '5', '1'], ['9', '6', '7', '3', '8', '4', '1', '2', '5'], ['2', '1', '4', '7', '6', '5', '3', '9', '8'], ['3', '5', '8', '2', '9', '1', '6', '7', '4'], ['1', '7', '2', '5', '3', '6', '4', '8', '9'], ['6', '8', '3', '9', '4', '2', '5', '1', '7'], ['5', '4', '9', '1', '7', '8', '2', '6', '3']] == board)

    board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
    rtn = solution.solveSudoku1(board)
    print([["5","3","4","6","7","8","9","1","2"],["6","7","2","1","9","5","3","4","8"],["1","9","8","3","4","2","5","6","7"],["8","5","9","7","6","1","4","2","3"],["4","2","6","8","5","3","7","9","1"],["7","1","3","9","2","4","8","5","6"],["9","6","1","5","3","7","2","8","4"],["2","8","7","4","1","9","6","3","5"],["3","4","5","2","8","6","1","7","9"]] == board)
