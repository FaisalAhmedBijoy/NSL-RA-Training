# -*- coding: utf-8 -*-
"""
Created on Tue Dec 15 13:06:12 2020

@author: Faisal
"""
def hash_function(number):
    hash_values=[]
    length=len(number)
    for i in number:
        hash_values.append(i%length)
    return hash_values
values=[113,117,97,100,114,108,116,105,99]
hash_values=hash_function(values)
print(hash_values)