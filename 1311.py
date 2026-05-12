import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


INF = 345678
N = int(input_())
D = [list(minput()) for _ in range(N)]
# dp[i][mask] = (i번째 사람까지만, 완료한 일의 집합이 mask)
dp = [[INF] * (1 << N) for _ in range(N + 1)]
dp[0][0] = 0
for i in range(N):
    for mask in range(1 << N):
        if mask.bit_count() != i + 1: continue
        for bit in range(N):
            if not mask & (1 << bit): continue
            dp[i + 1][mask] = min(dp[i + 1][mask], dp[i][mask ^ (1 << bit)] + D[i][bit])

print(dp[-1][-1])
