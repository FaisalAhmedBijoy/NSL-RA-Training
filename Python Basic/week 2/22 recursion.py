'''
if a function has required similiar type of operation 
then recursion is used to do this task efficiently

Example: factorial 5! = 5x4x3x2x1
recursion has some rules
1. Base case to terminate the program
2. function by itself

'''

def factorial(n):
    if n==1:
        return 1
    else:
        return n * factorial(n-1)
print(factorial(5))
'''
if there is two function : Even(), Odd()
then even(),odd(),even(),odd()..... is possible to call
'''
def is_even(x):
    if x==0:
        return True
    else:
        return is_odd(x-1)
def is_odd(x):
    return not is_even(x)

print(is_odd(17))
print(is_even(23))

print(is_even(10))
print(is_odd(9))
