import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


def nCk(n, k):
    if k < 0 or k > n:
        return 0
    nu = factorial_mod[n]
    de = factorial_mod[k] * factorial_mod[n - k]
    return nu * pow(de, -1, MOD) % MOD


MOD = 10 ** 9 + 7
n, k = minput()
g = [list(map(int, list(input_().rstrip()))) for _ in range(n)]
zero = 0
for row in g:
    zero += row.count(0)

factorial_mod = [1, 1]
for i in range(2, max(zero, n * n) + 1):
    factorial_mod.append(factorial_mod[-1] * i % MOD)

ans = 0
# horizontal
for i in range(n):
    x = 0
    for j in range(n):
        if not g[i][j]:
            x += 1
    ans = (ans + nCk(zero - x, k - x)) % MOD

# vertical
for j in range(n):
    y = 0
    for i in range(n):
        if not g[i][j]:
            y += 1
    ans = (ans + nCk(zero - y, k - y)) % MOD

# diagonal1
z = 0
for i in range(n):
    if not g[i][i]:
        z += 1
ans = (ans + nCk(zero - z, k - z)) % MOD

# diagonal2
z = 0
for i in range(n):
    if not g[i][n - i - 1]:
        z += 1
ans = (ans + nCk(zero - z, k - z)) % MOD

print(ans * pow(nCk(zero, k), -1, MOD) * factorial_mod[n * n] % MOD)
