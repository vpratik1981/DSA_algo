#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 16 20:41:14 2024

@author: gq06
"""

import os
def find_files(suffix,path):
    result=[]
    
    # if  os.path.isdir(path):
        # result.append(path)
    
    # print(os.listdir(path))
    # print(os.path.isdir(path))
    # print(os.path.isfile(path))
    def check_isdir(path):
        
        if not os.path.isdir(path):
            return 
        
        if os.path.isdir(path):
            # result.append(path)
            for element in os.listdir(path):
                
                path1=os.path.join(path,element)
                
                if os.path.isfile(path1) and path1.endswith('.c'):
                    result.append(path1)
                    
                    
                # if not os.path.isfile(path1):
                    # result.append(path1)
                check_isdir(path1)
                # else:
                    
                    # pass
    
            # if os.path.is(element):
            #     result.append(path)
            # elif os.path.isdir(os.path.join(a, paths))
    check_isdir(path)
    print(len(result))
    print(result)
        
    
find_files('.c', '/Users/gq06/Downloads/testdir')
    
    