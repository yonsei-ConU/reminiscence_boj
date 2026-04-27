import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


N = int(input_())
scores = list(minput())

# pM[i][j] = max(scores[i..j]), pm은 min
pM = [[0] * N for _ in range(N)]
pm = [[10000] * N for _ in range(N)]
for i in range(N):
    pM[i][i] = pm[i][i] = scores[i]
    for j in range(i + 1, N):
        pM[i][j] = max(pM[i][j - 1], scores[j])
        pm[i][j] = min(pm[i][j - 1], scores[j])

# dp[i] = i번째 사람까지 확인
dp = [0] * N
for i in range(1, N):
    for j in range(i):
        # i번째 사람으로 끝나는 조가 j번째 사람부터 시작
        dp[i] = max(dp[i], pM[j][i] - pm[j][i] + (dp[j - 1] if j else 0))

print(dp[-1])
