#! /usr/bin/python3
# -*- coding:utf8 -*-

# Copyright 2025 Robina Li. BSD 3-Clause License All Rights Reserved.
# @file : solution.py
# @desc : Solution for Leetcode
# Reference : https://leetcode.com/problems/two-sum

from typing import List

class Solution(object):
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i in range(len(nums)):
            pair = target - nums[i]
            if pair in hashmap and hashmap[pair] != i:
                return [hashmap[pair],i]
            hashmap[nums[i]] = i

        return []

    def twoSum1(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                if nums[j] == target - nums[i]:
                    return [i, j]

        return []

    def twoSum2(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i in range(len(nums)):
            hashmap[nums[i]] = i
        for i in range(len(nums) -1):
            pair = target - nums[i]
            if pair in hashmap and hashmap[pair] != i:
                return [i, hashmap[pair]]

        return []
    
    def twoSum3(self, nums: List[int], target: int) -> List[int]:
        nums_with_idx = list(enumerate(nums))
        nums_with_idx.sort(key=lambda x:x[1])
        left, right = 0, len(nums) -1
        while left < right:
            total = nums_with_idx[left][1] + nums_with_idx[right][1]
            if total == target:
                return [nums_with_idx[left][0], nums_with_idx[right][0]]
            elif total < target:
                left += 1
            else:
                right -=1

if __name__ == '__main__':
    solution = Solution()
    
    rtn = solution.twoSum([2,7,11,15], 9)
    print([0,1] == rtn)
    rtn = solution.twoSum([3,2,4], 6)
    print([1,2] == rtn)
    rtn = solution.twoSum([3,3], 6)
    print([0,1] == rtn)
    
    rtn = solution.twoSum1([2,7,11,15], 9)
    print([0,1] == rtn)
    rtn = solution.twoSum1([3,2,4], 6)
    print([1,2] == rtn)
    rtn = solution.twoSum1([3,3], 6)
    print([0,1] == rtn)

    rtn = solution.twoSum2([2,7,11,15], 9)
    print([0,1] == rtn)
    rtn = solution.twoSum2([3,2,4], 6)
    print([1,2] == rtn)
    rtn = solution.twoSum2([3,3], 6)
    print([0,1] == rtn)

    rtn = solution.twoSum3([2,7,11,15], 9)
    print([0,1] == rtn)
    rtn = solution.twoSum3([3,2,4], 6)
    print([1,2] == rtn)
    rtn = solution.twoSum3([3,3], 6)
    print([0,1] == rtn)