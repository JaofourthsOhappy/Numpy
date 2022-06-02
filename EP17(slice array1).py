import numpy as np

# x = [start,stop,step]

a = np.arange(1,11)
print(a)
# [ 1  2  3  4  5  6  7  8  9 10]

print(a[:])
# [ 1  2  3  4  5  6  7  8  9 10]

print(a[3:])
# [ 4  5  6  7  8  9 10]

print(a[:5])
# [1 2 3 4 5]

print(a[2:9:2])
# [3 5 7 9]

print(a[::3])
# [ 1  4  7 10]