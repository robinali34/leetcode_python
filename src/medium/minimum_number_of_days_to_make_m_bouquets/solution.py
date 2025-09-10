#! /usr/bin/python3
# -*- coding:utf8 -*-

# Copyright 2025 Robina Li. BSD 3-Clause License All Rights Reserved.
# @file : solution.py
# @desc : Solution for Leetcode
# Reference : https://leetcode.com/problems/minimum-number-of-days-to-make-m-bouquets/

from typing import List

class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if m * k > len(bloomDay):
            return -1
        def canMake(day: int) -> bool:
            flowers = bouquets = 0
            for bloom in bloomDay:
                if bloom <= day:
                    flowers += 1
                    if flowers == k:
                        bouquets += 1
                        flowers = 0
                else:
                    flowers = 0
            return bouquets >= m
        left, right = min(bloomDay), max(bloomDay)
        answer = -1
        while left <= right:
            pivot = (left + right) >> 1
            if canMake(pivot):
                ans = pivot
                right = pivot - 1
            else:
                left = pivot + 1
        return ans

if __name__ == '__main__':
    solution = Solution()

    rtn = solution.minDays([1,10,3,10,2], 3, 1)
    print(3 == rtn)
    rtn = solution.minDays([1,10,3,10,2], 3, 2)
    print(-1 == rtn)
    rtn = solution.minDays([7,7,7,7,12,7,7], 2, 3)
    print(12 == rtn)