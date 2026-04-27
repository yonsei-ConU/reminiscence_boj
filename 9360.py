import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


for tc in range(1, int(input_()) + 1):
    _, _, first = input_().split()
    _, _, second = input_().split()
    prob = [int(first) / 100, int(second) / 100]
    # dp[i][j][k]: 처음 서브한쪽이 i일때, 선수0이 j판, 선수1이 k판 이길 확률
    dp = [[[0] * 8 for _ in range(8)] for __ in range(2)]
    dp[0][0][0] = 1
    dp[1][0][0] = 1
    for i in range(2):
        for j in range(8):
            for k in range(8):
                if not j and not k:
                    continue
                if 1 <= j <= 6 or (j == 7 and (k == 5 or k == 6)):  # 0번이 이김
                    dp[i][j][k] += dp[i][j - 1][k] * prob[((j + k) ^ i) & 1]
                if 1 <= k <= 6 or (k == 7 and (j == 5 or j == 6)):  # 1번이 이김
                    dp[i][j][k] += dp[i][j][k - 1] * prob[((j + k) ^ i) & 1]
    E = [[0, 0], [0, 0]]  # 한세트 이후, 처음 서브한쪽이 i일때, 경기수 홀짝이 j일때 판수 기댓값
    for i in range(2):
        E[i][0] = (6 * dp[i][6][0] + 8 * dp[i][6][2] + 10 * dp[i][6][4] + 12 * dp[i][7][5]) / (6 + 8 + 10 + 12)
        E[i][1] = (7 * dp[i][6][1] + 9 * dp[i][6][3] + 13 * dp[i][7][6]) / (7 + 9 + 13)
