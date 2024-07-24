#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 27 18:22:22 2024

@author: gq06
"""

def nth_row_pascal(n):
    """
    :param: - n - index (0 based)
    return - list() representing nth row of Pascal's triangle
    1
    1,1
    1,2,1
    1,3,3,1
    """
    current_row=[1]

    
    if n==0:
        return current_row
    # prev_ele=0
    
    for i in range(1,n+1):
        prev_row=current_row
        current_row=[1]
        for j in range(1,i):
            next_number = prev_row[j-1]+prev_row[j]
            current_row.append(next_number)
        current_row.append(1)
    return current_row
            
    
nth_row_pascal(3)