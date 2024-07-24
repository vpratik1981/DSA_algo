#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul  7 18:11:23 2024

@author: gq06
"""
import os
def find_files(suffix,path):
    
    # print(os.listdir("/Users/gq06/"))
    
    if path == None:
        return None
    list_of_files = []
    dir_list = os.listdir(path)
    
    for element in dir_list :
        tmp_path = os.path.join(path, element)
        
        if os.path.isfile(tmp_path) and tmp_path.endswith(suffix):
            list_of_files.append(tmp_path)
        elif os.path.isdir(tmp_path):
            list_of_files +=find_files(suffix, tmp_path)
    
    
    return list_of_files

print("****Empty test directory****")        
print(find_files(".py", "/Users/gq06/"))