#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import random
class RandomizedCollection:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dict={}
        self.num=[]

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        """
        n=len(self.num)
        self.num.append(val)
        if val in self.dict:
            self.dict[val].add(n)
            return False
        else:
            self.dict[val]=set([n])
            return True
        
    def remove(self, val: int) -> bool:
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        """
        if self.num==[] or val not in self.dict:
            return False
        else:
            lidx=len(self.num)-1
            litm=self.num[-1]
            idx=self.dict[val].pop()
            
            self.dict[litm].add(idx)
            self.dict[litm].remove(lidx)
            self.num[idx]=self.num[lidx]
            
            self.num.pop()
            if len(self.dict[val])==0:
                del self.dict[val]
            return True

        
    def getRandom(self) -> int:
        """
        Get a random element from the collection.
        """
        
        return self.num[random.randint(0,len(self.num)-1)] if len(self.num)>0 else -1

