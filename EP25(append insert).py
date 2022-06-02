
import numpy as np 
a = np.array([1,2,4,5,8])

print(np.append(a,40))
# [ 1  2  4  5  8 40]      last point


print(np.insert(a,1,100))
# [  1 100   2   4   5   8]     at point
