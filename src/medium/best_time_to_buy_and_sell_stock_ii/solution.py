#! /usr/bin/python3
# -*- coding:utf8 -*-

# Copyright 2025 Robina Li. BSD 3-Clause License All Rights Reserved.
# @file : solution.py
# @desc : Solution for Leetcode
# Reference : https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/

from typing import List

class Solution(object):
    def maxProfit(self, prices: List[int]) -> int:
        # Iterate all prices from idx 1, get max difference prices[idx] - prices[idx - 1]
        return sum(max(0, p - q) for p, q in zip(prices[1:], prices))

if __name__ == '__main__':
    solution = Solution()
    rtn = solution.maxProfit([7,1,5,3,6,4])
    print(7 == rtn)
    rtn = solution.maxProfit([1,2,3,4,5])
    print(4 == rtn)
    rtn = solution.maxProfit([7,6,4,3,1])
    print(0 == rtn)