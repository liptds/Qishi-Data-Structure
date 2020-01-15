#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import heapq
class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        events=sorted([(l,-h,r) for l,r,h in buildings]+list({(r,0,0) for l,r,h in buildings}))
        hp=[(0,float('inf'))]
        ans=[[0,0]]
        for l,negh,r in events:
            while l>=hp[0][1]:
                heapq.heappop(hp)
            if negh:
                heapq.heappush(hp,(negh,r))
            if hp[0][0]+ans[-1][1]!=0:
                ans.append([l,-hp[0][0]])
        return ans[1:]

