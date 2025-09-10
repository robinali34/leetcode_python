#! /usr/bin/python3
# -*- coding:utf8 -*-

# Copyright 2025 Robina Li. BSD 3-Clause License All Rights Reserved.
# @file : solution.py
# @desc : Solution for Leetcode
# Reference : https://leetcode.com/problems/minimum-swaps-to-group-all-1s-together/

from typing import List
import math

class Solution:
    def minSwaps(self, data: List[int]) -> int:
        num_ones = 0
        for i in range(len(data)):
            num_ones += data[i]
        # Find min count of 0s in window
        num_zeros, min_num_zeros = 0, math.inf
        start = 0
        for end in range(len(data)):
            if data[end] == 0:
                num_zeros += 1
            if end - start + 1 == num_ones:
                min_num_zeros = min(min_num_zeros, num_zeros)
            if end >= num_ones - 1:
                if data[start] == 0:
                    num_zeros -= 1
                start += 1
        if min_num_zeros == math.inf:
            return 0
        return min_num_zeros

if __name__ == '__main__':
    solution = Solution()

    rtn = solution.minSwaps([1,0,1,0,1])
    print(1 == rtn)
    rtn = solution.minSwaps([0,0,0,1,0])
    print(0 == rtn)
    rtn = solution.minSwaps([1,0,1,0,1,0,0,1,1,0,1])
    print(3 == rtn)