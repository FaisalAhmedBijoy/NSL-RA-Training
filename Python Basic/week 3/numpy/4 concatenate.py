import numpy as np
n,m,p=map(int,input().split())
array1=np.array([input().strip().split() for _ in range(n)],int)
array2=np.array([input().strip().split() for _ in range(m)],int)
print(np.concatenate((array1,array2),axis=0))