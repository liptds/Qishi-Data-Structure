#!/usr/bin/env python
# coding: utf-8

# In[25]:


class Queue:
    def __init__(self):
        self.items=[]
    def enqueue(self,item):
        self.items.append(item)
    def dequeue(self):
        return self.items.pop(0)
    def isEmpty(self):
        return self.items==[]
    def size(self):
        return len(self.items)
    def qprint(self):
        print(self.items)


# In[42]:


def hotpotato(namelist,num):
    q=Queue()
    for i in namelist:
        q.enqueue(i)
    while q.size()>1:
        for i in range(num-1):
            q.enqueue(q.dequeue())
        print(q.dequeue())
        
    return q
        
    


# In[43]:


namelist=['Bill','James','John','Justin']


# In[47]:


hotpotato(namelist,3).qprint()

