# -*- coding: utf-8 -*-
"""
Created on Mon Dec 14 11:36:05 2020

@author: Faisal

Complexity: O(log (n))
Mid :  50
Mid :  80
Mid :  90
item 90: True
Mid :  50
item 50:  True
Mid :  50
Mid :  20
item 20:  True
"""
def binarySearch(numbers,item):
    first=0
    last=len(numbers)-1
    found=False
    while first<last and not found:
        mid=(first+last)//2
        print("Mid : ",numbers[mid])
        if numbers[mid] ==item:
            found=True
        elif numbers[mid]>item:
            last=mid-1
        else:
            first=mid+1
    return found
numbers=[10,20,30,40,50,60,70,80,90,100]
item=90
print("item 90:",binarySearch(numbers,item))

item=50
print("item 50: ",binarySearch(numbers,item))

item=20
print("item 20: ",binarySearch(numbers,item))

