#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode, c=0) -> ListNode:
        ans=ListNode(0)
        ans_temp=ans
        while l1 or l2 or c:
            val1=l1.val if l1 else 0
            val2=l2.val if l2 else 0
            c,out=(val1+val2+c)//10,(val1+val2+c)%10
            ans_temp.next=ListNode(out)
            ans_temp=ans_temp.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return ans.next
        

