#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 29 14:57:36 2024

@author: gq06
"""

class Node:
    def __init__(self,value):
        self.value=value
        self.next=None
        self.previous=None
    def remove(self,head,value):
        if head is None :
            return
        
        node= self.head
        
        if node.value==self.value:
            head.next=head.next.next
            return
        
        node= head    
        while node.next is not None:
            if value==node.next.value:
                node.next=node.next.next
                return
            node=node.next
        return

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
    
        
# def skip_i_delete_j(head,i,j):   
#     if head is None:
#         return 'empty linked list'
    
#     node= head
#     previous=None
#     count =1
    
#     while node.next is not None:
        
#         node.next=node.next.next
#         print(node.value)
        
        
        
#         # if count>i and count<=i+j-1:
#         #     print(previous.value)
#         #     previous.next=node.next
#         #     previous=node
#         #     print(previous.value)
#         #     node=node.next
#         #     print(node.value)
#         #     count+=1

#         # if count<=i:
           
#         #     print(node.value)
#         #     previous=node
#         #     node=node.next
#         #     count+=1
#         #     # break
            
#         # if count == i+j-1:
#         #     count=1
#     return head


def skip_i_delete_j(head, i, j):
    # Edge case - Skip 0 nodes (means Delete all nodes)
    if i == 0:
        return None
    
    # Edge case - Delete 0 nodes
    if j == 0:
        return head
    
    # Invalid input
    if head is None or j < 0 or i < 0:
        return head

    # Helper references
    current = head
    previous = None
    
    # Traverse - Loop untill there are Nodes available in the LinkedList
    while current:
        for _ in range(i-1):
            if current is None:
                return head
            current=current.next
        # print(current.value)
        previous = current
        current=current.next
        
        for _ in range(j):
            if current is None:
                return head
            current=current.next
        
        previous.next=current
        
            
            

    # Loop ends
    
    return head

input_list = [1,2,3,4,5,6,7,8,9,10,11,12]

head = create_linked_list(input_list)

print_linked_list(head)

head = skip_i_delete_j(head, 2, 3)

print_linked_list(head)


            
            
        
                
                
                
                
    