import sys
from math import sqrt
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


def f(x):
    i = 1
    cur = x
    ans = 0

    while cur > sqrt(x):
        nxt = x // (i + 1) + 1
        if nxt % 2 and cur % 2:
            sign = -1
        elif not nxt % 2 and not cur % 2:
            sign = 1
        else:
            sign = 0
        ans += sign * i
        cur = nxt - 1
        i += 1
    for i in range(1, cur + 1):
        ans += (-1) ** i * (x // i)

    return ans


def g(x):
    ans = 0
    for i in range(1, x + 1):
        ans += (-1) ** i * (x // i)
    return ans


S, T = minput()
print(f(T) - f(S - 1))
