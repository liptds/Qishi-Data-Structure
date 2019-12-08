#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        l1=len(nums1)
        l2=len(nums2)
        ans = []
        if l1 == 0 or l2 == 0:
            return []
        dict1={}
        dict2={}
        if l2>l1:
            nums1,nums2=nums2,nums1
        for i in nums1:
            if i in dict1.keys():
                dict1[i] += 1
            else:
                dict1[i] = 1
        for i in nums2:
            if i in dict2.keys():
                dict2[i] += 1
            else:
                dict2[i] = 1
        for j in dict2.keys():
            if j in dict1.keys():
                times = min(dict1[j],dict2[j])
                for k in range(times):
                    ans.append(j)
        return ans         

