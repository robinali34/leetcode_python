#! /usr/bin/python3
# -*- coding:utf8 -*-

# Copyright 2021 Robina Li. BSD 3-Clause License All Rights Reserved.
# @file : solution.py
# @desc : Solution for Leetcode
# Reference : https://leetcode.com/problems/climbing-stairs

from typing import List
from collections import deque

class Solution(object):

    def climbStairs(self, n: int) -> int:
        memo = [0] * (n + 1)
        return self.climb_stairs(0, n, memo)

    def climb_stairs(self, i:int, n:int, memo:List[int]) -> int:
        if i > n:
            return 0
        if i == n:
            return 1
        if memo[i] > 0:
            return memo[i]
        memo[i] = self.climb_stairs(i+1, n, memo) + self.climb_stairs(i+2, n, memo)
        return memo[i]

    def climbStairs2(self, n: int) -> int:
        if n == 1:
            return 1
        dp = [0 for _ in range(n + 1)]
        dp[1] = 1
        dp[2] = 2
        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[n]

if __name__ == '__main__':
    solution = Solution()
    rtn = solution.climbStairs(2)
    print(2 == rtn)
    rtn = solution.climbStairs(3)
    print(3 == rtn)

    rtn = solution.climbStairs2(2)
    print(2 == rtn)
    rtn = solution.climbStairs2(3)
    print(3 == rtn)