#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class BSTIterator:

    def __init__(self, root: TreeNode):
        self.stack=[]
        self.order(root)
    
    def order(self,root):
        while root:
            self.stack.append(root)
            root=root.left
        
    def next(self) -> int:
        """
        @return the next smallest number
        """
        temp=self.stack.pop()
        if temp.right:
            self.order(temp.right)
        return temp.val

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        return len(self.stack)>0

