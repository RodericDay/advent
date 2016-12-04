lim = 36000000

def gift_sieve(n):
    sieve = [0 for _ in range(n)]
    for x in range(1,n):
        for i, y in enumerate(range(x,n,x)):
            if i == 50: break
            sieve[y] += x*11
            if sieve[y] > lim:
                return y

print(gift_sieve(1000000))
