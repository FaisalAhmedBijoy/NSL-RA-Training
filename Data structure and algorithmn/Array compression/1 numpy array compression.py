import numpy as np
a=np.array([[1,2],[3,4],[5,6]])
print(a)
print(a.flatten())
print(np.compress([0,1],a,axis=0))
print(np.compress([False,True],a,axis=1))