import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


# dp[i][j]: i를 만들 수 있는 방법의 수 단 쓰인 것 중 가장 큰 수가 j
dp = [[0, 0, 0] for i in range(10001)]
dp[1] = [1, 0, 0]  # 1
dp[2] = [1, 1, 0]  # 2, 1+1
dp[3] = [2, 0, 1]  # 3, 2+1, 1+1+1

for i in range(4, 10001):
    dp[i][0] = dp[i - 1][0] + dp[i - 1][1] + dp[i - 1][2]
    dp[i][1] = dp[i - 2][1] + dp[i - 2][2]
    dp[i][2] = dp[i - 3][2]

for _ in range(int(input_())):
    print(sum(dp[int(input_())]))
