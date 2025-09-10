#! /usr/bin/python3
# -*- coding:utf8 -*-

# Copyright 2025 Robina Li. BSD 3-Clause License All Rights Reserved.
# @file : solution.py
# @desc : Solution for Leetcode
# Reference : https://leetcode.com/problems/search-in-a-binary-search-tree/

from typing import List, Optional
import math

class TreeNode:
    def __init__(self, val: int = 0, left: Optional['TreeNode'] = None, right: Optional['TreeNode'] = None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        # Base case
        if not root: return None
        if root.val == val: return root

        # Recursion relation
        if val > root.val:
            return self.searchBST(root.right, val)
        else:
            return self.searchBST(root.left, val)

from collections import deque

def build_tree_from_list(values):
    if not values:
        return None
    root = TreeNode(values[0])
    queue = deque([root])
    i = 1
    while queue and i < len(values):
        node = queue.popleft()
        if values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1

        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1
    return root


def test_search_bst(tree_vals, search_val, expected_val):
    root = build_tree_from_list(tree_vals)
    solution = Solution()
    result = solution.searchBST(root, search_val)
    output = result.val if result else None
    print(f"Search {search_val} in {tree_vals} → Found: {output}, Expected: {expected_val}")
    assert output == expected_val, f"❌ Failed: expected {expected_val}, got {output}"
    print("✅ Test passed\n")

if __name__ == "__main__":
    test_search_bst([4, 2, 7, 1, 3], 2, 2)
    test_search_bst([4, 2, 7, 1, 3], 5, None)
    test_search_bst([], 1, None)
    test_search_bst([1], 1, 1)
    test_search_bst([5, 3, 6, 2, 4], 4, 4)