#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Solution:
    """
    @param hashTable: A list of The first node of linked list
    @return: A list of The first node of linked list which have twice size
    """
    def addlistnode(self,node,number):
        if node.next:
            self.addlistnode(node.next,number)
        else:
            node.next=ListNode(number)
    def addnode(self,ans,number):
        p=number%len(ans)
        if ans[p]==None:
            ans[p]=ListNode(number)
        else:
            self.addlistnode(ans[p],number)
    
    def rehashing(self, hashTable):
        # write your code here
        hash_size=2*len(hashTable)
        ans=[None for i in range(hash_size)]
        for i in hashTable:
            p=i
            while p:
                self.addnode(ans,p.val)
                p=p.next
        return ans      

