#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Solution:
    def decodeString(self, s: str) -> str:
        stack=[]
        stack.append(['',1])
        num=''
        for char in s:
            if char.isdigit():
                num+=char
            elif char=='[':
                stack.append(['',int(num)])
                num=''
            elif char==']':
                string,time=stack.pop()
                stack[-1][0]+=string*time
            else:
                stack[-1][0]+=char
        return stack[0][0]

