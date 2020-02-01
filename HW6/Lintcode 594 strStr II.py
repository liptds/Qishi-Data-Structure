#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Solution:
    """
    @param: source: A source string
    @param: target: A target string
    @return: An integer as index
    """
    def strStr2(self, source, target):
        # write your code here
        if source is None or target is None:
            return -1
        n=len(source)
        m=len(target)
        if m==0: return 0
        if n<m: return -1
        q=10**7
        d=31
        s,t,h=0,0,1
        
        for i in range(m-1):
            t=(d*t+ord(target[i]))%q
            s=(d*s+ord(source[i]))%q
            h=(h*d)%q
        t=(d*t+ord(target[m-1]))%q
        for i in range(m-1,n):
            s=(d*s+ord(source[i]))%q
            print(i)
            if t==s and target==source[i-m+1:i+1]:
                return i-m+1
            if i==n-1:
                return -1
            s=(s-h*ord(source[i-m+1]))%q
            if s<0:
                s=s+q

