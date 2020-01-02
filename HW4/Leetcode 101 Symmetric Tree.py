#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if root:
            return(self.dfs(root.left,root.right))
        else:
            return True
        
    def dfs(self,left,right):
        if left and right:
            return (left.val==right.val) and self.dfs(left.left,right.right) and self.dfs(right.left,left.right)
        elif not left and not right:
            return True
        else:
            return False

