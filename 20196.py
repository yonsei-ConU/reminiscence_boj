import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


n, m = minput()
fear = input_().rstrip()
favorite = input_().rstrip()
# dp[i][j]: i번째 글자까지 완료, 위치가 j
dp = [[1000000] * n for _ in range(m)]
for j in range(n):
    if fear[j] == favorite[0]:
        dp[0][j] = 0

for i in range(1, m):
    for j in range(n):
        if favorite[i] != fear[j]:
            continue
        if j:
            for k in range(n):
                if fear[j - 1] == fear[k]:
                    dp[i][j] = min(dp[i][j], dp[i - 1][k] + abs(j - 1 - k) + 1)
        if j != n - 1:
            for k in range(n):
                if fear[j + 1] == fear[k]:
                    dp[i][j] = min(dp[i][j], dp[i - 1][k] + abs(j + 1 - k) + 1)

# print(*dp, sep='\n')
ans = min(dp[m - 1])
print(ans if ans != 1000000 else -1)
