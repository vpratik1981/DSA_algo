#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun  2 22:39:48 2024

@author: gq06
"""

class LinkedListNode:

    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:

    def __init__(self):
        self.num_elements = 0
        self.head = None

    def push(self, data):
        new_node = LinkedListNode(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.num_elements += 1

    def pop(self):
        if self.is_empty():
            return None
        temp = self.head.data
        self.head = self.head.next
        self.num_elements -= 1
        return temp

    def top(self):
        if self.head is None:
            return None
        return self.head.data

    def size(self):
        return self.num_elements

    def is_empty(self):
        return self.num_elements == 0


def minimum_bracket_reversals(input_string):
    """
    Calculate the number of reversals to fix the brackets

    Args:
       input_string(string): Strings to be used for bracket reversal calculation
    Returns:
       int: Number of breacket reversals needed
    """
    stack_obj=Stack()
    
    # TODO: Write function here
    # left_brace=0
    # right_brace=0
    for item in input_string[:]:
        if stack_obj.is_empty():
            stack_obj.push(item)
        elif not item==stack_obj.top():
            stack_obj.pop()
        else:
            stack_obj.push(item)
    print(stack_obj.size())
        
    #     stack_obj.push(item)
    # print(stack_obj.size())
    
    # while  not stack_obj.is_empty():
    #     ele = stack_obj.pop()
    #     if ele=='{':
    #         left_brace+=1
    #     else:
    #         right_brace+=1
        
    #     if left_brace!=0 and right_brace
    
    # print(left_brace)
    # print(right_brace)
    
    # check=[]
    
    # while not stack_obj.is_empty():
    #     ele= stack_obj.pop()
    #     if 
        
            
        
        
    
    

test_case_1 = "}}{}{"

# minimum_bracket_reversals(test_case_1)

a=[1,2,3,4]
a.pop(0)
print(a[0])




            
        
