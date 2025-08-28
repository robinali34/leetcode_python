#! /usr/bin/python3
# -*- coding:utf8 -*-

# Copyright 2025 Robina Li. BSD 3-Clause License All Rights Reserved.
# @file : solution.py
# @desc : Solution for Leetcode
# Reference : https://leetcode.com/problems/maximum-depth-of-binary-tree/

from typing import List, Optional
from collections import deque
class TreeNode:
    def __init__(self, val: int=0, left: Optional['TreeNode']=None, right: Optional['TreeNode']=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    # Recursive DFS (Top-down)
    def maxDepth_recursive(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        left = self.maxDepth_recursive(root.left)
        right = self.maxDepth_recursive(root.right)
        return 1 + max(left, right)

    # Iterative DFS (using stack)
    def maxDepth_dfs_iterative(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        stack = [(root, 1)]
        max_depth = 0
        while stack:
            node, depth = stack.pop()
            if node:
                max_depth = max(max_depth, depth)
                stack.append((node.left, depth + 1))
                stack.append((node.right, depth + 1))
        return max_depth

    # Iterative BFS (using queue)
    def maxDepth_bfs_iterative(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        queue = deque([root])
        depth = 0
        while queue:
            for _ in range(len(queue)):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            depth += 1
        return depth

def buildTree(values: List[Optional[int]]) -> Optional[TreeNode]:
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

if __name__ == '__main__':
    sol = Solution()

    test_cases = [
        ([3,9,20,None,None,15,7], 3),
        ([1,None,2],2),
        ([],0),
        ([1,2,3,4,None,None,5],3),
    ]
    methods = [
        ("Recursive DFS", sol.maxDepth_recursive),
        ("Iterative DFS", sol.maxDepth_dfs_iterative),
        ('Iterative BFS', sol.maxDepth_bfs_iterative),
    ]

    for name, method in methods:
        print(f"Testing {name}...")
        for i, (tree_list, expected) in enumerate(test_cases, 1):
            root = buildTree(tree_list)
            result = method(root)
            print(f"Test #{i}: expected {expected}, got {result}")