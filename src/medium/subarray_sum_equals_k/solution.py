#! /usr/bin/python3
# -*- coding:utf8 -*-

# Copyright 2025 Robina Li. BSD 3-Clause License All Rights Reserved.
# @file : solution.py
# @desc : Solution for Leetcode
# Reference : https://leetcode.com/problems/subarray-sum-equals-k

from typing import List

class Solution:

    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        cur_sum = 0
        pre_sums = {0:1}
        for num in nums:
            cur_sum += num
            if(cur_sum - k) in pre_sums:
                count += pre_sums[cur_sum - k]
            pre_sums[cur_sum] = pre_sums.get(cur_sum, 0) + 1
        return count

    # Time Complexity: O(n^3)
    # Space Complexity: O(1)
    def subarraySum1(self, nums: List[int], k: int) -> int:
        count = 0
        for start in range(len(nums)):
            for end in range(start + 1, len(nums) + 1):
                total = 0
                for i in range(start, end):
                    total += nums[i]
                if total == k:
                    count += 1
        return count

    # Time Complexity: O(n^2)
    # Space Complexity: O(n)
    def subarraySum2(self, nums: List[int], k: int) -> int:
        count = 0
        size = len(nums)
        sum = [0] * (size + 1)
        for i in range(1, size + 1):
            sum[i] = sum[i - 1] + nums[i - 1]
        for i in range(size):
            for j in range(i + 1, size + 1):
                if sum[j] - sum[i] == k:
                    count += 1
        return count


if __name__ == '__main__':
    solution = Solution()

    rtn = solution.subarraySum([1,1,1], 2)
    print(2 == rtn)
    rtn = solution.subarraySum([1,2,3], 3)
    print(2 == rtn)

    rtn = solution.subarraySum1([1,1,1], 2)
    print(2 == rtn)
    rtn = solution.subarraySum1([1,2,3], 3)
    print(2 == rtn)

    rtn = solution.subarraySum2([1,1,1], 2)
    print(2 == rtn)
    rtn = solution.subarraySum2([1,2,3], 3)
    print(2 == rtn)