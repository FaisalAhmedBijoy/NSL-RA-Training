# -*- coding: utf-8 -*-
"""
Created on Thu Dec 10 22:25:20 
@author: Faisal 
Numbers:  [1, 3, 5, 7, 9]
Numbers:  [3, 5, 7, 9]
Numbers:  [5, 7, 9]
Numbers:  [7, 9]
Numbers:  [9]
25
25
"""
def listsum(numbers):
    print("Numbers: ",(numbers))
    if len(numbers) ==1:
        return numbers[0]
    else:
        return numbers[0] + listsum(numbers[1:])
print(listsum([1,3,5,7,9]))

