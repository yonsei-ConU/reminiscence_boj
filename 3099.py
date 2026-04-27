import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


word = input_().rstrip()
if len(word) == 1: exit(print(2))
# dp[i][j]: i번째 글자까지, 주 메모리에 j가 있을 때 횟수의 최솟값
dp = [[30000] * 26 for _ in range(len(word))]
dp[0][ord(word[0]) - 65] = 2
for i in range(1, len(word)):
    k = ord(word[i]) - 65
    m = min(dp[i - 1])
    for j in range(26):
        if j == k:
            dp[i][j] = min(dp[i][j], dp[i - 1][j] + 1, m + 2)
        else:
            dp[i][j] = min(dp[i][j], dp[i - 1][j] + 2)
            dp[i][k] = min(dp[i][k], m + 2)

print(dp[-1][k])
