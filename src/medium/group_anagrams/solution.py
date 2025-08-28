#! /usr/bin/python3
# -*- coding:utf8 -*-

# Copyright 2025 Robina Li. BSD 3-Clause License All Rights Reserved.
# @file : solution.py
# @desc : Solution for Leetcode
# Reference : https://leetcode.com/problems/group-anagrams/

from typing import List
import collections

class Solution(object):
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = collections.defaultdict(list)

        for s in strs:
            key = tuple(sorted(s))
            ans[key].append(s)
        return list(ans.values())

    def groupAnagrams1(self, strs: List[str]) -> List[List[str]]:
        ans = collections.defaultdict(list)
        for s in strs:
            count = collections.Counter(s)
            ans[tuple(sorted(count.items()))].append(s)
            print(collections.Counter(s))
        return list(ans.values())

    def groupAnagrams2(self, strs: List[str]) -> List[List[str]]:
        ans = collections.defaultdict(list)
        for s in strs:
            ans[tuple(sorted(s))].append(s)
        return list(ans.values())

    def groupAnagrams3(self, strs: List[str]) -> List[List[str]]:
        ans = collections.defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            ans[tuple(count)].append(s)
        return list(ans.values())

    def groupAnagrams4(self, strs: List[str]) -> List[List[str]]:
        res = []
        if not strs:
            return res
        map_str_to_idx = {}
        for s in strs:
            sorted_str = '.'.join(sorted(s))

            if sorted_str in map_str_to_idx:
                idx = map_str_to_idx[sorted_str]
                res[idx].append(s)
            else:
                res.append([s])
                map_str_to_idx[sorted_str] = len(res) - 1
        return res
if __name__ == '__main__':
    solution = Solution()
    
    rtn = solution.groupAnagrams(["eat","tea","tan","ate","nat","bat"])
    print([["eat","tea","ate"],["tan","nat"],["bat"]] == rtn)
    rtn = solution.groupAnagrams([""])
    print([[""]] == rtn)
    rtn = solution.groupAnagrams(["a"])
    print([["a"]] == rtn)
    
    rtn = solution.groupAnagrams1(["eat","tea","tan","ate","nat","bat"])
    print([["eat","tea","ate"],["tan","nat"],["bat"]] == rtn)
    print (rtn)
    rtn = solution.groupAnagrams1([""])
    print([[""]] == rtn)
    rtn = solution.groupAnagrams1(["a"])
    print([["a"]] == rtn)

    rtn = solution.groupAnagrams2(["eat","tea","tan","ate","nat","bat"])
    print([["eat","tea","ate"],["tan","nat"],["bat"]] == rtn)
    rtn = solution.groupAnagrams2([""])
    print([[""]] == rtn)
    rtn = solution.groupAnagrams2(["a"])
    print([["a"]] == rtn)

    rtn = solution.groupAnagrams3(["eat","tea","tan","ate","nat","bat"])
    print([["eat","tea","ate"],["tan","nat"],["bat"]] == rtn)
    rtn = solution.groupAnagrams3([""])
    print([[""]] == rtn)
    rtn = solution.groupAnagrams3(["a"])
    print([["a"]] == rtn)

    rtn = solution.groupAnagrams4(["eat","tea","tan","ate","nat","bat"])
    print([["eat","tea","ate"],["tan","nat"],["bat"]] == rtn)
    rtn = solution.groupAnagrams4([""])
    print([[""]] == rtn)
    rtn = solution.groupAnagrams4(["a"])
    print([["a"]] == rtn)