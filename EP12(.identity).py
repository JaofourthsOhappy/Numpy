import numpy as np

a = np.identity(4)
print(a)
# [[1. 0. 0. 0.]
#  [0. 1. 0. 0.]
#  [0. 0. 1. 0.]
#  [0. 0. 0. 1.]]

b = np.identity(5,dtype=int)
print(b)
# [[1 0 0 0 0]
#  [0 1 0 0 0]
#  [0 0 1 0 0]
#  [0 0 0 1 0]
#  [0 0 0 0 1]]

c = np.eye(5)
print(c)
# [[1. 0. 0. 0. 0.]
#  [0. 1. 0. 0. 0.]
#  [0. 0. 1. 0. 0.]
#  [0. 0. 0. 1. 0.]
#  [0. 0. 0. 0. 1.]]

d = np.eye(5,k=1)
print(d)
# [[0. 1. 0. 0. 0.]
#  [0. 0. 1. 0. 0.]
#  [0. 0. 0. 1. 0.]
#  [0. 0. 0. 0. 1.]
#  [0. 0. 0. 0. 0.]]


e = np.eye(5,k=2)
print(e)
# [[0. 0. 1. 0. 0.]
#  [0. 0. 0. 1. 0.]
#  [0. 0. 0. 0. 1.]
#  [0. 0. 0. 0. 0.]
#  [0. 0. 0. 0. 0.]]


f = np.eye(5,k=-2)
print(f)
# [[0. 0. 0. 0. 0.]
#  [0. 0. 0. 0. 0.]
#  [1. 0. 0. 0. 0.]
#  [0. 1. 0. 0. 0.]
#  [0. 0. 1. 0. 0.]]