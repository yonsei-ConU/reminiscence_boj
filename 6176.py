import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


N, M = minput()
Mi = [int(input_()) for _ in range(N)]
ps = [M]
cur_sum = 0
for i in range(N): ps.append(ps[-1] + Mi[i])

# dp[i] = (i마리 소를 데려가는 데 걸리는 시간의 최솟값)
dp = ps[:]
for i in range(2, N + 1):
    for j in range(1, i):
        dp[i] = min(dp[i], dp[i - j] + dp[j] + M)

print(dp[N])
