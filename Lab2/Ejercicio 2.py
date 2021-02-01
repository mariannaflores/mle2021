import numpy as np 

E = np.zeros((2,3))
print("E = \n", repr(E))

D = np.eye(2)
print("D = \n", repr(D))

A = np.arange(5,9).reshape((2,2))
print("A = \n", repr(A))

B = np.arange(-7,-1).reshape(2,3)
print("B = \n", repr(B))

C = np.arange(4,14,3).reshape(2,2)
print("C = \n", repr(C))

h1 = (A,D,E)
h2 = (D,C,B)
H1 = np.hstack(h1)
H2 = np.hstack(h2)
h = (H1,H2)
H = np.vstack(h)
print("H = \n", repr(H))

