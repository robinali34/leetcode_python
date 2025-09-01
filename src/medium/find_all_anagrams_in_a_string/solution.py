#! /usr/bin/python3
# -*- coding:utf8 -*-

# Copyright 2025 Robina Li. BSD 3-Clause License All Rights Reserved.
# @file : solution.py
# @desc : Solution for Leetcode
# Reference : https://leetcode.com/problems/find-all-anagrams-in-a-string/

from functools import cache
from typing import List

class Solution(object):
    def findAnagrams(self, s: str, p: str) -> List[int]:
        res, hashmap = [], {}
        hashmap_p = {}
        for char in p:
            hashmap_p[char] = hashmap_p.get(char, 0) + 1
        start = 0
        for end in range(len(s)):
            hashmap[s[end]] = hashmap.get(s[end], 0) + 1
            if hashmap == hashmap_p:
                res.append(start)
            if end - start >= len(p) - 1:
                hashmap[s[start]] -= 1
                if hashmap[s[start]] == 0:
                    del hashmap[s[start]]
                start += 1
        return res
 
if __name__ == '__main__':
    solution = Solution()
    rtn = solution.findAnagrams("cbaebabacd", "abc")
    print([0,6] == rtn)
    rtn = solution.findAnagrams("abab", "ab")
    print([0,1,2] == rtn)