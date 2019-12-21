#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0
        m=len(matrix)
        n=len(matrix[0])

        left = [0] * n 
        right = [n-1] * n 
        height = [0] * n        
        
        area=0
        
        for i in range(m):
            cur_left,cur_right=0,n
            for j in range(n):
                if matrix[i][j]=='1':height[j]+=1
                else: height[j]=0
            for j in range(n):
                if matrix[i][j] == '1': left[j] = max(left[j], cur_left)
                else:
                    left[j] = 0
                    cur_left = j+1
            for j in range(n-1,-1,-1):
                if matrix[i][j] == '1': right[j] =min(right[j], cur_right)
                else: 
                    right[j] = n-1
                    cur_right = j-1
            for j in range(n):
                area = max(area, height[j] * (right[j] - left[j]+1))

        return area

