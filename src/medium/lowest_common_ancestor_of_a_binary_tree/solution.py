#! /usr/bin/python3
# -*- coding:utf8 -*-

# Copyright 2025 Robina Li. BSD 3-Clause License All Rights Reserved.
# @file : solution.py
# @desc : Solution for Leetcode
# Reference : https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree

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
    def lowestCommonAncestor_recursive(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        rtn = None
        def dfs(node: 'TreeNode') -> bool:
            nonlocal rtn
            if not node:
                return False
            l = dfs(node.left)
            r = dfs(node.right)
            if (l and r) or (node.val == p.val or node.val == q.val) and (l or r):
                rtn = node
            return l or r or (node.val == p.val or node.val == q.val)
        dfs(root)
        return rtn

    # parent node
    def lowestCommonAncestor_dfs_iterative_with_parent(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        stack = [root]
        parent = {root: None}
        while p not in parent or q not in parent:
            node = stack.pop()
            if node.left:
                parent[node.left] = node
                stack.append(node.left)
            if node.right:
                parent[node.right] = node
                stack.append(node.right)
        ancestors = set()
        while p:
            ancestors.add(p)
            p = parent[p]
        while q not in ancestors:
            q = parent[q]
        return q

    BOTH_PENDING = 2
    LEFT_DONE = 1
    BOTH_DONE = 0
    def lowestCommonAncestor_dfs_iterative(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        stack = [(root, Solution.BOTH_PENDING)]
        one_node_found = False
        LCA_idx = -1
        while stack:
            parent_node, parent_state = stack[-1]
            if parent_state != Solution.BOTH_DONE:
                if parent_state == Solution.BOTH_PENDING:
                    if parent_node == p or parent_node == q:
                        if one_node_found:
                            return stack[LCA_idx][0]
                        else:
                            one_node_found = True
                            LCA_idx = len(stack) - 1
                    child_node = parent_node.left
                else:
                    child_node = parent_node.right
                stack.pop()
                stack.append((parent_node, parent_state - 1))
                if child_node:
                    stack.append((child_node, Solution.BOTH_PENDING))
            else:
                if one_node_found and LCA_idx == len(stack) - 1:
                    LCA_idx -= 1
                stack.pop()
        return None

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
        # format: (tree_list, p_val, q_val, expected_lca_val)
        ([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4], 5, 1, 3),
        ([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4], 5, 4, 5),
        ([1, 2], 1, 2, 1),
        ([1, 2, 3, 4, 5], 4, 5, 2),
    ]

    methods = [
        ("Recursive DFS", sol.lowestCommonAncestor_recursive),
        ("Iterative DFS with parent", sol.lowestCommonAncestor_dfs_iterative_with_parent),
        ("Iterative DFS", sol.lowestCommonAncestor_dfs_iterative)
    ]

    for name, method in methods:
        print(f"\nTesting {name}:")
        for i, (tree_vals, p_val, q_val, expected_val) in enumerate(test_cases, 1):
            root, val_map = buildTree(tree_vals)
            p = val_map[p_val]
            q = val_map[q_val]
            expected = val_map[expected_val]
            result = method(root, p, q)
            result_val = result.val if result else None
            status = "✅ PASS" if result == expected else "❌ FAIL"
            print(f"  Test #{i}: expected {expected_val}, got {result_val} → {status}")

if __name__ == '__main__':
    main()