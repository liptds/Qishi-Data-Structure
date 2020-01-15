#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import heapq
class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.med, self.odd, self.heaps = 0, 0, [[], []]

    def addNum(self, x: int) -> None:
        big, small = self.heaps
        if self.odd:
            heapq.heappush(big, max(x, self.med))
            heapq.heappush(small, -min(x, self.med))
            self.med = (big[0] - small[0]) / 2.0
        else:
            if x > self.med:
                self.med = heapq.heappushpop(big, x)
            else:
                self.med = -heapq.heappushpop(small, -x)
        self.odd ^= 1
                
    def findMedian(self) -> float:
        return self.med

