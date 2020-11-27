
# Factorial of a number by recursion
def algo(n):
    if n==1:
        return 1
    return n* algo(n-1)
print(algo(5))