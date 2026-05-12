import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


N, M, K, B = minput()
categories = [[] for _ in range(M)]
for _ in range(N):
    pt, c = minput()
    categories[c - 1].append(pt)

items = [[] for _ in range(M)]
for i in range(M):
    categories[i].sort(reverse=True)
    cur_sum = 0
    for j in range(len(categories[i])):
        cur_sum += categories[i][j]
        if j + 1 == len(categories[i]):
            cur_sum += B
        items[i].append((cur_sum, j + 1))

# dp[i][j]: i번째 카테고리까지, 총 문제수 j일 때 점수의 최댓값
dp = [[0] * (K + 1) for _ in range(M + 1)]
for i in range(1, M + 1):
    for j in range(1, K + 1):
        dp[i][j] = dp[i - 1][j]
        for value, weight in items[i - 1]:
            if j >= weight:
                dp[i][j] = max(dp[i][j], dp[i - 1][j - weight] + value)

print(max(dp[M]))
