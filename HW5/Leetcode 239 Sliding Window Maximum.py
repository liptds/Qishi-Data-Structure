#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n=len(nums)
        if n*k==0:
            return []
        if k==1:
            return nums
        deq=deque()
        def cmdeq(i):
            if deq and deq[0]==i-k:
                deq.popleft()
            while deq and nums[i]>=nums[deq[-1]]:
                deq.pop()
        idx_m=0
        for i in range(k):
            cmdeq(i)
            deq.append(i)
            if nums[i]>=nums[idx_m]:
                idx_m=i
        ans=[nums[idx_m]]
        for i in range(k,n):
            cmdeq(i)
            deq.append(i)
            ans.append(nums[deq[0]])
        return ans

