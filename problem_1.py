#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul  5 19:10:36 2024

@author: gq06
"""
from collections import OrderedDict

class LRU_Cache(object):
    def __init__(self,capacity=5):
        self.capacity = capacity
        self.cache = OrderedDict()
        
    def get(self,key):
        
        try:
        
            hash_value = self.cache.pop(key)
            self.cache[key] = hash_value
            return hash_value
        except KeyError :
            return -1
    
    def set(self,key,value):
        
        if self.get(key) == -1  and len(self.cache) >= self.capacity:
            self.cache.popitem(last= False)
        self.cache[key] = value
        
our_cache = LRU_Cache(5)

our_cache.set(1, 1)
our_cache.set(2, 2)
our_cache.set(3, 3)
our_cache.set(4, 4)
our_cache.set(5, 5)
our_cache.set(6,6)

print(our_cache.get(1))

            
        
        
        
