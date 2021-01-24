def rombo(n):

    m = round(n/2+0.5) 
    for i in range(m):
        print(' '*(m-i-1)+'* '*(i+1))
    
    for j in range(m-1,0,-1):
        print(' '*(m-j)+'* '*(j))
    
rombo(7)
rombo(9)
rombo(11)