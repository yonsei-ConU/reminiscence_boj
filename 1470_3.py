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
    t = []
    if g > gold:
        ans += 1
        continue
    elif g == gold:
        if s > silver or (s == silver and b > bronze):
            ans += 1
            continue
        elif b > bronze:
            if silver - s <= L:
                t.append((silver - s, 0))
        else:
            if silver - s + 1 <= L:
                t.append((silver - s + 1, 0))
            if silver - s + bronze - b + 1 <= L:
                t.append((silver - s, bronze - b + 1))
    teams.append(t)

# teams[i]는 (s, b)로 이루어짐, 각각 은메달 s개 동메달 b개를 주면 됨을 의미
# dp_(i-th loop)_[j][k]: i번까지의 팀들 중 j개 팀의 등수를 올려줌, 은메달 k개 사용 -> 최소 동메달 개수??
T = len(teams)
prev = [[L + 1] * (L + 1) for _ in range(T + 1)]
prev[0][0] = 0
ans2 = 0
for i in range(1, T + 1):
    dp = [tmp[:] for tmp in prev]
    for j in range(1, i + 1):
        for s, b in teams[i - 1]:
            for k in range(s, L + 1):
                dp[j][k] = min(dp[j][k], prev[j - 1][k - s] + b)
        if min(dp[j]) < L + 1:
            ans2 = max(ans2, j)
    dp, prev = prev, dp

print(ans + ans2)
