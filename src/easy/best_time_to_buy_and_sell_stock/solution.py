#! /usr/bin/python3
# -*- coding:utf8 -*-

# Copyright 2025 Robina Li. BSD 3-Clause License All Rights Reserved.
# @file : solution.py
# @desc : Solution for Leetcode
# Reference : https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

from typing import List
import math

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_, profit = float("inf"), 0
        for i in range(len(prices)):
            if prices[i] < min_:
                min_ = prices[i]
            elif prices[i] - min_ > profit:
                profit = prices[i]- min_
        return profit

if __name__ == '__main__':
    solution = Solution()

    rtn = solution.maxProfit([7,1,5,3,6,4])
    print(5 == rtn)
    rtn = solution.maxProfit([7,6,4,3,1])
    print(0 == rtn)