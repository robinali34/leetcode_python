#! /usr/bin/python3
# -*- coding:utf8 -*-

# Copyright 2025 Robina Li. BSD 3-Clause License All Rights Reserved.
# @file : solution.py
# @desc : Solution for Leetcode
# Reference : https://leetcode.com/problems/simplify-path/

from typing import List
import math

class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        for portion in path.split('/'):
            if portion == "..":
                if stack:
                    stack.pop()
            elif portion == '.' or not portion:
                continue
            else:
                stack.append(portion)
        return '/' + '/'.join(stack)

if __name__ == '__main__':
    solution = Solution()

    rtn = solution.simplifyPath("/home/")
    print("/home" == rtn)
    rtn = solution.simplifyPath("/home//foo/")
    print("/home/foo" == rtn)
    rtn = solution.simplifyPath("/home/user/Documents/../Pictures")
    print("/home/user/Pictures" == rtn)
    rtn = solution.simplifyPath("/../")
    print("/" == rtn)
    rtn = solution.simplifyPath("/.../a/../b/c/../d/./")
    print("/.../b/d" == rtn)