import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


def sieve(n):
    a = [False, False] + [True] * (n - 1)
    primes = []

    for i in range(2, n + 1):
        if a[i]:
            primes.append(i)
            for j in range(2 * i, n + 1, i):
                a[j] = False
    return tuple(primes)


def factorize(x):
    factor = 2
    ret = {}
    while x - 1:
        while x % factor:
            factor += 1
        if factor in ret:
            ret[factor] += 1
        else:
            ret[factor] = 1
        x //= factor
    return ret


def factorial_primes(x):
    ret = {}
    for p in primes:
        ret[p] = 0
        i = p
        while i <= x:
            ret[p] += x // i
            i *= p
    return ret


S, F, M = minput()
primes = sieve(M)
spf = factorial_primes(S + F)
s = factorial_primes(S)
f = factorial_primes(F)
comb_factors = {i: spf[i] - s[i] - f[i] for i in spf}

for m in range(M, 0, -1):
    m_factors = factorize(m)
    if all(m_factors[i] <= comb_factors[i] for i in m_factors):
        print(m)
        break
else:
    print(-1)
