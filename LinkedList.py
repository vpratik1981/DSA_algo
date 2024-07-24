#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 18 14:16:56 2024

@author: gq06
"""

"""
Step 1. Once you've seen the walkthrough, give it a try for yourself:
Create a Node class with value and next attributes
Use the class to create the head node with the value 2
Create and link a second node containing the value 1
Try printing the values (1 and 2) on the nodes you created (to make sure that you can access them!)
"""

class Node:
    def __init__(self,value):
        self.value=value
        self.next=None
    def print_LinkedList(head):
        current_head = head
        while current_head is not None:
            print(current_head.value)
            current_head = current_head.next
    
def create_linked_list(input_list):
    head = None
    for value in input_list:
        if head is None:
            head = Node(value)    
        else:
        # Move to the tail (the last node)
            current_node = head
            while current_node.next:
                current_node = current_node.next
        
            current_node.next = Node(value)
    return head

def create_linked_list_better(input_list):
    head = None
    tail = None
    
    for value in input_list:
        if head is None:
            head=Node(value)
            tail=head
        else:
            tail.next=Node(value)
            tail=tail.next
            
    return head

# result = create_linked_list_better([1,2,3,4,5])
# Node.print_LinkedList(result)

class LinkedList:
    def __init__(self):
        self.head=None
    def append(self, value):
        if self.head is None:
            self.head = Node(value)
            return
        node=self.head
        while node.next:
            node=node.next
        node.next=Node(value)
        return 
    
    def to_list(self):
        out_list=[]
        node=self.head
        while node is not None:
            out_list.append(node.value)
            node=node.next
        return out_list
    
        

    
obj_linked_list = LinkedList()
obj_linked_list.append(1)
obj_linked_list.append(2)
obj_linked_list.append(3)

print(obj_linked_list.to_list())

# node = obj_linked_list.head
# while node is not None:
#     print(node.value)
#     node=node.next
            
    



                
             






# head=Node(2)
# head.next=Node(1)
# head.next.next=Node(4)
# head.next.next.next=Node(3)
# head.next.next.next.next=Node(5)

# print(head.value)
# print(head.next.value)
# print(head.next.next.value)
# print(head.next.next.next.value)
# print(head.next.next.next.next.value)

# Node.print_LinkedList(head)    
    