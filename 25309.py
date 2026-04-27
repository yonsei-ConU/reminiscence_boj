import sys
from math import isqrt
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


def p(x):
    for i in range(2, isqrt(x) + 1):
        if not x % i:
            return False
    return True


N, K = minput()
n, k = N, K

if K == 1:
    if p(N):
        res = [str(N)]
    else:
        res = []
else:
    if (N + K) % 2:
        N -= 2
        res = ['2']
        K -= 1
    else:
        res = []
    while N > 2 * K + N % 2 and N > 0:
        if K == 1:
            res.append(str(N))
            break
        left = 2 * K - 1 + N % 2
        while True:
            i = N - left
            if (True if K != 2 else p(left)) and p(i):
                res.append(str(i))
                N = left
                K -= 1
                break
            left += 1
    if N == 2 * K:
        res += ['2'] * K
    elif N == 2 * K + 1:
        res += ['2'] * (K - 1) + ['3']

if sum(map(int, res)) == n and len(res) == k and all(p(int(x)) for x in res):
    print(' '.join(res))
else:
    print(-1)
