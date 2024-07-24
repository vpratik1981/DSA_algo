#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 22 15:04:18 2024

@author: gq06
"""

def add_one(arr):
    """
    :param: arr - list of digits representing some number x
    return a list with digits represengint (x + 1)
    """
    prev=0
    last=arr[len(arr)-1]
    arr[len(arr)-1]=last+1
    
    for count in range(len(arr)-1,-1,-1):
        if count== len(arr)-1:
            arr[len(arr)-1]=last+1
            if arr[len(arr)-1] >9:
                prev=1
                arr[count]=0
        elif count==0 and prev==1:
            arr[count]=arr[count]+1
            if arr[count]>9:
                arr_new=[]
                for i in range(len(arr)+1):
                    if i==0:
                        arr_new.append(1)
                    else:
                        arr_new.append(0)
                
                return arr_new
            
            
        else:
            if prev ==1:
                arr[count]=arr[count]+1
                if arr[count]>9:
                    prev=1
                    arr[count]=0
                else:
                    prev=0
            else:
                prev=0
    return arr
            
    
            
print(add_one([9,9,1,9]))