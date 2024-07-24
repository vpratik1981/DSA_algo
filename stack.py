#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun  2 14:43:04 2024

@author: gq06
"""

class Node:
    def __init__(self,value):
        self.value=value
        self.next=None
class Stack:
    # def __init__(self,size=10):
    #     self.arr = [0 for _ in range(size)]
    #     self.next_index=0
    #     self.num_elements=0
    # def push(self,ele):
    #     if self.next_index==len(self.arr):
    #         self.arr= self.handle_stack_capacity_full()
    #     self.arr[self.next_index]=ele
    #     self.next_index=self.next_index+1
    #     self.num_elements+=1
    #     return self.arr
        
    # def handle_stack_capacity_full(self):
    #     old_arr=self.arr
    #     new_arr=[0 for _ in range(len(self.arr)*2)]
    #     for i in range(len(old_arr)):
    #         new_arr[i]=old_arr[i]
    #     return new_arr
    # def size(self):
    #     return self.num_elements
    # def is_empty(self):
    #     if self.num_elements==0:
    #         return True
    #     return False
    # def pop(self):
    #     if self.num_elements==0:
    #         return None
    #     self.next_index-=1
    #     self.num_elements-=1
    #     return self.arr[self.next_index-1]
    
    def __init__(self):
        self.head=None
        self.num_elements=0
        
    def push(self,ele):
        new_node=Node(ele)
        
        if self.head is None:
            self.head=new_node
        else:
            current_node=self.head
            # new_node.next=self.head
            self.head =new_node
            new_node.next=current_node
        # print(self.head.value)
        self.num_elements+=1
        
    def size(self):
        
        return self.num_elements
    
    def is_empty(self):
        return self.num_elements==0
    
    def pop(self):
        if self.head is None:
            return None
        current_node = self.head
        # print(current_node.value)
        self.head= current_node.next
        self.num_elements-=1
        
        return current_node.value
        
    
    
    
        
        
        
# foo = Stack()
# foo.push("Test") # We first have to push an item so that we'll have something to pop
# print(foo.pop()) # Should return the popped item, which is "Test"
# print(foo.pop()) # Should return None, since there's nothing left in the stack

# print(foo.is_test(1))

# Setup
stack = Stack()
stack.push(10)
stack.push(20)
stack.push(30)
stack.push(40)
stack.push(50)

# Test size
print ("Pass" if (stack.size() == 5) else "Fail")

# Test pop
print ("Pass" if (stack.pop() == 50) else "Fail")

# Test push
stack.push(60)
print ("Pass" if (stack.pop() == 60) else "Fail")
print ("Pass" if (stack.pop() == 40) else "Fail")
print ("Pass" if (stack.pop() == 30) else "Fail")
stack.push(50)
print ("Pass" if (stack.size() == 3) else "Fail")