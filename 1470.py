import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


N, L = minput()
gold, silver, bronze = minput()
gold += L
teams = sorted([list(minput()) for _ in range(N - 1)])

ans = 1
while teams:
    g, s, b = teams[-1]
    if g > gold:
        ans += 1
        teams.pop()
    else:
        break

for idx in range(len(teams)):
    if teams[idx][0] == gold:
        break

teams = teams[idx:]

dp = [set() for _ in range(len(teams) + 1)]
# dp[i][j]: until i_th team, GIVEN MEDALS TO j TEAMS
max_j = 0
for i in range(1, len(teams)):
    new_dp = [set() for _ in range(len(teams) + 1)]
    g, s, b = teams[i]
    if silver - s + 1 <= L:
        print('case 1')
        new_dp[1].add((silver - s + 1, 0))
        max_j = max(max_j, 1)
    if silver - s <= L and bronze - b + 1 <= L:
        print('case 2')
        new_dp[1].add((silver - s, bronze - b + 1))
        max_j = max(max_j, 1)
    for j in range(2, len(teams) + 1):
        for ss, bb in dp[j - 1]:
            if silver - s + 1 + ss <= L:
                print('case 3')
                new_dp[j].add((silver - s + 1 + ss, bb))
                max_j = max(max_j, j)
            if silver - s + ss <= L and bronze - b + 1 + bb <= L:
                print('case 4')
                new_dp[j].add((silver - s + ss, bronze - b + 1 + bb))
                max_j = max(max_j, j)
        for ss, bb in dp[j]:
            new_dp[j].add((ss, bb))
    for j in range(len(teams) + 1):
        dp[j] = new_dp[j].copy()

print(max_j + ans)
