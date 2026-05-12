import sys
from collections import defaultdict
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


def sieve(n):
    a = [False,False] + [True]*(n-1)
    primes=[]

    for i in range(2,n+1):
      if a[i]:
        primes.append(i)
        for j in range(i*i, n+1, i):
            a[j] = False
    return tuple(primes)


N = int(input_())
t = list(minput())
primes = sieve(2000000)
ans = 0
for p in primes:
    if ans * p > 2000000:
        break
    mod = defaultdict(int)
    for i in range(N):
        mod[t[i] % p] += 1
    ans = max(ans, max(mod.values()))

print(ans)
