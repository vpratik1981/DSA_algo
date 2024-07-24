#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 20 13:01:42 2024

@author: gq06
"""

class DoubleNode:
    def __init__(self,value):
        self.value = value
        self.next=None
        self.previous= None

class DoublyLinkedList:
    def __init__(self):
        self.head= None
        self.tail = None
        
    def append(self, value):
        if self.head is None:
            self.head = DoubleNode(value)
            self.tail = self.head
            return
        else:
            self.tail.next=DoubleNode(value)
            self.tail.next.previous = self.tail
            self.tail = self.tail.next
            return
            
        
    