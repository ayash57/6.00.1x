# -*- coding: utf-8 -*-
"""
Created on Mon Sep 26 18:52:44 2016

@author: AshrafAy
"""

string = input("Enter the string:")
count=0
#string='bob'
substring=input("Enter the substring to be found:")
limit=len(substring)
for i in range(len(string)):
    if string[i:i+limit]==substring:
       count=count+1
print("Number of times " +string+" occurs is:"+str(count))



#ORIGINAL CODE

"""
count=0
for i in range(len(s)):
    if s[i]=='b':
        if i<len(s)-2:
            if s[i+1]=='o':
                if s[i+2]=='b':  
                    count=count+1
print("Number of times bob occurs is:"+str(count))
"""