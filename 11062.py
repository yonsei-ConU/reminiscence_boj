import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


for _ in range(int(input_())):
    N = int(input_())
    cards = list(minput())
    # dp[i][j]: i~j th card, difference of score
    dp = [[0] * N for _ in range(N)]
    for i in range(N):
        dp[i][i] = cards[i]

    for diff in range(1, N):
        for start in range(N - diff):
            end = start + diff
            dp[start][end] = max(cards[i] - dp[start][i] - dp[i + 1][end] for i in range(start, end))

    ans = max(dp[-1]) + sum(cards)
    assert not ans % 2
    print(ans // 2)
