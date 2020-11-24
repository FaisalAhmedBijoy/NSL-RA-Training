import numpy as np
n,m=map(int,input().split())
array=np.array([input().split() for _ in range(n)],int)
print(np.max(np.min(array,axis=1)))