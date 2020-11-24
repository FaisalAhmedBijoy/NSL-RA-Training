import numpy as np
array1=np.array(input().split(),int)
array2=np.array(input().split(),int)
print(np.inner(array1,array2))
print(np.outer(array1,array2))