# -*- coding: utf-8 -*-
"""
Created on Mon Sep 26 18:07:12 2016

@author: AshrafAy
"""

# Paste your code into this box 
string=""
s = 'kzbatsozhhrrxamjtmmh'
temp=0
count=0
length=0
flag=0
for i in range(len(s)):
    if i<len(s)-1:
        if s[i]<=s[i+1]:
            count+=1
            flag+=1
            continue
    if count>temp:
        temp=count
        string=s[i-temp:i+1]
        count=0
    else:
        count=0
if temp==0 and flag==0:
    string=s[0]
print("Longest substring in alphabetical order is :",string)

#ORIGINAL SUBMITTED CODE

"""
string=""
temp=0
count=0
length=0
flag=0
for i in range(len(s)):
 if i<len(s)-1:
  if s[i]<=s[i+1]:
   count+=1
   flag+=1
   continue
 if count>temp:
  length=count
  temp=count
  string=s[i-length:i+1]
  count=0
 else:
   temp=temp
   count=0
if temp==0 and flag==0:
 string=s[0]
print("Longest substring in alphabetical order is :",string)
"""

'''
str_list=['namexjacvomne','pxvtcmspqtwqqarlr','yksojcfejsyefiaxrjuvci','ikrpemkuryxvsfihdae',\
'bkvxxzoa','ndjreivzdbhlflux','popjawgq','abcdefghijklmnopqrstuvwxyz','zotrvlyfshldu','zotrvlyfshldu',\
'ggczinldwldvdijqafjimuor','zyxwvutsrqponmlkjihgfedcba','gxdtooxdyosxsguxmfqf',\
'jxzzhcdyvas','tnfdgvusugyo','rcodytraodywrqjrziks','dfjwzvjtcemfbwqmzhtrxzt',\
'iagfzbkfbjx','vzqdnwxwoygklkxgumwmgvux','kzbatsozhhrrxamjtmmh']
for s in str_list:
    print("Longest substring in alphabetical order in \'"+s+"\' is :",string)
'''
