#! /usr/bin/python3
# -*- coding:utf8 -*-

# Copyright 2025 Robina Li. BSD 3-Clause License All Rights Reserved.
# @file : solution.py
# @desc : Solution for Leetcode
# Reference : https://leetcode.com/problems/two-sum

from typing import List
from collections import Counter

class Solution(object):
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        count = [0] * 26
        for ch1, ch2 in zip(s,t):
            count[ord(ch1) - ord('a')] += 1
            count[ord(ch2) - ord('a')] -= 1
        return all(c == 0 for c in count)

    def isAnagram1(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)

    def isAnagram2(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)

if __name__ == '__main__':
    solution = Solution()
    
    rtn = solution.isAnagram("anagram", "nagaram")
    print(True == rtn)
    rtn = solution.isAnagram("rat", "car")
    print(False == rtn)
    
    rtn = solution.isAnagram1("anagram", "nagaram")
    print(True == rtn)
    rtn = solution.isAnagram1("rat", "car")
    print(False == rtn)
    
    rtn = solution.isAnagram2("anagram", "nagaram")
    print(True == rtn)
    rtn = solution.isAnagram2("rat", "car")
    print(False == rtn)