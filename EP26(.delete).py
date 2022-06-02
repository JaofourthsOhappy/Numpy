import numpy as np

a = np.arange(1,11)
print(a)
# [ 1  2  3  4  5  6  7  8  9 10]

print(np.delete(a,2))
# [ 1  2  4  5  6  7  8  9 10]

b = np.arange(1,13).reshape(4,3)
print(b)
# [[ 1  2  3]
#  [ 4  5  6]
#  [ 7  8  9]
#  [10 11 12]]

print(np.delete(b,2,axis=0))
# [[ 1  2  3]
#  [ 4  5  6]
#  [10 11 12]]

print(np.delete(b,1,axis=1))
# [[ 1  3]
#  [ 4  6]
#  [ 7  9]
#  [10 12]]