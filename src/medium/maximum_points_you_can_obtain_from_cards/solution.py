#! /usr/bin/python3
# -*- coding:utf8 -*-

# Copyright 2025 Robina Li. BSD 3-Clause License All Rights Reserved.
# @file : solution.py
# @desc : Solution for Leetcode
# Reference : https://leetcode.com/problems/maximum-points-you-can-obtain-from-cards/

from typing import List
import math

class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        if k == len(cardPoints):
            return sum(cardPoints)
        m = len(cardPoints) - k
        sum_, min_sum = 0, math.inf
        start = 0
        for end in range(len(cardPoints)):
            sum_ += cardPoints[end]
            if end >= m - 1:
                min_sum = min(min_sum, sum_)
                sum_ -= cardPoints[start]
                start += 1
        return sum(cardPoints) - min_sum

if __name__ == '__main__':
    solution = Solution()

    rtn = solution.maxScore([1,2,3,4,5,6,1], 3)
    print(12 == rtn)
    rtn = solution.maxScore([2,2,2], 2)
    print(4 == rtn)
    rtn = solution.maxScore([9,7,7,9,7,7,9], 7)
    print(55 == rtn)