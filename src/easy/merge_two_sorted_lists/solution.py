#! /usr/bin/python3
# -*- coding:utf8 -*-

# Copyright 2025 Robina Li. BSD 3-Clause License All Rights Reserved.
# @file : solution.py
# @desc : Solution for Leetcode
# Reference : https://leetcode.com/problems/merge-two-sorted-lists

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
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None:
            return list2
        elif list2 is None:
            return list1
        elif list1.val < list2.val:
            list1.next = self.mergeTwoLists(list1.next, list2)
            return list1
        else:
            list2.next = self.mergeTwoLists(list1, list2.next)
            return list2

    def mergeTwoLists1(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        prehead = ListNode(-1)
        prev = prehead
        while list1 and list2:
            if list1.val <= list2.val:
                prev.next = list1
                list1 = list1.next
            else:
                prev.next = list2
                list2 = list2.next
            prev = prev.next
        prev.next = list1 if list1 is not None else list2
        return prehead.next

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

    list1 = create_linked_list([1,2,4])
    list2 = create_linked_list([1,3,4])
    print("list1: ", list1)
    print("list2: ", list2)
    rtn = solution.mergeTwoLists(list1, list2)
    print("Merged: ", rtn)

    list1 = create_linked_list([])
    list2 = create_linked_list([])
    print("list1: ", list1)
    print("list2: ", list2)
    rtn = solution.mergeTwoLists(list1, list2)
    print("Merged: ", rtn)

    list1 = create_linked_list([])
    list2 = create_linked_list([0])
    print("list1: ", list1)
    print("list2: ", list2)
    rtn = solution.mergeTwoLists(list1, list2)
    print("Merged: ", rtn)

    list1 = create_linked_list([1,2,4])
    list2 = create_linked_list([1,3,4])
    print("list1: ", list1)
    print("list2: ", list2)
    rtn = solution.mergeTwoLists1(list1, list2)
    print("Merged: ", rtn)

    list1 = create_linked_list([])
    list2 = create_linked_list([])
    print("list1: ", list1)
    print("list2: ", list2)
    rtn = solution.mergeTwoLists1(list1, list2)
    print("Merged: ", rtn)

    list1 = create_linked_list([])
    list2 = create_linked_list([0])
    print("list1: ", list1)
    print("list2: ", list2)
    rtn = solution.mergeTwoLists1(list1, list2)
    print("Merged: ", rtn)
