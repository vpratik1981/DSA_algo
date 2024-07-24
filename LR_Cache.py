#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 16 17:49:16 2024

@author: gq06
"""

import collections

class LRU_Cache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = collections.OrderedDict()
    
    def get(self,key):
        if key in self.cache.keys():
            return self.cache[key]
        else:
            return -1

        
        
    def put(self,key,value):
        if key not in self.cache and self.size() < 5:
            self.cache[key] = value
            
        if key in self.cache and self.size() < 5:
            self.cache[key] = value
        
        if key not in self.cache and self.size() ==5:
            self.cache.popitem(0)
            self.cache[key]=value
    def size(self):
        return len(self.cache)
    
    def get_keys(self):
        return self.cache.keys()


lru_cache = LRU_Cache(5)
lru_cache.put(1,1)
lru_cache.put(2,2)
lru_cache.put(3,3)
lru_cache.put(4,4)
lru_cache.put(5,5)
# lru_cache.put(6,6)


print(lru_cache.get_keys())
            