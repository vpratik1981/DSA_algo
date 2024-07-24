#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 27 20:38:42 2024

@author: gq06
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def createLinkedList(arr):
    if len(arr)==0:
        return None
    head = Node(arr[0])
    tail=head
    
    for item in range(1,len(arr)):
        tail.next = Node(arr[item])
        # head.next = node
        tail=tail.next
    return head

def even_after_odd(head):
    """
    :param - head - head of linked list
    return - updated list with all even elements are odd elements
    """
    final_linkedList_head= None
    even_only=[]
    odd_only=[]
    
    tail=head
    
    while tail is not None :
        if tail.data%2==0:
            # print(tail.data)
            even_only.append(tail.data)
        # tail=tail.next
        else:
            # print(tail.data)
            odd_only.append(tail.data)
        tail=tail.next
    # print(odd_only)
    # print(even_only)
    final_linkedList_head=Node(odd_only[0])
    final_linkedList_tail = final_linkedList_head
    for i in range(1,len(odd_only)):
        final_linkedList_tail.next=Node(odd_only[i])
        final_linkedList_tail=final_linkedList_tail.next
    
    for j in range(len(even_only)):
        final_linkedList_tail.next=Node(even_only[j])
        final_linkedList_tail=final_linkedList_tail.next
        
        # while final_linkedList_tail.next not None:
            
        
    
    return final_linkedList_head
        
        
        



arr=[1,2,3,4,5,6]

head = createLinkedList(arr)

# print(head.data)

head1=even_after_odd(head)

node = head1

while node is not  None:
    print(node.data)
    node=node.next
    
