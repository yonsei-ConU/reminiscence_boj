import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


MOD = 998244353
n, k = minput()
a = list(minput())
f = []
cur = 0
for i in range(n):
    cur |= a[i]
    f.append(bin(cur).count('1'))

ans = 0
f = [0] + f
for i in range(n + 1):
    if f[i]:
        ans = (ans + i * 2 ** (k - f[i]) * (2 ** (f[i] - f[i - 1]) - 1)) % MOD

print(ans)
