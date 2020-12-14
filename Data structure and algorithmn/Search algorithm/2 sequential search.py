# -*- coding: utf-8 -*-
"""
Created on Mon Dec 14 11:01:55 2020

@author: Faisal

Sequential seacrh random
item found
Item 31: position is :5 
Not found
Item 100: position is :-1 

Best case: O(1)
Wrost case: O(n)
Avg case: O(n/2) 
"""
def sequential_search(numbers,item):
    position=-1
    
    for i in range (len(numbers)):
        if numbers[i] ==item:
            position=i
    if position !=-1:
        print("item found")
    else:
        print("Not found")
    return position
numbers=[54,26,93,17,77,31,44,55,20,65]
item=31
position=sequential_search(numbers,item)
print("Item %d: position is :%d "%(item,position))

item=100
position=sequential_search(numbers,item)
print("Item %d: position is :%d "%(item,position))

