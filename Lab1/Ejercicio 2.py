def ec_rec(n,m):
    if n > m and m > 0:
        print(((n-1)+(n-1),(m)+(m-1)))
    elif m == n:
        print(1)
    elif m == 0:
        print(1)

ec_rec(20,20)
ec_rec(15,0)
ec_rec(50,35)
ec_rec(100,85)
