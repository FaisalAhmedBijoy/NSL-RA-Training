# -*- coding: utf-8 -*-
"""
Created on Fri Dec 11 19:01:29 2020

@author: Faisal
faisal
aisal
isal
sal
al
l

lasiaf
"""

def Reverse(name):
    print(name)
    if len(name)==0:
        return name
    else:
        return Reverse(name[1:])+name[0]
        
print(Reverse("faisal"))

