#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun  7 15:46:44 2024

@author: gq06
"""

class Stack:
    def __init__(self):
        self.items=[]
        
    def push(self,val):
        self.items.append(val)
    
    def pop(self):
        if len(self.items)==0:
            return None
        return self.items.pop()
    def getItems(self):
        return self.items
    def getSize(self):
        return len(self.items)
    

class Queue:
    def __init__(self):
        # Code here
        # self.head = -1
        # self.tail = -1
        # self.num_elements=0
        self.instorage=Stack()
        self.outStorage=Stack()
        
    def size(self):
         # Code here
         return self.instorage.getSize()+self.outStorage.getSize()
        
    def enqueue(self,item):
        # Code here
        # st = Stack()
        # st.push(item)
        # self.num_elements+=1
        # if self.head ==-1:
        #     self.head=0
        # if self.tail ==-1:
        #     self.tail=0
        # else:
        #     self.tail+=1
        # print(self.head)
        # print(self.tail)
        
        self.instorage.push(item)
        # print(self.instorage.items)
        
        
    def dequeue(self):
        # Code here
        if not self.outStorage.items:
            while self.instorage.items:
                self.outStorage.push(self.instorage.pop())
        print(self.outStorage.items)
        
# Setup
q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)

# Test size
print ("Pass" if (q.size() == 3) else "Fail")  
# Test dequeue
print ("Pass" if (q.dequeue() == 1) else "Fail")
      
        
        
        
        
        
        
        
        
        
        
        
        