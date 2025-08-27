#! /usr/bin/python3
# -*- coding:utf8 -*-

# Copyright 2025 Robina Li. BSD 3-Clause License All Rights Reserved.
# @file : solution.py
# @desc : Solution for Leetcode
# Reference : https://leetcode.com/problems/valid-parentheses/

from typing import List

class Solution(object):
    def isValid(self, s: str) -> bool:
        stack = []
        for i in range(len(s)):
            if s[i] == '(' or s[i] == '[' or s[i] == '{':
                stack.append(s[i])
            else:
                if not stack:
                    return False
                top = stack.pop()
                if s[i] == ')' and top != '(':
                    return False
                elif s[i] == ']' and top != '[':
                    return False
                elif s[i] == '}' and top != '{':
                    return False
        return len(stack) == 0

    def isValid1(self, s: str) -> bool:
        stack = []
        mapping = {')' : '(', ']' : '[', '}' : '{'}
        for char in s:
            if char in mapping:
                top = stack.pop() if stack else '#'
                if mapping[char] != top:
                    return False

            else:
                stack.append(char)

        return not stack

if __name__ == '__main__':
    solution = Solution()
    
    rtn = solution.isValid("()")
    print(True == rtn)
    rtn = solution.isValid("()[]{}")
    print(True == rtn)
    rtn = solution.isValid("(]")
    print(False == rtn)
    rtn = solution.isValid("([])")
    print(True == rtn)

    print("\n")
    rtn = solution.isValid1("()")
    print(True == rtn)
    rtn = solution.isValid1("()[]{}")
    print(True == rtn)
    rtn = solution.isValid1("(]")
    print(False == rtn)
    rtn = solution.isValid1("([])")
    print(True == rtn)
