#! /usr/bin/python3
# -*- coding:utf8 -*-

# Copyright 2025 Robina Li. BSD 3-Clause License All Rights Reserved.
# @file : solution.py
# @desc : Solution for Leetcode
# Reference : https://leetcode.com/problems/same-tree

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
    def isSameTree_recursive(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if not p or not q:
            return False
        if p.val != q.val:
            return False
        return self.isSameTree_recursive(p.right, q.right) and self.isSameTree_recursive(p.left, q.left)

    # Iterative BFS (using queue)
    def isSameTree_bfs_iterative(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def check(p: TreeNode, q: TreeNode) -> bool:
            if not p and not q:
                return True
            if not q or not p:
                return False
            if p.val != q.val:
                return False
            return True
        queue = deque([(p,q)])
        while queue:
            p, q = queue.popleft()
            if not check(p, q):
                return False
            if p:
                queue.append((p.left, q.left))
                queue.append((p.right, q.right))
        return True

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
        # identical trees
        ([1, 2, 3], [1, 2, 3], True),

        # different structure
        ([1, 2], [1, None, 2], False),

        # different values
        ([1, 2, 1], [1, 1, 2], False),

        # both empty
        ([], [], True),

        # one empty
        ([1], [], False),

        # deep identical tree
        ([3, 9, 20, None, None, 15, 7], [3, 9, 20, None, None, 15, 7], True),
    ]
    methods = [
        ("Recursive DFS", sol.isSameTree_recursive),
        ("Iterative BFS", sol.isSameTree_bfs_iterative),
    ]

    for name, method in methods:
        print(f"\nTesting {name}:")
        for i, (p_list, q_list, expected) in enumerate(test_cases, 1):
            p = buildTree(p_list)
            q = buildTree(q_list)
            result = method(p, q)
            status = "✅ PASS" if result == expected else "❌ FAIL"
            print(f"  Test #{i}: expected {expected}, got {result} → {status}")

if __name__ == '__main__':
    main()