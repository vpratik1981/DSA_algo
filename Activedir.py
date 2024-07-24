#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  8 17:58:55 2024

@author: gq06
"""

class Group:
    def __init__(self,_name):
        self.name = _name
        self.users =[]
        self.groups=[]
    def addUser(self,user):
        self.users.append(user)
    def addGroups(self,group):
        self.groups.append(group)
    def getUser(self):
        return self.users
    def getGroups(self):
        return self.groups
    def getName(self):
        return self.name
  
def is_user_in_group(self, user,group):
    if user in group.getUser():
        return True
    else:
        if group.getGroups()==[]:
            return False
        else:
            for g in group.getGroups():
                return is_user_in_group(user, g)

parent = Group('parent')
child = Group('child')
sub_child = Group('sub_child')

sub_child_user ='sub_child_user'
sub_child.addUser(sub_child_user)

sub_child.addGroups(sub_child)
parent.addGroups(child)

print(parent.getGroups())


