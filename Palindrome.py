#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 12 18:01:48 2024

@author: gq06
"""

def is_palindrome(input):
    
    
    
    # result_str=''
    
    def check_pali(input):
        len_input=len(input)
    
        if len_input == 0:
            return ''
        
        return input[-1] + check_pali(input[0:len_input-1])
    result_str = check_pali(input)
    
    if input == result_str:
        return True
    else:
        return False

# print(is_palindrome('abcd'))


def add_one(input):
    if len(input)==0:
        return
    
    res_arr = []
    len_input_orig = len(input)
    
    
    # def add(input):
    
        
    def add_internal(input,carry_over):
        len_input = len(input)
        num = input[len_input-1]

        if len_input ==1 and input[len_input-1]<9 and carry_over==0:
            return res_arr.append(input[len_input-1])
        elif len_input==1 and input[len_input-1]==9 and carry_over==1:
            res_arr.append(0)
            return res_arr.append(1)
        if carry_over >0 :
            num =num+1
        elif carry_over == 0 and len_input_orig == len_input:
            num = num+1
        
        if num<=9:
            res_arr.append(num)
            carry_over=0
        else:
            res_arr.append(0)
            carry_over=1
        
        return add_internal(input[0:len_input-1], carry_over)
    add_internal(input,0)
    return res_arr[::-1]

# print(add_one([9,9,9,9]))

test =[1,2,3]

# print(test[:-1])

def add_one_1(input):
    if len(input)==0:
        return 'Invalid Array'
    else:
        if input[-1]==9:
            return add_one(input[:-1]) +[0]
        else:
            input[-1]+=1
            return input
print(add_one_1([9,9,9]))
    

        