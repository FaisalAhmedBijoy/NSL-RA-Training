import numpy as np
dimension=input().strip().split(" ")
dimension=np.int32(dimension)
#print(dimension)
print(np.zeros(dimension,dtype=np.int32))
print(np.ones(dimension,dtype=np.int32))