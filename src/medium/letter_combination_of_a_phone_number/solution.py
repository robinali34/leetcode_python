#! /usr/bin/python3
# -*- coding:utf8 -*-

# Copyright 2025 Robina Li. BSD 3-Clause License All Rights Reserved.
# @file : solution.py
# @desc : Solution for Leetcode
# Reference : https://leetcode.com/problems/letter-combinations-of-a-phone-number/

from typing import List

class Solution(object):
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits: return []
        phone_map = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
                     '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        rtn = []
        def backtrack(idx: int, path: List[str]) -> None:
            if idx == len(digits):
                rtn.append("".join(path))
                return
            for letter in phone_map[digits[idx]]:
                path.append(letter)
                backtrack(idx + 1, path)
                path.pop()
        backtrack(0, [])
        return rtn
 
    def letterCombinations1(self, digits: str) -> List[str]:
        if not digits: return []
        phone_map = {
            '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
            '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        rtn = []
        def backtrack(idx: int, path: str):
            if idx == len(digits):
                rtn.append(path)
                return
            letters = phone_map[digits[idx]]
            for letter in letters:
                backtrack(idx + 1, path + letter)
        backtrack(0, '')
        return rtn


if __name__ == '__main__':
    solution = Solution()

    rtn = solution.letterCombinations("23")
    print(["ad","ae","af","bd","be","bf","cd","ce","cf"] == rtn)
    rtn = solution.letterCombinations("")
    print([] == rtn)
    rtn = solution.letterCombinations("2")
    print(["a","b","c"] == rtn)

    rtn = solution.letterCombinations1("23")
    print(["ad","ae","af","bd","be","bf","cd","ce","cf"] == rtn)
    rtn = solution.letterCombinations1("")
    print([] == rtn)
    rtn = solution.letterCombinations1("2")
    print(["a","b","c"] == rtn)