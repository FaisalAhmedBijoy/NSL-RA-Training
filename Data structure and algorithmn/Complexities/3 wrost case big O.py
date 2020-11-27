'''
In the worst case 
total execution time is the complexity value
in this there are two for loop 
so complexity is : O(n2)
'''
def myAlgo(n):
    sum=0
    for i in range(n):
        for j in range(i):
            sum=sum+(i+j)
    return sum
print(myAlgo(10))
