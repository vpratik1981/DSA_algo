#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  5 22:31:45 2024

@author: gq06
"""

class Queue:
    def __init__(self,size=4):
        self.arr=[0 for _ in range(size)]
        self.next_index=0
        self.front_index=-1
        self.queue_size=0
    
    def enqueue(self,value):
        if self.queue_size == len(self.arr):
            self.arr=self.handle_queue_capacity_full()
        self.arr[self.next_index]= value
        self.queue_size+=1
        self.next_index= (self.next_index+1)%len(self.arr)
        if self.front_index == -1:
            self.front_index=0
        # else:
        #     self.front_index+=1
        
    
    def size(self):
        return self.queue_size
    
    def is_empty(self):
        return self.queue_size==0
    
    def front(self):
        if self.is_empty():
            return None
        return self.front_index
    
    def dequeue(self):
        if self.is_empty():
            self.front_index=-1
            self.next_index=0
            return None
        item = self.arr[self.front_index]
        self.front_index=(self.front_index+1)%len(self.arr)
        self.queue_size-=1
        # print(item)
        return item
    def front(self):
        if self.is_empty():
            return None
        return self.arr[self.front_index]
    
    def handle_queue_capacity_full(self):
        # if self.queue_size==len(self.arr):
        old_arr = self.arr
        self.arr= [0 for _ in range(len(self.arr)*2)]
        index=0
        for i in range(self.front_index,len(old_arr)):
            self.arr[index]=old_arr[i]
            index+=1
        for i in range(0,self.front_index):
            self.arr[index]=old_arr[i]
            index+=1
        self.front_index=0
        self.next_index=index
        return self.arr
        
            



# Setup
q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
q.dequeue()
q.dequeue()
q.enqueue(5)
q.enqueue(6)
q.enqueue(7)
# q.enqueue(5)

# Test size
# print ("Pass" if (q.size() == 3) else "Fail")

# # Test dequeue
# print ("Pass" if (q.dequeue() == 1) else "Fail")   

# # Test enqueue
# q.enqueue(4)
# print ("Pass" if (q.dequeue() == 2) else "Fail")
# print ("Pass" if (q.dequeue() == 3) else "Fail")
# print ("Pass" if (q.dequeue() == 4) else "Fail")
# q.enqueue(5)
# print ("Pass" if (q.size() == 1) else "Fail")     