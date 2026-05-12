import sys
from math import gcd
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


N = int(input_())
S = [int(input_()) for _ in range(N)]
lS = [len(str(s)) for s in S]
pre = [0] * (1 << N)
for i in range(N):
    for j in range(1 << i, 1 << N, 1 << (i + 1)):
        for k in range(j, j + (1 << i)):
            pre[k] += lS[i]

K = int(input_())
pow10 = [1 % K]
for i in range(sum(lS)):
    pow10.append(pow10[-1] * 10 % K)

# dp[mask][mod] = 처리된 수 집합이 mask일 때 이어붙인 것들 나머지가 mod인 경우의 수
# mask는 증가하는 방향으로만 상태전이됨 -> mask 기준으로 한 번만 돌리면 됨
# 앞에다가 붙이는 경우만 생각하면 됨
dp = [[0] * K for _ in range(1 << N)]
for i in range(N):
    dp[1 << i][S[i] % K] = 1
for mask in range(1 << N):
    for nxt in range(N):
        if mask & (1 << nxt): continue
        for mod in range(K):
            dp[mask | (1 << nxt)][(mod + pow10[pre[mask]] * S[nxt]) % K] += dp[mask][mod]

nu = dp[-1][0]
de = sum(dp[-1])
if not nu:
    de = 1
else:
    g = gcd(nu, de)
    nu //= g
    de //= g

print(f"{nu}/{de}")
