import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


def nc3(n):
    return n * (n - 1) * (n - 2) // 6


N, M = minput()
ans = nc3((N + 1) * (M + 1))
ans -= (N + 1) * nc3(M + 1)
ans -= (M + 1) * nc3(N + 1)
for dx in range(1, (N // 2) + 1):
    for dy in range(1, (M // 2) + 1):
        ...
