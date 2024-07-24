#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 17 18:07:19 2024

@author: gq06
"""

def anagram_checker(str1, str2):

    """
    Check if the input strings are anagrams of each other

    Args:
       str1(string),str2(string): Strings to be checked
    Returns:
       bool: Indicates whether strings are anagrams
    """
    # print(str2.replace(' ',''))
    str1_repl=str1.replace(' ', '')
    str2_repl=str2.replace(' ', '')
    # print(str1_repl)
    # print(str2_repl)
    if len(str1_repl)!=len(str2_repl):
        return False
    elif sorted(str1_repl.lower())!=sorted(str2_repl.lower()):
        return False
    
    return True

print ("Pass" if not (anagram_checker('water','waiter')) else "Fail")
print ("Pass" if anagram_checker('Dormitory','Dirty room') else "Fail")
print ("Pass" if anagram_checker('Slot machines', 'Cash lost in me') else "Fail")
print ("Pass" if not (anagram_checker('A gentleman','Elegant men')) else "Fail")
print ("Pass" if anagram_checker('Time and tide wait for no man','Notified madman into water') else "Fail")
    