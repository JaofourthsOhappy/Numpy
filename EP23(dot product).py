import numpy as np

a = np.array([[1,2],[3,4]])
b = np.array([[11,12],[13,14]])


print(a.dot(b))
# [[37 40]
#  [85 92]]

# [[1*11+2*13,1*12+2*14],[3*11+4*13,3*12+4*14]]