#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        dict={}
        for i in tasks:
            if i in dict:
                dict[i]+=1
            else:
                dict[i]=1
        count=0
        m=max(dict.values())
        for j in dict.values():
            if j==m:
                count+=1
        return max(len(tasks),(m-1)*(n+1)+count)
                

