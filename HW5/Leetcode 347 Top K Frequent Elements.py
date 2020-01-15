#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict={}
        for i in nums:
            if i in dict:
                dict[i]+=1
            else:
                dict[i]=1
        heap=[]
        for i in dict:
            heapq.heappush(heap,(-dict[i],i))
        ans=[]
        for i in range(k):
            key,value=heapq.heappop(heap)
            ans.append(value)
        return ans

