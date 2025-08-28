#! /usr/bin/python3
# -*- coding:utf8 -*-

# Copyright 2025 Robina Li. BSD 3-Clause License All Rights Reserved.
# @file : solution.py
# @desc : Solution for Leetcode
# Reference : https://leetcode.com/problems/invert-binary-tree

from typing import List, Optional
from collections import deque
class TreeNode:
    def __init__(self, val: int=0, left: Optional['TreeNode']=None, right: Optional['TreeNode']=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    # Recursive DFS (Top-down)
    def invertTree_recursive(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return 0
        left = self.invertTree_recursive(root.left)
        right = self.invertTree_recursive(root.right)
        root.left, root.right = right, left
        return root

    # Iterative BFS (using queue)
    def invertTree_bfs_iterative(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return 0
        queue = deque([root])
        while queue:
            node = queue.popleft()
            node.left, node.right = node.right, node.left
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return root

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

if __name__ == '__main__':
    sol = Solution()

    test_cases = [
        ([2,1,3], [2,3,1]),
        ([],[]),
    ]
    methods = [
        ("Recursive DFS", sol.invertTree_recursive),
        ('Iterative BFS', sol.invertTree_bfs_iterative),
    ]

    for name, method in methods:
        print(f"Testing {name}...")
        for i, (tree_list, expected) in enumerate(test_cases, 1):
            root = buildTree(tree_list)
            result = method(root)
            result_list = tree_to_list(result)
            print(f"Test #{i}: expected {expected}, got {result_list}")