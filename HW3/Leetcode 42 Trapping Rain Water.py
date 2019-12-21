#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height)==0:
            return 0            
        idstack=[]
        ans=0
        for i,v in enumerate(height):
            while idstack!=[] and height[idstack[-1]]<v:
                bottom=height[idstack.pop()]
                if idstack==[]:
                    break
                diff=min(v,height[idstack[-1]])-bottom
                width=i-idstack[-1]-1
                ans+=diff*width
            idstack.append(i)
        return ans

