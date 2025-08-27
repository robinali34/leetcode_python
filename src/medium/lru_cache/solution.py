#! /usr/bin/python3
# -*- coding:utf8 -*-

# Copyright 2025 Robina Li. BSD 3-Clause License All Rights Reserved.
# @file : solution.py
# @desc : Solution for Leetcode
# Reference : https://leetcode.com/problems/lru-cache/

from typing import List
import collections


from collections import OrderedDict

class ListNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.dic = {}
        self.head = ListNode(-1, -1)
        self.tail = ListNode(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key not in self.dic:
            return -1

        node = self.dic[key]
        self.remove(node)
        self.add(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.dic:
            old_node = self.dic[key]
            self.remove(old_node)

        node = ListNode(key, value)
        self.dic[key] = node
        self.add(node)

        if len(self.dic) > self.capacity:
            node_to_delete = self.head.next
            self.remove(node_to_delete)
            del self.dic[node_to_delete.key]

    def add(self, node):
        previous_end = self.tail.prev
        previous_end.next = node
        node.prev = previous_end
        node.next = self.tail
        self.tail.prev = node

    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev


class LRUCache1:
    def __init__(self, capacity: int):
        self.cache = OrderedDict()
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        # Move to end to mark as recently used
        self.cache.move_to_end(key)
        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            # Update and move to end
            self.cache.move_to_end(key)
        self.cache[key] = value
        if len(self.cache) > self.capacity:
            # Pop the least recently used item
            self.cache.popitem(last=False)

import unittest
class TestLRUCache(unittest.TestCase):
    def test_basic_operations(self):
        cache = LRUCache(2)

        cache.put(1, 1)
        cache.put(2, 2)
        self.assertEqual(cache.get(1), 1)  # returns 1

        cache.put(3, 3)  # evicts key 2
        self.assertEqual(cache.get(2), -1)  # returns -1 (not found)

        cache.put(4, 4)  # evicts key 1
        self.assertEqual(cache.get(1), -1)  # returns -1 (not found)
        self.assertEqual(cache.get(3), 3)  # returns 3
        self.assertEqual(cache.get(4), 4)  # returns 4

    def test_update_existing_key(self):
        cache = LRUCache(2)
        cache.put(1, 1)
        cache.put(1, 10)  # update value
        self.assertEqual(cache.get(1), 10)

    def test_capacity_eviction(self):
        cache = LRUCache(1)
        cache.put(1, 1)
        cache.put(2, 2)  # evict 1
        self.assertEqual(cache.get(1), -1)
        self.assertEqual(cache.get(2), 2)

    def test_ordering(self):
        cache = LRUCache(2)
        cache.put(1, 1)
        cache.put(2, 2)
        cache.get(1)      # use 1 -> now 2 is LRU
        cache.put(3, 3)   # evict 2
        self.assertEqual(cache.get(2), -1)
        self.assertEqual(cache.get(1), 1)
        self.assertEqual(cache.get(3), 3)

if __name__ == "__main__":
    unittest.main()