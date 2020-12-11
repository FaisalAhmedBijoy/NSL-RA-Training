# -*- coding: utf-8 -*-
"""
Created on Fri Dec 11 21:09:43 2020
@author: Faisal

using stack to store the remainder of number%base 
Reloaded modules: data_structure
7363
736
73
7
DEC 7363
7363
3681
1840
920
460
230
115
57
28
14
7
3
1
BIN 1110011000011
"""
from data_structure import Stack
def toStr(number,base):
    s=Stack()
    while number>0:
        remainder=number%base
        result=""
        print(number)
        if number<base:
            s.push(remainder)
            while not s.isEmpty():
                result=result+str(s.pop())
            return result
        else:
            s.push(remainder)
        number=number//base
        
print("DEC",toStr(7363,10))
print("BIN",toStr(7363,2))