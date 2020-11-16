import numpy

def arrays(arr):
    # complete this function
    # use numpy.array
    arr=numpy.float32(arr)
    return numpy.flip((arr))

arr = input().strip().split(' ')
print(arrays(arr))

# 1 2 3 4 -8 -10