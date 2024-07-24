#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 12 14:05:34 2024

@author: gq06
"""

def reverse_string(input):
    len_input = len(input)
    
    if len_input == 0:
        return ""
    else:
        # print(input[-1])
        # print(input[-(len_input-1)])
        return input[-1]+reverse_string(input[0:len_input-1])
    
print(reverse_string('abcdef'))