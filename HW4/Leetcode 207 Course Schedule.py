#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        G=[[]for i in range(numCourses)]
        rec=[0]*numCourses
        for j,i in prerequisites:
            G[i].append(j)
            rec[j]+=1
        start=[i for i in range(numCourses) if rec[i]==0]
        for i in start:
            for j in G[i]:
                rec[j]-=1
                if rec[j]==0:
                    start.append(j)
        if rec==[0]*numCourses:
            return True
        else:
            return False

