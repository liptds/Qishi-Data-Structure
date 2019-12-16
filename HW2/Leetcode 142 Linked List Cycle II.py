#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        visited={}
        node = head
        while node is not None:
            if node in visited:
                return node
            else:
                visited[node]=1
                node=node.next
        return None

