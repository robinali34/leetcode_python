#! /usr/bin/python3
# -*- coding:utf8 -*-

# Copyright 2025 Robina Li. BSD 3-Clause License All Rights Reserved.
# @file : solution.py
# @desc : Solution for Leetcode
# Reference : https://leetcode.com/problems/max-difference-you-can-get-from-changing-an-integer/

from typing import List
import math

class Solution:
    def maxDiff(self, num: int) -> int:
        min_num = max_num = str(num)
        for digit in max_num:
            if digit != '9':
                max_num = max_num.replace(digit, '9')
                break
        for i, digit in enumerate(min_num):
            if i == 0:
                if digit != '1':
                    min_num = min_num.replace(digit, '1')
                    break
            else:
                if digit != '0' and digit != min_num[0]:
                    min_num = min_num.replace(digit, '0')
                    break
        return int(max_num) - int (min_num)

if __name__ == '__main__':
    solution = Solution()

    rtn = solution.maxDiff(555)
    print(888 == rtn)
    rtn = solution.maxDiff(9)
    print(8 == rtn)