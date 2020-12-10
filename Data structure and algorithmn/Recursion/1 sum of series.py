# -*- coding: utf-8 -*-
"""
total= (1+(3+(5+(7+9))))
total= (1+(3+(5+16)))
total= (1+(3+21))
total= (1+24)
total= 25

((((1+3)+5)+7)+9)
"""
def listsum(numlist):
    thesum=0
    for i in numlist:
        thesum+=i
    return thesum
print(listsum([1,3,5,7,9]))

