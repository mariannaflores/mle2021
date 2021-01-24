def triangulo_inv(n):
    for i in range(n,0,-1):
        for j in range(n-i):
            print(' ', end=' ') 
        for j in range(2*i-1):
            print('*',end=' ') 
        print()

triangulo_inv(4)
triangulo_inv(5)
triangulo_inv(6)
