import numpy as np

a = np.array([3,4,2,6])
b = np.array([8,6,5,10])


print(np.concatenate((a,b)))
# [ 3  4  2  6  8  6  5 10]


c = np.array([[1,2],[3,4]])

print(np.append(c,[[10],[20]],axis=1))
# [[ 1  2 10]
#  [ 3  4 20]]