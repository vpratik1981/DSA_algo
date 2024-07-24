#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 17 19:06:32 2024

@author: gq06
"""

def word_flipper(our_string):

    """
    Flip the individual words in a sentence

    Args:
       our_string(string): String with words to flip
    Returns:
       string: String with words flipped
    """
    our_string_reversed=our_string.split(' ')
    length =len(our_string_reversed)
    count=0
    
    
    result=''
    for item in our_string_reversed:
        result+=item[::-1]
        if length==1:
            return result
        if count <length-1:
            result+=' '
        count+=1

        
    
    # print(result)
    return result
        
    
    
    # TODO: Write your solution here
    
    
    
    
# word_flipper('This is an example')
print ("Pass" if ('retaw' == word_flipper('water')) else "Fail")
print ("Pass" if ('sihT si na elpmaxe' == word_flipper('This is an example')) else "Fail")
print ("Pass" if ('sihT si eno llams pets rof ...' == word_flipper('This is one small step for ...')) else "Fail")