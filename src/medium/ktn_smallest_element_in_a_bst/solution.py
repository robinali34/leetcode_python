#! /usr/bin/python3
# -*- coding:utf8 -*-

# Copyright 2025 Robina Li. BSD 3-Clause License All Rights Reserved.
# @file : solution.py
# @desc : Solution for Leetcode
# Reference : https://leetcode.com/problems/kth-smallest-element-in-a-bst

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
    def kthSmallest_inorder(self, root: Optional[TreeNode], k: int) -> int:
        def inorder(r: Optional[TreeNode]) -> List[int]:
            return inorder(r.left) + [r.val] + inorder(r.right) if r else []
        return inorder(root)[k - 1]

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
        ([3,1,4,None,2], 1, 1),
        ([5,3,6,2,4,None,None,1], 3, 3),
    ]
    methods = [
        ("Inorder DFS", sol.kthSmallest_inorder),
    ]

    for name, method in methods:
        print(f"\nTesting {name}:")
        for i, (root, k, expected) in enumerate(test_cases, 1):
            root = buildTree(root)
            result = method(root, k)
            status = "✅ PASS" if result == expected else "❌ FAIL"
            print(f"  Test #{i}: expected {expected}, got {result} → {status}")

if __name__ == '__main__':
    main()