#! /usr/bin/python3
# -*- coding:utf8 -*-

# Copyright 2025 Robina Li. BSD 3-Clause License All Rights Reserved.
# @file : solution.py
# @desc : Solution for Leetcode
# Reference : https://leetcode.com/problems/binary-tree-level-order-traversal

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
    def levelOrder_recursive(self, root: Optional[TreeNode]) -> List[List[int]]:
        rtn = []
        if not root:
            return rtn
        def helper(node: TreeNode, level: int) -> None:
            if len(rtn) == level:
                rtn.append([])
            rtn[level].append(node.val)
            if node.left:
                helper(node.left, level + 1)
            if node.right:
                helper(node.right, level + 1)
        helper(root, 0)
        return rtn

    # Iterative BFS (using queue)
    def levelOrder_bfs_iterative(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []
        if not root:
            return ans
        queue = deque([root])
        while queue:
            vals = []
            for _ in range(len(queue)):
                node = queue.popleft()
                vals.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            ans.append(vals)
        return ans

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

def main():
    sol = Solution()

    test_cases = [
        # multiple levels
        ([3,9,20,None,None,15,7], [[3],[9,20],[15,7]]),

        # one level
        ([1], [[1]]),

        # both empty
        ([], []),
    ]
    methods = [
        ("Recursive DFS", sol.levelOrder_recursive),
        ("Iterative BFS", sol.levelOrder_bfs_iterative),
    ]

    for name, method in methods:
        print(f"\nTesting {name}:")
        for i, (root, expected) in enumerate(test_cases, 1):
            root = buildTree(root)
            result = method(root)
            status = "✅ PASS" if result == expected else "❌ FAIL"
            print(f"  Test #{i}: expected {expected}, got {result} → {status}")

if __name__ == '__main__':
    main()