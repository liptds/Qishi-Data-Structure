#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import heapq
class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        heap=[]
        ans=[]
        for i in points:
            heapq.heappush(heap,(i[0]**2+i[1]**2,i[0],i[1]))
        for i in range(K):
            dist,x,y=heapq.heappop(heap)
            ans.append([x,y])
        return ans

