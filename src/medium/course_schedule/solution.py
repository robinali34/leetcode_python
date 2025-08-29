#! /usr/bin/python3
# -*- coding:utf8 -*-

# Copyright 2021 Robina Li. BSD 3-Clause License All Rights Reserved.
# @file : solution.py
# @desc : Solution for Leetcode
# Reference : https://leetcode.com/problems/course-schedule

from typing import List
from collections import deque

class Solution(object):
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = [0] * numCourses
        adj = [[] for _ in range(numCourses)]

        for prerequsite in prerequisites:
            adj[prerequsite[1]].append(prerequsite[0])
            indegree[prerequsite[0]] += 1
        queue = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)
        nodesVisited = 0
        while queue:
            node = queue.popleft()
            nodesVisited += 1
            for neighbor in adj[node]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)
        return nodesVisited == numCourses


    def canFinish2(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = [[] for _ in range(numCourses)]
        for prerequisite in prerequisites:
            adj[prerequisite[1]].append(prerequisite[0])
        visit = [False] * numCourses
        inStack = [False] * numCourses
        for i in range(numCourses):
            if self.dfs(i, adj, visit, inStack):
                return False
        return True
    def dfs(self, node, adj, visit, inStack):
        if inStack[node]:
            return True
        if visit[node]:
            return False
        visit[node] = True
        inStack[node] = True
        for neighbor in adj[node]:
            if self.dfs(neighbor, adj, visit, inStack):
                return True
        inStack[node] = False
        return False

if __name__ == '__main__':
    solution = Solution()
    rtn = solution.canFinish(2, [[1,0]])
    print(True == rtn)
    rtn = solution.canFinish(2, [[1,0],[0,1]])
    print(False == rtn)

    rtn = solution.canFinish2(2, [[1,0]])
    print(True == rtn)
    rtn = solution.canFinish2(2, [[1,0],[0,1]])
    print(False == rtn)