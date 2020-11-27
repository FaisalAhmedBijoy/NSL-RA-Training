'''
In a loop 
total exection time is O(n)
always sum is : 1035
'''
def myAlgo(n):
    sum=0
    for i in range(n):
        sum=sum+i
        if sum>=1000:
            break
    return sum
print(myAlgo(1000))
