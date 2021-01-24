from time import process_time 

def primos(n):

    is_prime = [False, False] + [True] * (n - 1)
    p = [2]
    for j in range(4, n + 1, 2):
        is_prime[j] = False
    for i in range(3, n + 1, 2):
        if is_prime[i]:
            p.append(i)
            for j in range(i * i, n + 1, i):
                is_prime[j] = False
    print(p)

t1_start = process_time()
print(primos(100000))
t1_stop = process_time()
print('Tiempo: ', t1_stop-t1_start)