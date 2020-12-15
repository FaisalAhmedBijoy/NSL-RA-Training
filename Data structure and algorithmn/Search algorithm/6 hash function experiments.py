# -*- coding: utf-8 -*-
"""
Created on Tue Dec 15 16:19:35 2020

@author: Faisal
"""
def hash_function(name):
    sum=0
    for i in range(len(name)):
        sum=sum+ ord(name[i])
    print(sum)
    return sum%len(name)
name='cat' 
hash_value=hash_function(name)
print(hash_value)
