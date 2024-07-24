#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun  2 19:36:54 2024

@author: gq06
"""

# Our Stack Class - Brought from previous concept
# No need to modify this
class Stack:
    def __init__(self):
        self.items = []
    
    def size(self):
        return len(self.items)
    
    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.size()==0:
            return None
        else:
            return self.items.pop()

def equation_checker(equation):
    """
    Check equation for balanced parentheses

    Args:
       equation(string): String form of equation
    Returns:
       bool: Return if parentheses are balanced or not
    """
    
    
    # TODO: Intiate stack object
    stack_obj=Stack()
    
    # TODO: Interate through equation checking parentheses
    for item in equation:
        stack_obj.push(item)
    print(stack_obj.size())
    left_para=0
    right_para=0
    while stack_obj.size()>0:
        # print(stack_obj.pop())
        # print(type(stack_obj.pop()))
        check_element=stack_obj.pop()
        
        
        if check_element=='(':
            left_para+=1
        elif check_element== ')':
            right_para+=1
            
    print(' left para : ',left_para)
    print(' right para :',right_para)
    return left_para==right_para
            
        
        # print(stack_obj.pop())
    
    # TODO: Return True if balanced and False if not
    
    # pass

print(equation_checker('((32+8)∗(5/2))/(2+6'))
    