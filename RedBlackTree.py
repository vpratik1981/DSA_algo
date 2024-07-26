#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 23 21:38:54 2024

@author: gq06
"""

class Node:
    def __init__(self,value,parent,color):
        self.value = value
        self.left = None
        self.right = None
        self.parent = parent
        self.color = color
        
class RedBlackTree:
    def __init__(self,root):
        self.root = Node(root,None,'red')
        
    def insert(self,new_val):
        self.insert_helper(self.root,new_val)
    
    def insert_helper(self,current,new_val):
        if current.value < new_val :
            if current.right:
                self.insert_helper(current, new_val)
            else:
                self.current.right = Node(new_val, self.curent,'red')
        else:
            if current.left:
                self.insert_helper(current.left, new_val)
            else:
                self.curent.left = Node(new_val, current, 'red')
                
    def search(self,find_val):
        pass