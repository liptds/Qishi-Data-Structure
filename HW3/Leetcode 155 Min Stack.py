#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack=[]
        self.minstack=[]
        

    def push(self, x: int) -> None:
        self.stack.append(x)
        if self.minstack==[]:
            self.minstack.append(x)
        elif x<self.minstack[-1]:
            self.minstack.append(x)
        else:
            self.minstack.append(self.minstack[-1])
                
    def pop(self) -> None:
        self.stack.pop()
        self.minstack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minstack[-1]

