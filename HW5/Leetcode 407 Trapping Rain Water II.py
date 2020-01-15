#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import heapq
class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        if not heightMap or not heightMap[0]: return 0
        m=len(heightMap)
        n=len(heightMap[0])
        heap=[]
        seen=set()
        for i in range(n):
            heapq.heappush(heap,(heightMap[0][i],0,i))
            heapq.heappush(heap,(heightMap[m-1][i],m-1,i))
            seen.add((0,i))
            seen.add((m-1,i))
        for j in range(m):
            heapq.heappush(heap,(heightMap[j][0],j,0))
            heapq.heappush(heap,(heightMap[j][n-1],j,n-1))
            seen.add((j,0))
            seen.add((j,n-1))
        ans=0
        while heap:
            d,x,y=heapq.heappop(heap)
            for dx,dy in [(-1,0),(1,0),(0,1),(0,-1)]:
                new_x,new_y=x+dx,y+dy
                if new_x>=0 and new_x<m and new_y>=0 and new_y<n and (new_x,new_y) not in seen:
                    seen.add((new_x,new_y))
                    ans+=max(0,d-heightMap[new_x][new_y])
                    heapq.heappush(heap,(max(heightMap[new_x][new_y],d),new_x,new_y))
        return ans

