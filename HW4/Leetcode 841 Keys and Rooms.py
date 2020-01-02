#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        if rooms==[[]]:
            return True
        queue=[]
        visited=set()
        visited.add(0)
        for i in rooms[0]:
            queue.append(i)
            
        while queue:
            a=queue.pop(0)
            if a in visited:
                continue
            else:
                visited.add(a)
                for j in rooms[a]:
                    queue.append(j)
        if len(visited)==len(rooms):
            return True
        else:
            return False

