import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


N, L = minput()
gold, silver, bronze = minput()
gold += L
tmp = [list(minput()) for _ in range(N - 1)]
ans = 1
teams = []
for g, s, b in tmp:
    if g > gold:
        ans += 1
    elif g == gold:
        if s > silver or (s == silver and b > bronze):
            ans += 1
        teams.append((silver + 1 - s, bronze + 1 - b))

# teams는 (s, b)로 이루어짐, 은메달 s개를 주거나 은메달 s-1개, 동메달 b개를 주면 됨
# dp[i][j][k]: i번까지의 팀들 중 j개 팀의 등수를 올려줌, 은메달 k개 사용 -> 최소 동메달 개수??
T = len(teams)
dp = [[L + 1] * (L + 1) for _ in range(T + 1)]
prev = [[L + 1] * (L + 1) for _ in range(T + 1)]
dp[0][0] = 0
prev[0][0] = 0
ans2 = 0
for i in range(1, T + 1):
    dp = [[L + 1] * (L + 1) for _ in range(T + 1)]
    s, b = teams[i - 1]
    for j in range(1, i + 1):
        for k in range(s - 1, L + 1):
            # case1. 은메달 s
            if k != s - 1:
                dp[j][k] = min(dp[j][k], prev[j - 1][k - s])
            # case2. 은메달 s - 1, 동메달 b
            dp[j][k] = min(dp[j][k], prev[j - 1][k - s + 1] + b)
        if min(dp[j]) < L + 1:
            ans2 = max(ans2, j)
    dp, prev = prev, dp

print(ans + ans2)
