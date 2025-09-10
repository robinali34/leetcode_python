#! /usr/bin/python3
# -*- coding:utf8 -*-

# Copyright 2025 Robina Li. BSD 3-Clause License All Rights Reserved.
# @file : solution.py
# @desc : Solution for Leetcode
# Reference : https://leetcode.com/problems/parsing-a-boolean-expression/

from typing import List

class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        idx = [0]
        def parse(exp: str, idx: list) -> bool:
            cur = exp[idx[0]]
            idx[0] += 1
            if cur == 't': return True
            if cur == 'f': return False
            if cur == '!':
                idx[0] += 1
                rtn = not parse(exp, idx)
                idx[0] += 1
                return rtn
            is_and = (cur == '&')
            rtn = True if is_and else False
            idx[0] += 1
            while True:
                val = parse(exp, idx)
                rtn = rtn and val if is_and else rtn or val
                if exp[idx[0]] == ')':
                    idx[0] += 1
                    break
                elif exp[idx[0]] == ',':
                    idx[0] += 1 
            return rtn
        return parse(expression, idx)

if __name__ == '__main__':
    solution = Solution()

    rtn = solution.parseBoolExpr("&(|(f))")
    print(False == rtn)
    rtn = solution.parseBoolExpr("|(f,f,f,t)")
    print(True == rtn)
    rtn = solution.parseBoolExpr("!(&(f,t))")
    print(True == rtn)