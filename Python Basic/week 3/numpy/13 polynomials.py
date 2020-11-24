import numpy as np
array1=list(map(float,input().split()))
point=float(input())
#print(array1)
print(np.polyval(array1,point))