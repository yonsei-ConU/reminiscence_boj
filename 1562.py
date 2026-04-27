import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


mod = 1_000_000_000
N = int(input_())
dp = [[[0] * 10 for _ in range(2 ** 10)] for __ in range(N)]
# dp[i][j][k] = i-1자리 계단 수 중에 현재 쓰인 수들의 집합이 j이고 마지막 자리수가 k
for x in range(1, 10): dp[0][1 << x][x] = 1

for i in range(1, N):
    for mask in range(2, 1 << 10):
        for cur_k in range(10):
            if not cur_k:
                dp[i][mask | 2][1] = (dp[i][mask | 2][1] + dp[i - 1][mask][0]) % mod
            elif cur_k == 9:
                dp[i][mask | 256][8] = (dp[i][mask | 256][8] + dp[i - 1][mask][9]) % mod
            else:
                dp[i][mask | (1 << (cur_k + 1))][cur_k + 1] = (dp[i][mask | (1 << (cur_k + 1))][cur_k + 1] + dp[i - 1][mask][cur_k]) % mod
                dp[i][mask | (1 << (cur_k - 1))][cur_k - 1] = (dp[i][mask | (1 << (cur_k - 1))][cur_k - 1] + dp[i - 1][mask][cur_k]) % mod

print(sum(dp[-1][-1]) % mod)
