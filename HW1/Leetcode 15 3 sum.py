#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans=set()
        for i in range(len(nums)):
            low,high=i+1,len(nums)-1
            while low<high:
                x=nums[i]+nums[low]+nums[high]
                if x==0:
                    ans.add((nums[i],nums[low],nums[high]))
                    low+=1
                    high-=1
                elif x>0:
                    high-=1
                elif x<0:
                    low+=1
        return list(ans)

