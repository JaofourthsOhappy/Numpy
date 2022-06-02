import numpy as np

# x = [start,end,step,start,end,step]

a = np.array([[1,2,3],[4,5,6],[7,8,9]])

print(a[:,:])
# [[1 2 3]
#  [4 5 6]
#  [7 8 9]]

print(a[1:,1:])
# [[5 6]
#  [8 9]]

print(a[2:,1:])
# [[8 9]]

print(a[:,2:])
# [[3]
#  [6]
#  [9]]

print(a[1:,:])
# [[4 5 6]
#  [7 8 9]]

print(a[:2,:2])
# [[1 2]
#  [4 5]]

print(a[::2,:])
# [[1 2 3]
#  [7 8 9]]

print(a[::,::2])
# [[1 3]
#  [4 6]
#  [7 9]]