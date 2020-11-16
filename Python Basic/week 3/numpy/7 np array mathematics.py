import numpy as np
n,m=map(int,input().split())
array1=[input().strip().split(" ") for _ in range(n)]
array2=[input().strip().split(" ") for _ in range(n)]
array1=np.int32(array1)
array2=np.int32(array2)
#print(array1)
#print(array2)

print(np.add(array1,array2))
print(np.subtract(array1,array2))
print(np.multiply(array1,array2))
print(array1//array2)
print(np.mod(array1,array2))
print(np.power(array1,array2))
