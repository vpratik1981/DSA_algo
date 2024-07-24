#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 20 13:42:32 2024

@author: gq06
"""

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        # self.tail =None

    def to_list(self):
        out = []
        node = self.head
        while node:
            out.append(node.value)
            node = node.next
        return out
    
    def prepend(self,value):
        if self.head is None:
            self.head=Node(value)
            # self.tail=self.head
            return
        else:
            new_head=Node(value)
            new_head.next=self.head
            self.head=new_head
            # self.tail=self.head.next
            return
    def append(self,value):
        if self.head is None:
            self.head=Node(value)
            return
        else:
            node=self.head
            while node.next is not None:
                node=node.next
            node.next=Node(value)
            return
    def search(self, value):
        if self.head is None:
            return 'The list is empty'
        else:
            node=self.head
            while node.next is not None:
                if node.value==value:
                    print(node.value)
                    return node
                node=node.next
        raise ValueError("Value not found in the list.")
        
    def remove(self,value):
        if self.head is None:
            return None
        # if self.head.value==value:
        #     self.head=self.head.next
        #     return
        node=self.head
        while node.next is not None:
            if node.next.value==value:
                node.next=node.next.next
                return
            node=node.next


    def pop(self):
        if self.head is  None:
            return None
        node = self.head
        self.head= node.next
        return node.value
    
    def insert(self,value,pos):

        if self.head is None:
            return None
        # If new node to be appeneded at the start
        if pos==0:
            new_head = Node(value)
            new_head.next =self.head
            self.head=new_head
            return
                

        node = self.head
        count=0
        while node is not None:
            # Insert at any position less than the size of the list
            if count+1==pos:
                new_node=Node(value)
                new_node.next=node.next
                node.next=new_node
                return
            # If Pos is greater than length of list
            if pos == count-1:
                new_node= Node(value)
                # 0->1->2->3
                new_node.next=node.next
                node.next=new_node
                return
            count+=1
            node=node.next


        
        


obj_linkedList = LinkedList()
obj_linkedList.prepend(1)
obj_linkedList.prepend(3)
obj_linkedList.prepend(5)

obj_linkedList.append(4)
obj_linkedList.append(2)
assert obj_linkedList.to_list() == [5, 3, 1, 4, 2], f"list contents: {obj_linkedList.to_list()}"
print(obj_linkedList.to_list())

obj_linkedList.insert(9,1)

# obj_linkedList.search(3)
# obj_linkedList.remove(3)

# print(obj_linkedList.pop())
print(obj_linkedList.to_list())
