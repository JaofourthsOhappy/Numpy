import numpy as np

a = np.array([[1,2],[3,4],[5,6]])
print(a)
# [[1 2]
#  [3 4]
#  [5 6]]

print(a[0][1])
# 2


a[0][1] = 500 
print(a)
# [[  1 500]
#  [  3   4]
#  [  5   6]]