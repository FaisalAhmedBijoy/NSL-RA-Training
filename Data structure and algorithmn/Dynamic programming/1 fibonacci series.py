# -*- coding: utf-8 -*-
"""
f(n)=f(n-1)+f(n-2)
Calling n: 5
Calling n: 4
Calling n: 3
Calling n: 2
Calling n: 2
Calling n: 3
Calling n: 2
5

"""
def fibo(n):
    
    if n==0:
        return 0
    if n==1:
        return 1
    print("Calling n:",n)
    return fibo(n-1)+fibo(n-2)

print(fibo(5))
