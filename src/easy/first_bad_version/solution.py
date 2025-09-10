#! /usr/bin/python3
# -*- coding:utf8 -*-

# Copyright 2025 Robina Li. BSD 3-Clause License All Rights Reserved.
# @file : solution.py
# @desc : Solution for Leetcode
# Reference : https://leetcode.com/problems/first-bad-version/

from typing import List
import math

def isBadVersion(version: int) -> bool:
    return version >= FIRST_BAD_VERSION

class Solution:
    def firstBadVersion(self, n: int) -> int:
        left, right = 1, n
        while left <= right:
            pivit = (left + right) >> 1
            if isBadVersion(pivit) == False:
                left = pivit + 1
            else:
                right = pivit - 1
        return left

def test_first_bad_version(n, expected):
    global FIRST_BAD_VERSION
    FIRST_BAD_VERSION = expected  # Set the "bad" version globally
    solution = Solution()
    result = solution.firstBadVersion(n)
    print(f"Input n = {n}, First Bad Version = {expected} -> Output = {result}")
    assert result == expected, f"❌ Expected {expected}, but got {result}"
    print("✅ Test passed\n")


if __name__ == '__main__':
    test_first_bad_version(5, 4)
    test_first_bad_version(1, 1)
    test_first_bad_version(10, 1)
    test_first_bad_version(1000, 873)
    test_first_bad_version(2, 2)