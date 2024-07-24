#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 21:48:29 2024

@author: gq06
"""

class Node:
    def __init__(self,value):
        self.value=value
        self.next=None

class Queue:
    def __init__(self):
        self.head=None
        self.tail = None
        self.num_elements=0
        
    def enqueue(self,value):
        new_node=Node(value)
        if self.head is None:
            self.head=new_node
            self.tail=self.head
            self.num_elements+=1
            return
        # tmp_node=None
        # count=1
        tmp_node= self.tail
        self.tail=new_node
        tmp_node.next=self.tail
        self.num_elements+=1
        
        current = self.head
        
        while current is not None:
            print(current.value)
               
            current=current.next
        
        
        # self.num_elements+=1
    
    def size(self):
        return self.num_elements
    
    def dequeue(self):
        if self.num_elements==0:
            return None
        current=self.head
        
        element_front = current.value
        self.head=current.next
        
        while current.next is not None:
            current=current.next
        self.tail=current
        current.next=None
        self.num_elements-=1
        # print(self.num_elements)
        # print(element_front)
        
        return element_front
            
    

q=Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
# q.dequeue()


print('pass' if q.size()==3  else 'fail')
print('pass' if q.dequeue()==1 else 'fail')
q.enqueue(4)
print ("Pass" if (q.dequeue() == 2) else "Fail")
        