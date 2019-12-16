#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class DLinkedNode():
    def __init__(self):
        self.key=0
        self.value=0
        self.prev=None
        self.next=None
        
class LRUCache():
    def __init__(self, capacity):
        self.cache={}
        self.size=0
        self.capacity=capacity
        self.head,self.tail=DLinkedNode(),DLinkedNode()
        self.head.next=self.tail
        self.tail.prev=self.head
    def remove_node(self,node):
        prev=node.prev
        nex=node.next
        prev.next=nex
        nex.prev=prev
        
    def move_to_head(self,node):
        self.remove_node(node)
        self.add_node(node)
        
    def pop_tail(self):
        temp=self.tail.prev
        self.remove_node(temp)
        return temp
    
    
    def add_node(self,node):
        node.prev=self.head
        node.next=self.head.next
        self.head.next.prev=node
        self.head.next=node
        
        
    def get(self, key):
        node=self.cache.get(key,None)
        if not node:
            return -1
        self.move_to_head(node)
        return node.value

    def put(self, key, value):
        node = self.cache.get(key,None)
        if not node:
            newNode=DLinkedNode()
            newNode.key=key
            newNode.value=value
            self.cache[key]=newNode
            self.add_node(newNode)
            self.size+=1
            if self.size>self.capacity:
                tail=self.pop_tail()
                del self.cache[tail.key]
                self.size-=1
        else:
            node.value=value
            self.move_to_head(node)

