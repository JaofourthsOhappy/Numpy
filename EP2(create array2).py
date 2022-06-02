import numpy as np

a = np.array([[1,2,3],[4,5,6]])
print(a)
# [[1 2 3]
#  [4 5 6]]


print(a.ndim)
# 2

list = [[1,2,3],[4,5,6],[7,8,9]]
b = np.array(list)
print(b)
# [[1 2 3]
#  [4 5 6]
#  [7 8 9]]




tu = ((1,2,3),(4,5,6),(7,8,9))
c = np.array(tu)
print(c)
# [[1 2 3]
#  [4 5 6]
#  [7 8 9]]