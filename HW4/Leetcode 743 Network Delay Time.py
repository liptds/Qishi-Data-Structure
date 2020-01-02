#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import heapq
import math
from collections import defaultdict
class Solution:
    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
        graph=defaultdict(list)
        for u,v,w in times:
            graph[u].append((v,w))
        pq=[(0,K)]
        dist={}
        while pq:
            d,node=heapq.heappop(pq)
            if node in dist:continue
            dist[node]=d
            for neig, d2 in graph[node]:
                if neig not in dist:
                    heapq.heappush(pq,(d+d2,neig))
        return max(dist.values()) if len(dist)==N else -1

