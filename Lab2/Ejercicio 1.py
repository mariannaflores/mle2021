import numpy as np 

M = np.array([[1,1,0,0,0,0,1],[0,1,1,0,0,1,0],[0,0,1,1,0,0,0],[0,0,0,1,1,0,1],[1,0,0,0,0,1,1],[0,0,0,0,1,1,1],[1,1,1,0,0,0,1]])
M1 = np.array([[1,1,0,0,0,1,1],[1,1,1,0,1,0,0],[0,1,1,1,1,0,0],[0,0,1,1,0,0,1],[0,1,1,0,1,1,1],[1,0,0,0,1,1,1],[1,0,0,1,1,1,1]])
M2 = np.array([[1,1,0,0,0,0,0],[1,1,0,0,0,0,0],[0,0,1,1,0,0,0],[0,0,1,1,0,0,0],[0,0,0,0,1,1,1],[0,0,0,0,1,1,1],[0,0,0,0,1,1,1]])

Sr = np.diagonal(M).sum()== M.shape[0]
Ss = (np.transpose(M)==M).all()
p = M.dot(M)
St = (p!=1).all()

Sr1 = np.diagonal(M1).sum()== M1.shape[0]
Ss1 = (np.transpose(M1)==M1).all()
p1 = M1.dot(M1)
St1 = (p1!=1).all()

Sr2 = np.diagonal(M2).sum()== M2.shape[0]
Ss2 = (np.transpose(M2)==M2).all()
p2 = M2.dot(M2) 
St2 = (p2!=1).all()

print("M: \n", M, "\n", "Reflexibidad:", Sr,"\n", "Simetria:", Ss,"\n","Transitividad:", St,"\n")
print("M1: \n", M1, "\n", "Reflexibidad:", Sr1,"\n", "Simetria:", Ss1,"\n","Transitividad:", St1,"\n")
print("M2: \n", M2, "\n", "Reflexibidad:", Sr2,"\n", "Simetria:", Ss2,"\n","Transitividad:", St2,"\n")

print(p,p1,p2)