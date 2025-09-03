#! /usr/bin/python3
# -*- coding:utf8 -*-

# Copyright 2025 Robina Li. BSD 3-Clause License All Rights Reserved.
# @file : solution.py
# @desc : Solution for Leetcode
# Reference : https://leetcode.com/problems/binary-search-tree-iterator/description/

from typing import List, Optional
from collections import deque
from typing import Union

class TreeNode:
    def __init__(self, val: int=0, left: Optional['TreeNode']=None, right: Optional['TreeNode']=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return f"TreeNode({self.val}, {self.left}, {self.right})"

class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.nodes_sorted = []
        self.index = -1
        self._inorder(root)

    def _inorder(self, root: TreeNode) -> None:
        if not root:
            return
        self._inorder(root.left)
        self.nodes_sorted.append(root.val)
        self._inorder(root.right)

    def next(self) -> int:
        self.index += 1
        return self.nodes_sorted[self.index]
    
    def hasNext(self) -> bool:
        return self.index + 1 < len(self.nodes_sorted)    

class BSTIterator2:

    def __init__(self, root: Optional[TreeNode]):
        self.stack = []
        self._leftmost_inorder(root)
    def _leftmost_inorder(self, root: TreeNode) -> None:
        while root:
            self.stack.append(root)
            root = root.left

    def next(self) -> int:
        topmost_node = self.stack.pop()

        if topmost_node.right:
            self._leftmost_inorder(topmost_node.right)
        return topmost_node.val

    def hasNext(self) -> bool:
        return len(self.stack) > 0


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

def BSTIterator_simulate(commands: List[str], args: List[List[Union[int, None]]], iterator_class) -> List[Union[int, bool, None]]:
    output = []
    obj = None

    for cmd, arg in zip(commands, args):
        if cmd == "BSTIterator":
            root = buildTree(arg[0])
            obj = iterator_class(root)
            output.append(None)
        elif cmd == "next":
            output.append(obj.next())
        elif cmd == "hasNext":
            output.append(obj.hasNext())
        else:
            raise ValueError(f"Unknown command: {cmd}")
    return output

# ---------- Main ----------
def main():
    commands = ["BSTIterator", "next", "next", "hasNext", "next", "hasNext", "next", "hasNext", "next", "hasNext"]
    args = [
        [[7, 3, 15, None, None, 9, 20]],
        [],
        [],
        [],
        [],
        [],
        [],
        [],
        [],
        [],
    ]
    expected_output = [None, 3, 7, True, 9, True, 15, True, 20, False]

    tests = [
        ("BSTIterator (eager full list)", BSTIterator),
        ("BSTIterator2 (lazy with stack)", BSTIterator2),
    ]

    for name, iterator_class in tests:
        print(f"\nTesting {name}:")
        result = BSTIterator_simulate(commands, args, iterator_class)
        for i, (exp, res) in enumerate(zip(expected_output, result), 1):
            status = "✅ PASS" if exp == res else "❌ FAIL"
            print(f"  Step {i}: expected {exp}, got {res} → {status}")

if __name__ == '__main__':
    main()