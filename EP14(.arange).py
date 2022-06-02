import numpy as np

# np.arange(start,stop,step,dtype)

a = np.arange(10)
print(a)
# [0 1 2 3 4 5 6 7 8 9]

b = np.arange(10.0)
print(b)
# [0. 1. 2. 3. 4. 5. 6. 7. 8. 9.]

c =np.arange(3,10)
print(c)
# [3 4 5 6 7 8 9]

d = np.arange(-5,2)
print(d)
# [-5 -4 -3 -2 -1  0  1]

e = np.arange(4,11,dtype=float)
print(e)
# [ 4.  5.  6.  7.  8.  9. 10.]

f = np.arange(4,11,dtype=complex)
print(f)
# [ 4.+0.j  5.+0.j  6.+0.j  7.+0.j  8.+0.j  9.+0.j 10.+0.j]

g = np.arange(1,11,2)
print(g)
# [1 3 5 7 9]