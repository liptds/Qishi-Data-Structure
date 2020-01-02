#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import math
class Solution:
    def shortestSubarray(self, A: List[int], K: int) -> int:
        n=len(A)
        res,cur=math.inf,0
        d=[[0,0]]
        for i,a in enumerate(A):
            cur+=a
            while d and cur-d[0][1]>=K:
                res=min(res,i+1-d.pop(0)[0])
            while d and cur<=d[-1][1]:
                d.pop()
            d.append([i+1,cur])
        return res if res<math.inf else -1
       

