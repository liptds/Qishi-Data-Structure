#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def partition(left,right,pivot_index):
            pivot=nums[pivot_index]
            nums[pivot_index],nums[right]=nums[right],nums[pivot_index]
            store_index=left-1
            for i in range(left,right):
                if nums[i]<pivot:
                    store_index+=1
                    nums[i],nums[store_index]=nums[store_index],nums[i]
            nums[right],nums[store_index+1]=nums[store_index+1],nums[right]
            return store_index+1
        def select(left,right,k_smallest):
            if left==right:
                return nums[left]
            pivot_index=left
            pivot_index=partition(left,right,pivot_index)
            if k_smallest==pivot_index:
                return nums[k_smallest]
            elif k_smallest<pivot_index:
                return select(left,pivot_index-1,k_smallest)
            else:
                return select(pivot_index+1,right,k_smallest)
        return select(0,len(nums)-1,len(nums)-k)

