# -*- coding: utf-8 -*-
"""
Created on Sat Oct  3 09:50:19 2020

@author: Shimul
"""

n=input()
n=int(n)
if n%2==0:
    if n>=2 and n<=5:
        print('Not Weird')
    elif n>=6 and n<20:
        print('Weird')
    elif n>=20:
        print('Not Weird')
else:
    print('Weird')

    