#! /usr/bin/python3
# -*- coding:utf8 -*-

# Copyright 2025 Robina Li. BSD 3-Clause License All Rights Reserved.
# @file : solution.py
# @desc : Solution for Leetcode
# Reference : https://leetcode.com/problems/final-prices-with-a-special-discount-in-a-shop

from typing import List

class Solution(object):
    def finalPrices(self, prices: List[int]) -> List[int]:
        stack = []
        for i in range(len(prices)):
            while stack and prices[stack[-1]] >= prices[i]:
                idx = stack.pop()
                prices[idx] -= prices[i]
            stack.append(i)
        return prices

if __name__ == '__main__':
    solution = Solution()
    rtn = solution.finalPrices([8,4,6,2,3])
    print([4,2,4,2,3] == rtn)
    rtn = solution.finalPrices([1,2,3,4,5])
    print([1,2,3,4,5] == rtn)
    rtn = solution.finalPrices([10,1,1,6])
    print([9,0,1,6] == rtn)