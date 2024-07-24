#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 21 18:02:26 2024

@author: gq06
"""

# Helper code

# A class behaves like a data-type, just like an int, float or any other built-in ones. 
# User defined class
class Node:
    def __init__(self, value): # <-- For simple LinkedList, "value" argument will be an int, whereas, for NestedLinkedList, "value" will be a LinkedList
        self.value = value
        self.next = None
    
    def __repr__(self):
        return str(self.value)
    
# User defined class
class LinkedList: 
    def __init__(self, head): # <-- Expects "head" to be a Node made up of an int or LinkedList
        self.head = head
    
    '''
    For creating a simple LinkedList, we will pass an integer as the "value" argument
    For creating a nested LinkedList, we will pass a LinkedList as the "value" argument
    '''
    def append(self, value):
        
        # If LinkedList is empty
        if self.head is None:
            self.head = Node(value)
            return
        
        # Create a temporary Node object
        node = self.head
        
        # Iterate till the end of the currrent LinkedList
        while node.next is not None:
            node = node.next
        
        # Append the newly creataed Node at the end of the currrent LinkedList
        node.next = Node(value)

        
    '''We will need this function to convert a LinkedList object into a Python list of integers'''
    def to_list(self):
        out = []          # <-- Declare a Python list
        node = self.head  # <-- Create a temporary Node object
        
        while node:       # <-- Iterate untill we have nodes available
            out.append(int(str(node.value))) # <-- node.value is actually of type Node, therefore convert it into int before appending to the Python list
            node = node.next
        
        return out
    
def merge(list1, list2):
    out_1= None
    out_2=LinkedList()
    merged_list = LinkedList(None)
    if list1 is not None and list2 is not None:
        out_1= LinkedList.to_list(list1)
        out_2=LinkedList.to_list(list2)
    if list1 is not None:
        out_1.extend(out_2)
    else:
        merged_list = out_2
    # print(type(out_1[0]))
    # print(sorted(out_1))
    
    for item in sorted(out_1):
        merged_list.append(item)
    
    return merged_list

class NestedLinkedList(LinkedList):
    def flatten(self):
        # TODO: Implement this method to flatten the linked list in ascending sorted order.
        node = LinkedList.head
        out=[]
        if node is None:
            return
        while node.next is None:
            new_linked_list = LinkedList()
            new_linked_list = node.value
            new_node= new_linked_list.head
            while new_node.next is not None:
                out.append(int(str(new_node.value)))
                new_node=new_node.next
            node=node.next
        
        print(out)
                
        
        
    
    
    
    
# head=Node(10)    
# list1= LinkedList(head)
# list1.append(5)
# list1.append(3)
# list1.append(4)

# head=Node(15)
# list2= LinkedList(head)
# list2.append(7)
# list2.append(8)
# list2.append(1)

# merge(list1, list2)


# ''' Create a simple LinkedList'''
# linked_list = LinkedList(Node(1)) # <-- Notice that we are passing a Node made up of an integer
# linked_list.append(3) # <-- Notice that we are passing a numerical value as an argument in the append() function here 
# linked_list.append(5)

# ''' Create another simple LinkedList'''
# second_linked_list = LinkedList(Node(2))
# second_linked_list.append(4)

# ''' Create a NESTED LinkedList, where each node will be a simple LinkedList in itself'''
# nested_linked_list = NestedLinkedList(Node(linked_list)) # <-- Notice that we are passing a Node made up of a simple LinkedList object
# nested_linked_list.append(second_linked_list) # <-- Notice that we are passing a LinkedList object in the append() function here
 
''' Test merge() function'''
linked_list = LinkedList(Node(1))
linked_list.append(3)
linked_list.append(5)

second_linked_list = LinkedList(Node(2))
second_linked_list.append(4)

# merged = merge(linked_list, second_linked_list)
# node = merged.head
# while node is not None:
#     #This will print 1 2 3 4 5
#     print(node.value)
#     node = node.next
    
# Lets make sure it works with a None list
merged = merge(None, linked_list)
node = merged.head
while node is not None:
    #This will print 1 3 5
    print(node.value)
    node = node.next   
    
    
    