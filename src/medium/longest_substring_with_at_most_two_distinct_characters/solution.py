#! /usr/bin/python3
# -*- coding:utf8 -*-

# Copyright 2025 Robina Li. BSD 3-Clause License All Rights Reserved.
# @file : solution.py
# @desc : Solution for Leetcode
# Reference : https://leetcode.com/problems/longest-substring-without-repeating-characters/description/

from functools import cache
from typing import List
import math

class Solution(object):
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        max_len, hashmap = 0, {}
        start = 0
        for end in range(len(s)):
            hashmap[s[end]] = hashmap.get(s[end], 0) + 1
            if len(hashmap) <= 2:
                max_len = max(max_len, end-start+1)
            while len(hashmap) > 2:
                hashmap[s[start]] -= 1
                if hashmap[s[start]] == 0:
                    del hashmap[s[start]]
                start += 1
        return max_len
 
if __name__ == '__main__':
    solution = Solution()
    rtn = solution.lengthOfLongestSubstringTwoDistinct("eceba")
    print(3 == rtn)
    rtn = solution.lengthOfLongestSubstringTwoDistinct("ccaabbb")
    print(5 == rtn)