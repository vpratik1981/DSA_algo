#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 13 17:44:27 2024

@author: gq06
"""

def permute(nums):
    """
    Args:
        nums (list): list of items to be permuted.

    Returns: 
        list: list of permutation with each permuted item being represented by a list.
    """
    if len(nums) <= 1:
        return [nums[:]]
    
    result = []
    
    for i in range(len(nums)):
        item = nums.pop(0)
        perms = permute(nums)
        for perm in perms:
            perm.append(item)
        result.extend(perms)
        nums.append(item)
        
    return result
        

print(permute([1,2,3]))
    
    