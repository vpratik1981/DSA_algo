#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun  2 19:11:20 2024

@author: gq06
"""

class Stack:
    def __init__(self):
        self.items=[]
         # TODO: Initialize the Stack
            
    
    def size(self):
        return len(self.items)
         # TODO: Check the size of the Stack
    
    def push(self, item):
         # TODO: Push item onto Stack
        self.items.append(item)
        

    def pop(self):
        if len(self.items)==0:
            return None
         # TODO: Pop item off of the Stack
        self.items.pop(len(self.items)-1)
    
MyStack = Stack()

MyStack.push("Web Page 1")
MyStack.push("Web Page 2")
MyStack.push("Web Page 3")

print (MyStack.items)
MyStack.pop()
MyStack.pop()

print ("Pass" if (MyStack.items[0] == 'Web Page 1') else "Fail")
MyStack.pop()

print ("Pass" if (MyStack.pop() == None) else "Fail")

    