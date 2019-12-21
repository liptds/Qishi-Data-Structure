#!/usr/bin/env python
# coding: utf-8

# In[1]:


class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        left=0
        right=0
        for char in s:
            if char=='(':
                left+=1
            elif char==')':
                if left==0:
                    right+=1
                else:
                    left-=1
            
        self.ans=set()
        def dfs(depth,left,right,left_rem,right_rem,cur):
            if depth==len(s):
                if left == right and left_rem==0 and right_rem==0:
                    self.ans.add(cur)
            else:
                if s[depth] == "(":
                    if left_rem > 0: 
                        dfs(depth + 1, left, right, left_rem - 1, right_rem, cur)
                    dfs(depth + 1, left + 1, right, left_rem, right_rem, cur + "(")  
                elif s[depth] == ")":
                    if right_rem > 0: 
                        dfs(depth + 1, left, right, left_rem, right_rem - 1, cur)
                    if left > right:
                        dfs(depth + 1, left, right + 1, left_rem, right_rem, cur + ")")
                else:  
                    dfs(depth + 1, left, right, left_rem, right_rem, cur + s[depth]) 
        dfs(0,0,0,left,right,'')
        return list(self.ans)

