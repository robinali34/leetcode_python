#! /usr/bin/python3
# -*- coding:utf8 -*-

# Copyright 2025 Robina Li. BSD 3-Clause License All Rights Reserved.
# @file : solution.py
# @desc : Solution for Leetcode
# Reference : https://leetcode.com/problems/get-equal-substrings-within-budget/

from typing import List

class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        cur_cost, max_len = 0, 0
        start = 0
        for end in range(len(t)):
            cur_cost += abs(ord(s[end]) - ord(t[end]))
            if cur_cost <= maxCost:
                max_len = max(max_len, end - start + 1)
            while cur_cost > maxCost:
                cur_cost -= abs(ord(s[start]) - ord(t[start]))
                start += 1
        return max_len


if __name__ == '__main__':
    solution = Solution()

    rtn = solution.equalSubstring("abcd", "bcdf", 3)
    print(3 == rtn)
    rtn = solution.equalSubstring("abcd", "cdef", 3)
    print(1 == rtn)
    rtn = solution.equalSubstring("abcd", "acde", 0)
    print(1 == rtn)