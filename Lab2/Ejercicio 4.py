import numpy as np 

A = np.array([[2,1], [1,1], [-1,2]])
A1 = np.array([4,3,3])
S1 = np.linalg.lstsq(A,A1)


B = np.array([[2,1], [1,1], [-1,2]])
B1 = np.array([3,2,1])
S2 = np.linalg.lstsq(B,B1)

C = np.array([[2,1], [1,1], [-1,2]])
C1 = np.array([6,4,2])
S3 = np.linalg.lstsq(C,C1)

D = np.array([[2, 1], [1, 1], [-1, 2]])
D1 = np.array([-3,-1,4])
S4 = np.linalg.lstsq(D,D1)

print("Respuesta 1: \n",S1,"\n","Respuesta 2: \n", S2,"\n","Respuesta 3: \n", S3,"\n", "Respuesta 4: \n",S4)