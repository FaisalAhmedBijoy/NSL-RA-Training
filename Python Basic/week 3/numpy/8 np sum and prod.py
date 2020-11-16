import numpy as np
n,m=map(int,input().split())
matrix=np.array([input().split() for _ in range(n)],int)
#print(matrix)
sum_val=np.sum(matrix, axis=0) 
#print(sum_val)
print(np.prod(sum_val))
