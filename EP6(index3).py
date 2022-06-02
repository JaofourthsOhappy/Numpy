import numpy as np

a = np.array([[[1,2,3],[4,5,6]]])
print(a.ndim)
# 3

# print(a[dept][row[column])
print(a[0][1][1])
# 5

b = np.array([[[1,2,3],[4,5,6],[7,8,9],[10,11,12]]])
print(b)
# [[[ 1  2  3]
#   [ 4  5  6]
#   [ 7  8  9]
#   [10 11 12]]]

print(b[0][1][0])
# 4