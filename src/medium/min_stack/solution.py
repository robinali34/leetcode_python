#! /usr/bin/python3
# -*- coding:utf8 -*-

# Copyright 2025 Robina Li. BSD 3-Clause License All Rights Reserved.
# @file : solution.py
# @desc : Solution for Leetcode
# Reference : https://leetcode.com/problems/min-stack

from typing import List
import collections

class MinStack(object):

    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.min_stack or val < self.min_stack[-1][0]:
            self.min_stack.append([val, 1])
        elif val == self.min_stack[-1][0]:
            self.min_stack[-1][1] += 1

    def pop(self) -> None:
        val = self.stack.pop()
        if val == self.min_stack[-1][0]:
            if self.min_stack[-1][1] == 1:
                self.min_stack.pop()
            else:
                self.min_stack[-1][1] -= 1

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1][0]


import unittest


class TestMinStack(unittest.TestCase):
    def test_push_and_getMin(self):
        stack = MinStack()
        stack.push(-2)
        stack.push(0)
        stack.push(-3)
        self.assertEqual(stack.getMin(), -3)

    def test_pop_and_getMin(self):
        stack = MinStack()
        stack.push(-2)
        stack.push(0)
        stack.push(-3)
        stack.pop()
        self.assertEqual(stack.getMin(), -2)

    def test_top(self):
        stack = MinStack()
        stack.push(1)
        self.assertEqual(stack.top(), 1)
        stack.push(2)
        self.assertEqual(stack.top(), 2)

    def test_multiple_min_values(self):
        stack = MinStack()
        stack.push(2)
        stack.push(0)
        stack.push(3)
        stack.push(0)
        self.assertEqual(stack.getMin(), 0)
        stack.pop()
        self.assertEqual(stack.getMin(), 0)
        stack.pop()
        self.assertEqual(stack.getMin(), 0)
        stack.pop()
        self.assertEqual(stack.getMin(), 2)

    def test_exceptions(self):
        stack = MinStack()
        with self.assertRaises(IndexError):
            stack.pop()
        with self.assertRaises(IndexError):
            stack.top()
        with self.assertRaises(IndexError):
            stack.getMin()


if __name__ == "__main__":
    unittest.main()
