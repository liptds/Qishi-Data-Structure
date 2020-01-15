#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import heapq
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        heap=[]
        intervals.sort(key=lambda x:x[0])
        res=0
        for interval in intervals:
            while heap and heap[0]<=interval[0]:
                heapq.heappop(heap)
            heapq.heappush(heap,interval[1])
            res=max(len(heap),res)
        return res
            

