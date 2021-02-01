import numpy as np

ar = np.arange(0,24).reshape(4,6)
print(ar)

def rota90(matriz):
    t = np.transpose(matriz)
    print("Rota90: \n", np.flip(t,0))

def rota180(matriz):
    print("Rota180: \n", np.flip(ar))

def rota270(matriz):
    t = np.transpose(matriz)
    print("Rota270: \n", np.flip(t,1))

def rota90_otro_lado(matriz):
    t = np.transpose(matriz)
    print("Rota90 otro lado: \n", np.flip(t,1))

def rota180_otro_lado(matriz):
    print("Rota180 otro lado: \n", np.flip(ar))

def rota270_otro_lado(matriz):
    t = np.transpose(matriz)
    print("Rota270 otro lado: \n", np.flip(t,0))
    
rota90(ar)
rota180(ar)
rota270(ar)
rota90_otro_lado(ar)
rota180_otro_lado(ar)
rota270_otro_lado(ar)

#adicionalmente logrado por:
'''''
def rota90(matriz):
    print(repr(np.rot90(matriz)))

def rota180(matriz):
    print(repr(np.rot90(matriz, 2)))

def rota270(matriz):
    print(repr(np.rot90(matriz, 3)))

def rota90_otro_lado(matriz):
    print(repr(np.rot90(matriz, 1, axes=(1,0))))

def rota180_otro_lado(matriz):
    print(repr(np.rot90(matriz, 2, axes=(1,0))))

def rota270_otro_lado(matriz):
    print(repr(np.rot90(matriz, 3, axes=(1,0))))'''''