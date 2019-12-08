#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 0:
            return -1
        if len(nums) == 1:
            return 0 if nums[0] == target else -1

        def find_rotate_index():
            left,right=0,len(nums)-1
            if nums[left]<nums[right]:
                return 0
            while left<=right:
                pivot=(left+right)//2
                if nums[pivot]>nums[pivot+1]:
                    return pivot+1
                elif nums[pivot]<nums[left]:
                    right=pivot-1
                else: left=pivot+1
        
        def my_search(a,target):
            left,right=0,len(a)-1
            while left<=right:
                pivot=(left+right)//2
                if a[pivot] == target:
                    return pivot
                elif a[pivot]>target:
                    right=pivot-1
                else: left=pivot+1
            return -1
        ri=find_rotate_index()
       
        if ri == 0:
            return my_search(nums[0:len(nums)],target)
        if nums[0]>target:
            ans=my_search(nums[ri:len(nums)],target)
            return ri+ans if ans!=-1 else -1
        if nums[len(nums)-1]<target:
            return my_search(nums[0:ri+1],target)

