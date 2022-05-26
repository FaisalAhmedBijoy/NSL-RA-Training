"""
5
----
1
121
12321
1234321
123454321
"""



"""
for i in range(1,int(input())+1): #More than 2 lines will result in 0 score. Do not leave a blank line also
    for j in range(1,i):
        
        print(j,end='')
    for k in range(i,0,-1):
        print(k,end='')
    print('\n') 
"""
for i in range(1,int(input())+1): 
    print(((10**i)/9)**2)
