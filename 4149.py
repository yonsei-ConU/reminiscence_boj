import sys
from math import gcd
from random import randint
input_ = sys.stdin.readline


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
    g = lambda x, r: (x ** 2 + r) % n
    d = 1
    x = randint(2, n)
    y = x
    c = randint(1, n)

    while not d - 1:
        y = g(g(y, c), c)
        x = g(x, c)
        t = abs(x - y)
        d = gcd(t, n)

        if d == n:
            return pollard_rho(n)
    if isprime(d):
        return d
    return pollard_rho(d)

n = int(input_())
ans = []
while n - 1:
    ans.append((k := pollard_rho(n)))
    n //= k

print('\n'.join(map(str, sorted(ans))))
