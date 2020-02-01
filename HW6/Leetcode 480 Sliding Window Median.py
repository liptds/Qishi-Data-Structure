#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import heapq
class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        def med(h1,h2,k):
            return h1[0][0] if k%2 else (h1[0][0]-h2[0][0])/2.0
        small,big=[],[]
        for i in range(k):
            heapq.heappush(big,(nums[i],i))
        for i in range(k//2):
            val,idx=heapq.heappop(big)
            heapq.heappush(small,(-val,idx))
       
        ans=[med(big,small,k)]
        for i in range(k,len(nums)):

            if nums[i]>=big[0][0]:
                heapq.heappush(big,(nums[i],i))
                if nums[i-k]<=big[0][0]:
                    val,idx=heapq.heappop(big)
                    heapq.heappush(small,(-val,idx))
            else:
                heapq.heappush(small,(-nums[i],i))
                if nums[i-k]>=big[0][0]:
                    val,idx=heapq.heappop(small)
                    heapq.heappush(big,(-val,idx))
            while small and small[0][1]<=i-k:
                heapq.heappop(small)
            while big and big[0][1]<=i-k:
                heapq.heappop(big)
            ans.append(med(big,small,k))    
        return ans

