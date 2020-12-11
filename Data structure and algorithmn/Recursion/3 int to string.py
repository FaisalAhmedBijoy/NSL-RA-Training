# -*- coding: utf-8 -*-
"""
Created on Fri Dec 11 18:48:03 2020

@author: Faisal
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
BIN:  1110011000011
7363
460
28
1
HEXA:  1CC3
"""
def toStr(number,base):
    convertString='0123456789ABCDE'
    print(number)
    if number<base:
        return convertString[number]
    else:
        return toStr(number//base,base) +convertString[number%base]
print("BIN: ",toStr(7363,2))
print("HEXA: ",toStr(7363,16))

