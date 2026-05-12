import sys
import math
from collections import defaultdict
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


def miller_rabin(a, n):
    d = n - 1
    r = 0

    while not d % 2:
        d //= 2
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
        if n in [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71]:
            return True
        else:
            return False
    else:
        for i in [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]:
            if not miller_rabin(i, n):
                return False
        return True


def g(x, n, r):
    return (x ** 2 + r) % n


def pollard_rho(n):
    from random import randint
    if isprime(n):
        return n

    for i in [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71]:
        if not n % i:
            return i

    d = 1
    x = randint(2, n)
    y = x
    c = randint(1, n)

    while not d - 1:
        y = g(g(y, n, c), n, c)
        x = g(x, n, c)
        t = abs(x - y)
        d = math.gcd(t, n)

        if d == n:
            return pollard_rho(n)
    if isprime(d):
        return d
    return pollard_rho(d)


def factorize_return_dict(n):
    factors = defaultdict(int)
    while n > 1:
        factor = pollard_rho(n)
        if factor in factors:
            factors[factor] += 1
        else:
            factors[factor] = 1
        n //= factor
    return factors


gcd, lcm = minput()
gcd_factors, lcm_factors = factorize_return_dict(gcd), factorize_return_dict(lcm)
variable_factors = {x: lcm_factors[x] - gcd_factors[x] for x in lcm_factors}
v = [x ** variable_factors[x] for x in variable_factors]

ans_x, ans_y, ans_sum = 0, 0, float('inf')
for i in range(1 << (len(v) - 1)):
    x = gcd
    y = gcd
    for j in range(len(v)):
        if i & (1 << j):
            x *= v[j]
        else:
            y *= v[j]
    if x + y < ans_sum:
        ans_x = x
        ans_y = y
        ans_sum = x + y

if ans_y < ans_x:
    ans_x, ans_y = ans_y, ans_x
print(ans_x, ans_y)
