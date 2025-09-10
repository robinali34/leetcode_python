#! /usr/bin/python3
# -*- coding:utf8 -*-

# Copyright 2025 Robina Li. BSD 3-Clause License All Rights Reserved.
# @file : solution.py
# @desc : Solution for Leetcode
# Reference : https://leetcode.com/problems/grumpy-bookstore-owner/

from typing import List

class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        sum_, max_sum, max_start = 0, 0, 0
        start = 0
        for end in range(len(grumpy)):
            if grumpy[end] == 1:
                sum_ += customers[end]
            if sum_ > max_sum:
                max_sum = sum_
                max_start = start
            if end >= minutes - 1:
                if grumpy[start]:
                    sum_ -= customers[start]
                start += 1
        for i in range(max_start, max_start + minutes):
            grumpy[i] = 0
        res = 0
        for i in range(len(customers)):
            if not grumpy[i]:
                res += customers[i]
        return res


if __name__ == '__main__':
    solution = Solution()

    rtn = solution.maxSatisfied([1,0,1,2,1,1,7,5], [0,1,0,1,0,1,0,1], 3)
    print(16 == rtn)
    rtn = solution.maxSatisfied([1], [0], 1)
    print(1 == rtn)