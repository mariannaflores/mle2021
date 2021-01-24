from time import process_time 

def primos(n):
    primes = [False, False] + [True] * (n - 1)
    p = [2]
    for j in range(4, n + 1, 2):
        primes[j] = False
    for i in range(3, n + 1, 2):
        if primes[i]:
            p.append(i)
            for j in range(i * i, n + 1, i):
                primes[j] = False
    print(p)

t1_start = process_time()
print(primos(100000))
t1_stop = process_time()
print('Tiempo: ', t1_stop-t1_start)