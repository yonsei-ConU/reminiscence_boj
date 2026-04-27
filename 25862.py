import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


n, k = minput()
L = 1475070
sieve = [True] * L
sieve[0] = sieve[1] = False
for i in range(2, n + 1):
    if sieve[i]:
        for j in range(i, L, i):
            sieve[j] = False

primes = [True] * L
primes[0] = primes[1] = False
for i in range(2, L):
    if primes[i]:
        for j in range(2 * i, L, i):
            primes[j] = False

res = [i for i in range(L) if sieve[i] and not primes[i]]
print(res[k - 1])
