#! /usr/bin/python3
# -*- coding:utf8 -*-

# Copyright 2025 Robina Li. BSD 3-Clause License All Rights Reserved.
# @file : solution.py
# @desc : Solution for Leetcode
# Reference : https://leetcode.com/problems/letter-case-permutation/

from typing import List

class Solution(object):
    def letterCasePermutation(self, s: str) -> List[str]:
        rtn = []
        def dfs (path, i):
            if i == len(s):
                rtn.append(path)
                return
            c = s[i]
            dfs(path + c, i + 1)
            if s[i].isalpha():
                dfs(path + chr(ord(c) ^ (1<<5)), i + 1)
            
        dfs("", 0)
        return rtn

    def letterCasePermutation1(self, s: str) -> List[str]:
        rtn = []
        def dfs (path, i):
            if i == len(s):
                rtn.append(path)
                return
            c = s[i]
            dfs(path + c, i + 1)
            if s[i].isalpha():
                dfs(path + chr(ord(c) ^ (1<<5)), i + 1)
            
        dfs("", 0)
        return rtn
 
    def letterCasePermutation2(self, s: str) -> List[str]:
        rtn = []
        def dfs (path, i):
            if i == len(s):
                rtn.append(path)
                return
            if s[i].isalpha():
                dfs(path + s[i].lower(), i + 1)
                dfs(path + s[i].upper(), i + 1)
            else:
                dfs(path + s[i], i + 1)
        dfs("", 0)
        return rtn

if __name__ == '__main__':
    solution = Solution()
    rtn = solution.letterCasePermutation("a1b2")
    print(["a1b2","a1B2","A1b2","A1B2"] == rtn)
    rtn = solution.letterCasePermutation("3z4")
    print(["3z4","3Z4"] == rtn)

    rtn = solution.letterCasePermutation1("a1b2")
    print(["a1b2","a1B2","A1b2","A1B2"] == rtn)
    rtn = solution.letterCasePermutation1("3z4")
    print(["3z4","3Z4"] == rtn)
    
    rtn = solution.letterCasePermutation2("a1b2")
    print(["a1b2","a1B2","A1b2","A1B2"] == rtn)
    rtn = solution.letterCasePermutation2("3z4")
    print(["3z4","3Z4"] == rtn)