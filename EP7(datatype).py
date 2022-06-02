import numpy as np

a = np.array([1,2,3,4,5])
print(a.dtype)
# int64

b = np.array([1,2,3,4,5],dtype=float)
print(b)
# [1. 2. 3. 4. 5.]


c = np.array([1,2,3,4,5],dtype=complex)
print(c)
# [1.+0.j 2.+0.j 3.+0.j 4.+0.j 5.+0.j]n