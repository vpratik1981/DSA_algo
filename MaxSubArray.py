#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 23 19:46:34 2024

@author: gq06
"""

def maxSubArray(arr):
    sum_max=arr[0]
    current_sum =arr[0]
    
    for ele in arr[1:]:
        current_sum = max(current_sum + ele, ele)
        sum_max = max(sum_max,current_sum)
    
    
    return sum_max
    
arr = [-12, 15, -13, 14, -1, 2, 1, -5, 4]
maxSubArray(arr)
    