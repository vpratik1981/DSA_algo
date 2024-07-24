#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 10 12:28:29 2024

@author: gq06
"""

# Define a function check_sudoku() here:
def check_sudoku(square):
    
    
    count_list=[ i for i in range(1,len(square)+1)]

    

    # for item in count_list:
    #     if item not in square[count] and square[count].count(item)>1 and len(square[count])>len(count_list):
    #         return False
    #     else:
    #         count+=1

    
    for ele in square:
        for item in count_list:
            if item not in ele or ele.count(item)>1:
                return False


            
    for ele in list(zip(*square)):
        # print(ele)
        for item in count_list:
            if item not in ele or ele.count(item)>1:
                return False
               

    # check_sum= sum(count_list)            
        
    return True
    
# Test cases
correct = [[1,2,3],
            [2,3,1],
            [3,1,2]]
incorrect = [[1,2,3,4],
              [2,3,1,3],
              [3,1,2,3],
              [4,4,4,4]]
incorrect2 = [[1,2,3,4],
              [2,3,1,4],
              [4,1,2,3],
              [3,4,1,2]]
incorrect3 = [[1,2,3,4,5],
              [2,3,1,5,6],
              [4,5,2,1,3],
              [3,4,5,2,1],
              [5,6,4,3,2]]
incorrect4 = [['a','b','c'],
              ['b','c','a'],
              ['c','a','b']]
incorrect5 = [ [1, 1.5],
                [1.5, 1]]

    
print(check_sudoku(incorrect))
# #>>> False
print(check_sudoku(correct))
# #>>> True
print(check_sudoku(incorrect2))
# #>>> False
print(check_sudoku(incorrect3))
# #>>> False
print(check_sudoku(incorrect4))
# #>>> False
print(check_sudoku(incorrect5))
# #>>> False