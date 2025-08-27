#! /usr/bin/python3
# -*- coding:utf8 -*-

# Copyright 2025 Robina Li. BSD 3-Clause License All Rights Reserved.
# @file : solution.py
# @desc : Solution for Leetcode
# Reference : https://leetcode.com/problems/reverse-linked-list/

from typing import List, Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def __str__(self):
        result = []
        cur = self
        while cur:
            result.append(cur.val)
            cur = cur.next
        return " -> ".join(str(i) for i in result)

class Solution(object):
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        cur = head
        while cur:
            next_tmp = cur.next
            cur.next = prev
            prev = cur
            cur = next_tmp
        return prev

    def reverseList1(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        p = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return p

def create_linked_list(nums: List[int]) -> ListNode:
    if not nums:
        return None
    head = ListNode(nums[0])
    cur = head
    for i in range(1, len(nums)):
        cur.next = ListNode(nums[i])
        cur = cur.next
    return head

if __name__ == '__main__':
    solution = Solution()

    head = create_linked_list([1,2,3,4,5])
    print(head)
    rtn = solution.reverseList(head)
    print(rtn)

    head = create_linked_list([1,2])
    print(head)
    rtn = solution.reverseList(head)
    print(rtn)

    head = create_linked_list([])
    print(head)
    rtn = solution.reverseList(head)
    print(rtn)

    head = create_linked_list([1,2,3,4,5])
    print(head)
    rtn = solution.reverseList1(head)
    print(rtn)

    head = create_linked_list([1,2])
    print(head)
    rtn = solution.reverseList1(head)
    print(rtn)

    head = create_linked_list([])
    print(head)
    rtn = solution.reverseList1(head)
    print(rtn)