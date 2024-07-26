#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 26 07:17:29 2024

@author: gq06
"""

def bubble_sort(l):
    for external_index in range(len(l)):
        for internal_index in range(1,len(l)):
            this = l[internal_index]
            prev = l[internal_index-1]
            if prev > this :
                l[internal_index] = prev
                l[internal_index-1] = this
    return l


# print(bubble_sort([16,49,3,12,56,49,55,22,13,46,19,55,46,13,25,56,9,48,45]))

sleep_times = [(24,13), (21,55), (23,20), (22,5), (24,23), (21,58), (24,3)]

# print(bubble_sort([7,8,6,1]))

def bubble_sort_1(l):
    for iteration in range(len(l)):
        for index in range(1,len(l)):
            this= l[index]
            prev = l[index-1]
            # print(this[0])
            if this[0] < prev[0] or (this[0]== prev[0] and this[1]<prev[1]):
                    l[index] = prev
                    l[index-1] = this
            # elif this[0] < prev[0]:
            #     l[index] = prev
            #     l[index-1] = this
    return l
                
                
            
            
print(bubble_sort_1(sleep_times))