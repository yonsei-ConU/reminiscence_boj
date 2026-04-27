import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


N, T, S = minput()
markets = [list(minput()) for _ in range(N)]

# i번의 iteration, i번째 야시장까지 방문한 상태
# dp[j]: j만큼의 시간이 흘렀을 때
# 얻을 수 있는 즐거움의 최댓값

dp = [0] * (T + 1)

for v, w in markets:
    dp_new = [0] * (T + 1)
    for j in range(T + 1):
        if not j:
            dp_new[j] = dp[j]
        elif j < w or j - w < S < j:
            dp_new[j] = max(dp[j], dp_new[j - 1])
        else:
            dp_new[j] = max(dp[j], dp[j - w] + v)
    dp = dp_new[:]

print(dp[-1])
