import sys
from random import randint
from math import gcd
from collections import defaultdict
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


def miller_rabin(a, n):
    d = n - 1
    r = 0
    while not d & 1:
        d >>= 1
        r += 1

    x = pow(a, d, n)
    if x == 1 or x == n - 1:
        return True

    for i in range(r - 1):
        x = pow(x, 2, n)
        if x == n - 1:
            return True
    return False


def isprime(n):
    if n <= 71:
        if n in {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71}:
            return True
        else:
            return False
    else:
        for i in [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]:
            if not miller_rabin(i, n):
                return False
        return True


def pollard_rho(n):
    if isprime(n):
        return n

    for i in [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71]:
        if not n % i:
            return i
    g = lambda x, n, r: (x ** 2 + r) % n
    d = 1
    x = randint(2, n)
    y = x
    c = randint(1, n)

    while not d - 1:
        y = g(g(y, n, c), n, c)
        x = g(x, n, c)
        t = abs(x - y)
        d = gcd(t, n)

        if d == n:
            return pollard_rho(n)
    if isprime(d):
        return d
    return pollard_rho(d)


def distinct_primes(n):
    ret = []
    while n != 1:
        factor = pollard_rho(n)
        ret.append(factor)
        while not n % factor:
            n //= factor
    return set(ret)


n = int(input_())

grundy = [0, 1]
for i in range(2, n + 1):
    j = i - 1
    k = 0
    next_state = set()
    while j >= k:
        next_state.add(grundy[j] ^ grundy[k])
        j -= 1
        k += 1
    mex = 0
    while mex in next_state:
        mex += 1
    grundy.append(mex)

a = list(minput())
table = []
ans = 0
streak = defaultdict(int)
for x in a:
    primes = distinct_primes(x)
    to_remove = []
    for v in streak:
        if v not in primes:
            ans ^= grundy[streak[v]]
            to_remove.append(v)
    for v in to_remove:
        del streak[v]
    for p in primes:
        streak[p] += 1

for s in streak.values():
    ans ^= grundy[s]

if ans:
    print("First")
else:
    print("Second")
