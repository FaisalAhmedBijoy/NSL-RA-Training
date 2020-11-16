import numpy as np
arr = input().strip().split(' ')
np_arr=np.array(arr)
np_arr=np.int32(np_arr)
print(np.reshape(np_arr,(3,3)))