# -*- coding: utf-8 -*-
"""
Created on Mon Dec 14 11:16:12 2020

@author: Faisal

False
True
"""
def sequential_search(numbers,item):
    position=0
    found=False
    stop=False
    while position<len(numbers) and not found and not stop:
        if numbers[position] ==item:
            found =True
        else:
            if numbers[position]>item:
                stop=True
            else:
                position=position+1
    return found
        
numbers=[10,20,30,40,50,60,70,80,90,100]
item=31
print(sequential_search(numbers,item))


item=100
print(sequential_search(numbers,item))


