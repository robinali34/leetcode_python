#! /usr/bin/python3
# -*- coding:utf8 -*-

# Copyright 2025 Robina Li. BSD 3-Clause License All Rights Reserved.
# @file : solution.py
# @desc : Solution for Leetcode
# Reference : https://leetcode.com/problems/search-a-2d-matrix/

from typing import List
import math

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        if m == 0:
            return False
        n = len(matrix[0])
        left, right = 0, m * n -1
        while left <= right:
            pivot_idx = (left + right) // 2
            pivot_data = matrix[pivot_idx // n][pivot_idx % n]
            if target == pivot_data:
                return True
            elif target < pivot_data:
                right = pivot_idx - 1
            else:
                left = pivot_idx + 1
        return False

if __name__ == '__main__':
    solution = Solution()

    rtn = solution.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 3)
    print(True == rtn)
    rtn = solution.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 13)
    print(False == rtn)