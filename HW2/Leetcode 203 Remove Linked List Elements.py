#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        sentinel = ListNode(0)
        sentinel.next = head
        slow, fast = sentinel, head
        while fast:
            if fast.val == val:
                slow.next = fast.next
            else:
                slow = slow.next
            fast = fast.next
        return sentinel.next

