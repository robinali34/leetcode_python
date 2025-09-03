#! /usr/bin/python3
# -*- coding:utf8 -*-

# Copyright 2025 Robina Li. BSD 3-Clause License All Rights Reserved.
# @file : solution.py
# @desc : Solution for Leetcode
# Reference : https://leetcode.com/problems/minimum-window-substring/

from typing import List
from collections import Counter

class Solution(object):
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""
        t_count = Counter(t)
        window_counts = {}
        formed = left = 0
        rtn = float("inf"), None, None
        for right in range(len(s)):
            char = s[right]
            window_counts[char] = window_counts.get(char, 0) + 1
            if char in t_count and window_counts[char] == t_count[char]:
                formed += 1
            while left <= right and formed == len(t_count):
                if right - left + 1 < rtn[0]:
                    rtn = (right - left + 1, left, right)
                window_counts[s[left]] -= 1
                if s[left] in t_count and window_counts[s[left]] < t_count[s[left]]:
                    formed -= 1
                left += 1
        return "" if rtn[0] == float("inf") else s[rtn[1]:rtn[2] + 1]
 
if __name__ == '__main__':
    solution = Solution()
    rtn = solution.minWindow("ADOBECODEBANC", "ABC")
    print("BANC" == rtn)
    rtn = solution.minWindow("a","a")
    print("a" == rtn)
    rtn = solution.minWindow("aa","")
    print("" == rtn)