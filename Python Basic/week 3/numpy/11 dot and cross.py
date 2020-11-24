import numpy as np
n=int(input())
array1=np.array([input().split() for _ in range(n)],int)
array2=np.array([input().split() for _ in range(n)],int)
print(np.dot(array1,array2))