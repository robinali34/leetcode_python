#! /usr/bin/python3
# -*- coding:utf8 -*-

# Copyright 2025 Robina Li. BSD 3-Clause License All Rights Reserved.
# @file : solution.py
# @desc : Solution for Leetcode
# Reference : https://leetcode.com/problems/longest-substring-without-repeating-characters

from typing import List
from collections import Counter

class Solution:
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars = [None] * 128
        left = right = res = 0
        while right < len(s):
            r = s[right]
            idx = chars[ord(r)]
            if idx is not None and left <= idx < right:
                left = idx + 1
            res = max(res, right - left + 1)
            chars[ord(r)] = right
            right += 1
        return res

    def lengthOfLongestSubstring1(self, s: str) -> int:
        def check(start, end):
            chars = set()
            for i in range(start, end + 1):
                c = s[i]
                if c in chars:
                    return False
                chars.add(c)
            return True

        n = len(s)

        res = 0
        for i in range(n):
            for j in range(i, n):
                if check(i, j):
                    res = max(res, j - i + 1)
        return res

    def lengthOfLongestSubstring2(self, s: str) -> int:
        chars = Counter()
        left = right = res = 0
        while right < len(s):
            r = s[right]
            chars[r] += 1
            while chars[r] > 1:
                l = s[left]
                chars[l] -= 1
                left += 1
            res = max(res, right - left + 1)
            right += 1
        return res

    def lengthOfLongestSubstring3(self, s: str) -> int:
        n = len(s)
        ans = 0
        charToNextIdx = {}
        i = 0
        for j in range(n):
            if s[j] in charToNextIdx:
                i = max(charToNextIdx[s[j]], i)
            ans = max(ans, j - i + 1)
            charToNextIdx[s[j]] = j + 1
        return ans

if __name__ == '__main__':
    solution = Solution()

    rtn = solution.lengthOfLongestSubstring("abcabcbb")
    print(3 == rtn)
    rtn = solution.lengthOfLongestSubstring("bbbbb")
    print(1 == rtn)
    rtn = solution.lengthOfLongestSubstring("pwwkew")
    print(3 == rtn)


    rtn = solution.lengthOfLongestSubstring1("abcabcbb")
    print(3 == rtn)
    rtn = solution.lengthOfLongestSubstring1("bbbbb")
    print(1 == rtn)
    rtn = solution.lengthOfLongestSubstring1("pwwkew")
    print(3 == rtn)

    rtn = solution.lengthOfLongestSubstring2("abcabcbb")
    print(3 == rtn)
    rtn = solution.lengthOfLongestSubstring2("bbbbb")
    print(1 == rtn)
    rtn = solution.lengthOfLongestSubstring2("pwwkew")
    print(3 == rtn)

    rtn = solution.lengthOfLongestSubstring3("abcabcbb")
    print(3 == rtn)
    rtn = solution.lengthOfLongestSubstring3("bbbbb")
    print(1 == rtn)
    rtn = solution.lengthOfLongestSubstring3("pwwkew")
    print(3 == rtn)

