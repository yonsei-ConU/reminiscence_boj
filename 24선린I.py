import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


MOD = 10 ** 9 + 7
k = int(input_())
p, q, r, s = minput()
t = int(input_())
ans = t

for i in range(k - 1):
    t = ((p + r) * t + (2 ** i) * (q + s)) % MOD
    ans = (ans + t) % MOD

print(ans)
