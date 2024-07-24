#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 22 11:20:13 2024

@author: gq06
"""

# Use this class as the nodes in your linked list
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
    
    def __repr__(self):
        return str(self.value)

class SortedLinkedList:
    def __init__(self):
        self.head = None
        
    def append(self, value):
        """
        Append a value to the Linked List in ascending sorted order

        Args:
           value(int): Value to add to Linked List
        """
        
        # TODO: Write your sorted append function here
        if self.head is None:
            self.head = Node(value)
            return
        # node = self.head
        
        if value < self.head.value:
            # new_node= Node(value)
            temp= self.head.value
            self.head.value=value
            self.head.next=Node(temp)
            return
        node= self.head
        
        while node.next is not None and value>=node.next.value:
            node=node.next
            
        new_node = Node(value)
        temp = node.value
        node.value=temp
        node.next= new_node
        
        return None
    
def sort(array):
    """
    Given an array of integers, use SortedLinkedList to sort them and return a sorted array.

    Args:
       array(array): Array of integers to be sorted
    Returns:
       array: Return sorted array
    """
    
    # TODO: Write your sorting function here
    out=[]
    linked_list = SortedLinkedList()
    for item in array:
        linked_list.append(item)
        
    node=linked_list.head
    while node is not None:
        out.append(node.value)
        node = node.next
    return out
    # print(out)
            
            # print(node.value)
        
        
        

            
        
# # Test cases
# linked_list = SortedLinkedList()
# linked_list.append(3)
# print ("Pass" if (linked_list.head.value == 3) else "Fail")

# linked_list.append(2)
# print ("Pass" if (linked_list.head.value == 2) else "Fail")

# linked_list.append(4)


# node = linked_list.head.next.next
# print ("Pass" if (node.value == 4) else "Fail")

# linked_list1 = SortedLinkedList()

sort([5,1,4,3,2])
                
        
    