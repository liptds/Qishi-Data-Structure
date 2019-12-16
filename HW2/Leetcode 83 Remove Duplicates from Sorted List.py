#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head==None:
            return
        dict={}
        fast = head
        slow = head
       
        dict[fast.val]=1
        while fast.next:
            fast=fast.next
            if fast.val in dict:
                slow.next=fast.next
            else: 
                dict[fast.val]=1
                slow=slow.next
        return head

