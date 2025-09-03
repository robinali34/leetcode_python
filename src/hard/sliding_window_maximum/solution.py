#! /usr/bin/python3
# -*- coding:utf8 -*-

# Copyright 2025 Robina Li. BSD 3-Clause License All Rights Reserved.
# @file : solution.py
# @desc : Solution for Leetcode
# Reference : https://leetcode.com/problems/sliding-window-maximum/

from typing import List
from collections import Counter
from collections import deque

class Solution(object):
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        q = deque()
        for i in range(len(nums)):
            while q and q[0] < i - k + 1:
                q.popleft()
            while q and nums[q[-1]] < nums[i]:
                q.pop()
            q.append(i)
            if i >= k -1:
                res.append(nums[q[0]])
        return res

if __name__ == '__main__':
    solution = Solution()
    rtn = solution.maxSlidingWindow([1,3,-1,-3,5,3,6,7], 3)
    print([3,3,5,5,6,7] == rtn)
    rtn = solution.maxSlidingWindow([1],1)
    print([1] == rtn)