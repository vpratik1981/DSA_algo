#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun  2 20:17:25 2024

@author: gq06
"""

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class Stack:
    
    def __init__(self):
        self.head=None
        self.num_elements=0

    def push(self,val):
        new_node=Node(val)
        if self.head==None:
            self.head=new_node
            self.num_elements+=1
            return
        tmp_node=self.head
        self.head= new_node
        new_node.next=tmp_node
        self.num_elements+=1
        
    def pop(self):
        if self.num_elements ==0 :
            return None
        # while self.num_elements>0:
        tmp_node=self.head.next
        self.head=self.head.next
        self.num_elements-=1
        return tmp_node.data
    
    def size(self):
        return self.num_elements
    
    def is_empty(self):
        return self.num_elements==0
    
    def top(self):
        if self.is_empty():
            return None
        return self.head.data

def evaluate_post_fix(input_list):
    stack = Stack()
    for element in input_list:
        if element == '*':
            second = stack.pop()
            first = stack.pop()
            output = first * second
            stack.push(output)
        elif element == '/':
            second = stack.pop()
            first = stack.pop()
            output = int(first / second)
            stack.push(output)
        elif element == '+':
            second = stack.pop()
            first = stack.pop()
            output = first + second
            stack.push(output)
        elif element == '-':
            second = stack.pop()
            first = stack.pop()
            output = first - second
            stack.push(output)
        else:
            stack.push(int(element))
    return stack.pop()

def test_function(test_case):
    output = evaluate_post_fix(test_case[0])
    print(output)
    if output == test_case[1]:
        print("Pass")
    else:
        print("Fail")


test_case_1 = [["3", "1", "+", "4", "*"], 16]

test_function(test_case_1)                
            
        
    

        
        
    
    # TODO: Use stacks to control the element positions
    


            
            
        
            