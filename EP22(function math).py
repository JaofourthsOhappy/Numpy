import numpy as np

a = np.array([1,45,23,77,4,32,56])

print(a.sum())
# 238

print(a.prod())
# 571253760

print(a.mean())
# 34.0

print(a.max())
# 77

print(a.min())
# 1

print(a.argmax())
# 3

print(a.argmin())
# 0

b = np.array([[10,20,30],[40,50,90],[80,100,5]])
print(b)
# [[ 10  20  30]
#  [ 40  50  90]
#  [ 80 100   5]]

print(np.min(b,axis=1))
# [10 40  5]

print(np.min(b,axis=0))
# [10 20  5]

print(np.max(b,axis=1))
# [ 30  90 100]


print(np.max(b,axis=0))
# [ 80 100  90]