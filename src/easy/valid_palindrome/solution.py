#! /usr/bin/python3
# -*- coding:utf8 -*-

# Copyright 2025 Robina Li. BSD 3-Clause License All Rights Reserved.
# @file : solution.py
# @desc : Solution for Leetcode
# Reference : https://leetcode.com/problems/remove-element/

from typing import List
from functools import cache

class Solution(object):
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        while left < right:
            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1
            if s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1
        return True

if __name__ == '__main__':
    solution = Solution()

    rtn = solution.isPalindrome("A man, a plan, a canal: Panama")
    print(True == rtn)
    rtn = solution.isPalindrome("race a car")
    print(False == rtn)
    rtn = solution.isPalindrome(" ")
    print(True == rtn)