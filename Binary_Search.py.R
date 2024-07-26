#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 18 18:13:39 2024

@author: gq06
"""

def binary_search(input,target):
    left,right =0 , len(input)-1
    
    while left <= right:
        mid = (left+right)//2
        # mid = input[mid]
        
        if input[mid] == target :
            return input[mid]
        
        if input[mid] > target:
            right = mid -1
            # left =0 
        if input[mid] < target :
            left = mid+1
            
# print(binary_search([22,32,45,63,85,90,105], 105))

def search(input,target):
    
    input_orig = input
    
    
    
    def search_in(input,target):
        left,right =0 , len(input)-1
        
    
        mid = (left+right)//2
        
        if input[mid] == target:
            # result =mid
            
            # print(mid)
            
            y=[x for x in range(len(input_orig)) if input_orig[x]==target]
            
            return y[0]
        
        if input[mid] > target:
            right = mid-1
            input=input[0:mid]
            
        elif input[mid] < target:
            left = mid+1
            input = input[mid+1:]
        
        return search_in(input, target)
    return search_in(input, target)
        

print(search([22,32,45,63,85,90,105], 105))
    