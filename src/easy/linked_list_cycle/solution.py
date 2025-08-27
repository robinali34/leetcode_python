#! /usr/bin/python3
# -*- coding:utf8 -*-

# Copyright 2025 Robina Li. BSD 3-Clause License All Rights Reserved.
# @file : solution.py
# @desc : Solution for Leetcode
# Reference : https://leetcode.com/problems/linked-list-cycle

from typing import List, Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def __str__(self):
        result = []
        visited = set()
        current = self
        while current and id(current) not in visited:
            visited.add(id(current))
            result.append(str(current.val))
            current = current.next
        if current:
            result.append("... (cycle detected)")
        return " -> ".join(result)

class Solution(object):
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return False
        slow = head
        fast = head.next
        while slow != fast:
            if fast is None or fast.next is None or slow is None:
                return False
            slow = slow.next
            fast = fast.next.next
        return True

    def hasCycle1(self, head: Optional[ListNode]) -> bool:
        node_seen = set()
        cur = head
        while cur is not None:
            if cur in node_seen:
                return True
            node_seen.add(cur)
            cur = cur.next
        return False

def create_linked_list(values, pos) -> ListNode:
    if not values:
        return None

    head = ListNode(values[0])
    current = head
    nodes = [head]

    for val in values[1:]:
        new_node = ListNode(val)
        current.next = new_node
        current = new_node
        nodes.append(new_node)

    if pos != -1:
        current.next = nodes[pos]  # Create the cycle

    return head

if __name__ == '__main__':
    solution = Solution()

    rtn = solution.hasCycle(create_linked_list([3,2,0,-4], 1))
    print(True == rtn)
    rtn = solution.hasCycle(create_linked_list([1,2], 0))
    print(True == rtn)
    rtn = solution.hasCycle(create_linked_list([1], -1))
    print(False == rtn)

    rtn = solution.hasCycle1(create_linked_list([3,2,0,-4], 1))
    print(True == rtn)
    rtn = solution.hasCycle1(create_linked_list([1,2], 0))
    print(True == rtn)
    rtn = solution.hasCycle1(create_linked_list([1], -1))
    print(False == rtn)