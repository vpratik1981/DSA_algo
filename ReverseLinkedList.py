#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 21 10:03:13 2024

@author: gq06
"""

# Helper Code

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        
    def append(self, value):
        if self.head is None:
            self.head = Node(value)
            return
        
        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)
        
    def __iter__(self):
        node = self.head
        while node:
            yield node.value
            node = node.next
            
    def __repr__(self):
        return str([v for v in self])
    
    def reverse(self,linkedList):
        new_list= LinkedList()
        out=[]
        
        for item in linkedList.__iter__():
            out.append(item)
        for item in out[::-1]:
            new_list.append(item)
        return new_list
            
        

obj_linkedList = LinkedList()
obj_linkedList.append(1)
obj_linkedList.append(3)
obj_linkedList.append(5)

obj_linkedList.append(4)
obj_linkedList.append(2)
obj_linkedList.reverse(obj_linkedList)
# assert obj_linkedList.to_list() == [5, 3, 1, 4, 2], f"list contents: {obj_linkedList.to_list()}"
print(obj_linkedList.__repr__())
new_list = obj_linkedList.reverse(obj_linkedList)

print(new_list.__repr__())

# print([item for item in obj_linkedList.__iter__()])

        