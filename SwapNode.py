#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 29 19:02:59 2024

@author: gq06
"""

class Node:
    def __init__(self,value):
        self.value=value
        self.next=None
def create_linked_list(inputList):
    if inputList is None:
        return 'Empty List'
    head = Node(inputList[0])
    tail= head
    
    for item in inputList[1:]:
        node=Node(item)
        tail.next=node
        tail=tail.next
    return head

def print_linked_list(head):
    
    while head is not None:
        print(head.value, end =' ')
        head = head.next
    print()

def swap_node(head, left_index, right_index):
    
    if head is None:
        return None
    
    if left_index<0 and right_index<0 and left_index>right_index:
        return head
    
    current= head
    # previous=None
    one_previous=None
    one_current=None
    two_previous=None
    two_current=None
    tmp=None
    
    
    count=0
    
    while current:
        if count==left_index-1:
            one_previous=current
            count+=1
            
        elif count==right_index-1:
            two_previous=current
            count+=1
        elif count==left_index:
            one_current=current
            count+=1
        elif count==right_index:
            two_current=current
            count+=1
        else:
            count+=1
        current=current.next
    # print(one_previous.value)
    # print(one_current.value)
    # print(two_previous.value)
    
    # print(two_current.value)
    
    two_previous.next=one_current
    # print(two_previous.next.value)
    tmp=one_current.next
    one_current.next=two_current.next
    two_current.next=tmp
    one_previous.next=two_current
    
            
        
            
    
            
    return head
                
            
        
        
input_list = [3,4,5,2,6,1,9]

head = create_linked_list(input_list)

print_linked_list(head)

head = swap_node(head, 2, 5)

print_linked_list(head)
        
        
    