import numpy as np
np.set_printoptions(legacy='1.13')
n,m=map(int,input().split())
array=np.array([input().split() for _ in range(n)],int)
#print(array)
print(np.mean(array,axis=1))
print(np.var(array,axis=0))
print(np.std(array))