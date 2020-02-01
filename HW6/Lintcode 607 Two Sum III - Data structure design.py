#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class TwoSum:
    """
    @param number: An integer
    @return: nothing
    """
    
       
    def __init__(self):
        self.num_list = []
    
    def add(self, number):
        # write your code here
        self.num_list.append(number)
    """
    @param value: An integer
    @return: Find if there exists any pair of numbers which sum is equal to the value.
    """
    def find(self, value):
        # write your code here
        dict = {}
        for number in self.num_list:
            target=value-number
            if number in dict:
                return True
            dict[target]=1
        return False

