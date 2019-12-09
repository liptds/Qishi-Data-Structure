#!/usr/bin/env python
# coding: utf-8

# In[3]:


from collections import defaultdict
class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def pos_num(d,row,col):
            return not (d in rows[row] or d in columns[col] or  d in boxes[box_index(row, col)])
        def place_num(d,row,col):
            rows[row][d] += 1
            columns[col][d] += 1
            boxes[box_index(row, col)][d] += 1
            board[row][col] = str(d)
        def remove_number(d, row, col):
            del rows[row][d]
            del columns[col][d]
            del boxes[box_index(row, col)][d]
            board[row][col] = '.'
            
        def place_next_num(row, col):
            if col == N - 1 and row == N - 1:
                nonlocal solved
                solved = True    
            elif col == N - 1:
                backtrack(row + 1, 0)
            else:
                backtrack(row, col + 1)
        def backtrack(row = 0, col = 0):
            if board[row][col] == '.':
                for d in range(1, 10):
                    if pos_num(d, row, col):
                        place_num(d, row, col)
                        place_next_num(row, col)
                        if not solved:
                            remove_number(d, row, col)
            else:
                place_next_num(row, col)
        n = 3
        N = n * n
        box_index = lambda row, col: (row // n ) * n + col // n
        
        rows = [defaultdict(int) for i in range(N)]
        columns = [defaultdict(int) for i in range(N)]
        boxes = [defaultdict(int) for i in range(N)]
        for i in range(N):
            for j in range(N):
                if board[i][j] != '.': 
                    d = int(board[i][j])
                    place_num(d, i, j)
        
        solved = False
        backtrack()

