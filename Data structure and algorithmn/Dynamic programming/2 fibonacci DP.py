# -*- coding: utf-8 -*-
"""
f(n)=f(n-1)+f(n-2)
DP is used to store the values of recusion returns
[None, None, None, None, None, None, None, None, None, None]
Calling n: 8
Calling n: 7
Calling n: 6
Calling n: 5
Calling n: 4
Calling n: 3
Calling n: 2
21
"""
memory=[None]*10
print(memory)
def fibo(n):
    if n==0:
        return 0
    if n==1:
        return 1
    if memory[n] != None:
        return memory[n]
    print("Calling n:",n)
    memory[n]=fibo(n-1)+fibo(n-2)
    return memory[n]
    
print(fibo(8))

