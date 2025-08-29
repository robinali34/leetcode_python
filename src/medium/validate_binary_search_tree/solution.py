#! /usr/bin/python3
# -*- coding:utf8 -*-
# Copyright 2025 Robina Li. BSD 3-Clause License All Rights Reserved.
# @file : solution.py
# @desc : Solution for Leetcode
# Reference : https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree

import math
from typing import List, Optional
from collections import deque

class TreeNode:
    def __init__(self, val: int=0, left: Optional['TreeNode']=None, right: Optional['TreeNode']=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return f"TreeNode({self.val}, {self.left}, {self.right})"

class Solution:
    # Recursive DFS (Top-down)
    def isValidBST_recursive(self, root: Optional[TreeNode]) -> bool:
        def validate(node, low=-math.inf, high=math.inf):
            if not node:
                return True
            if node.val <= low or node.val >= high:
                return False
            return validate(node.right, node.val, high) and validate(node.left, low, node.val)
        return validate(root)

    # DFS iterative
    def isValidBST_dfs_iterative(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        stack = [(root, -math.inf, math.inf)]
        while stack:
            root, lower, upper = stack.pop()
            if not root:
                continue
            val = root.val
            if val <= lower or val >= upper:
                return False
            stack.append((root.right, val, upper))
            stack.append((root.left, lower, val))
        return True

    # DFS Recursive Inorder Traversal
    def isValidBST_dfs_recursive_inorder(self, root: Optional[TreeNode]) -> bool:
        def inorder(root):
            if not root:
                return True
            if not inorder(root.left):
                return False
            if root.val <= self.prev:
                return False
            self.prev = root.val
            return inorder(root.right)
        self.prev = -math.inf
        return inorder(root)

def buildTree(values: List[Optional[int]]) -> Optional[TreeNode]:
    if not values:
        return None
    root = TreeNode(values[0])
    queue = deque([root])
    i = 1
    val_to_node = {values[0]: root}
    while queue and i < len(values):
        node = queue.popleft()
        if i < len(values) and values[i] is not None:
            node.left = TreeNode(values[i])
            val_to_node[values[i]] = node.left
            queue.append(node.left)
        i += 1
        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            val_to_node[values[i]] = node.right
            queue.append(node.right)
        i += 1
    return root, val_to_node

def tree_to_list(root: Optional[TreeNode]) -> List[Optional[int]]:
    if not root:
        return []
    ans = []
    queue = deque([root])
    while queue:
        node = queue.popleft()
        if node:
            ans.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            ans.append(None)
    while ans and ans[-1] is None:
        ans.pop()
    return ans

def main():
    sol = Solution()

    test_cases = [
        ([2,1,3], True),
        ([5,1,4,None,None,3,6], False),
    ]

    methods = [
        ("Recursive DFS", sol.isValidBST_recursive),
        ("Iterative DFS", sol.isValidBST_dfs_iterative),
        ("DFS Recursive Inorder Traversal", sol.isValidBST_dfs_recursive_inorder)
    ]

    for name, method in methods:
        print(f"\nTesting {name}:")
        for i, (tree_vals, expected_val) in enumerate(test_cases, 1):
            root, val_map = buildTree(tree_vals)
            result = method(root)
            status = "✅ PASS" if result == expected_val else "❌ FAIL"
            print(f"  Test #{i}: expected {expected_val}, got {result} → {status}")

if __name__ == '__main__':
    main()