import numpy as np

a = np.arange(1,21)

b = a.reshape(5,4)

print(np.split(a,4))
# [array([1, 2, 3, 4, 5]), array([ 6,  7,  8,  9, 10]), array([11, 12, 13, 14, 15]), array([16, 17, 18, 19, 20])]

print(np.hsplit(a,4)) 
# [array([1, 2, 3, 4, 5]), array([ 6,  7,  8,  9, 10]), array([11, 12, 13, 14, 15]), array([16, 17, 18, 19, 20])]

print(np.vsplit(b,5))
# [array([[1, 2, 3, 4]]), array([[5, 6, 7, 8]]), array([[ 9, 10, 11, 12]]), array([[13, 14, 15, 16]]), array([[17, 18, 19, 20]])]