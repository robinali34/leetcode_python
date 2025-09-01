#! /usr/bin/python3
# -*- coding:utf8 -*-

# Copyright 2025 Robina Li. BSD 3-Clause License All Rights Reserved.
# @file : solution.py
# @desc : Solution for Leetcode
# Reference : https://leetcode.com/problems/permutation-in-string/

from functools import cache
from typing import List

class Solution(object):
    def checkInclusion(self, s1: str, s2: str) -> bool:
        hashmap1 = {}
        hashmap = {}
        for char in s1:
            hashmap1[char] = hashmap1.get(char, 0) + 1
        start = 0
        for end in range(len(s2)):
            hashmap[s2[end]] = hashmap.get(s2[end], 0) + 1
            if hashmap == hashmap1:
                return True
            if end >= len(s1) - 1:
                hashmap[s2[start]] -= 1
                if hashmap[s2[start]] == 0:
                    del hashmap[s2[start]]
                start += 1
        return False
 
if __name__ == '__main__':
    solution = Solution()
    rtn = solution.checkInclusion("ab", "eidbaooo")
    print(True == rtn)
    rtn = solution.checkInclusion("ab", "eidboaoo")
    print(False == rtn)