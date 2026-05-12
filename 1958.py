import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


def LCS_len(str1, str2, str3):
    len1 = len(str1)
    len2 = len(str2)
    len3 = len(str3)
    dp = [[[0 for k in range(len3 + 1)] for i in range(len2 + 1)] for j in range(len1 + 1)]

    for i in range(1, len1 + 1):
        for j in range(1, len2 + 1):
            for k in range(1, len3 + 1):
                if str1[i - 1] == str2[j - 1] == str3[k - 1]:
                    dp[i][j][k] = dp[i - 1][j - 1][k - 1] + 1
                else:
                    dp[i][j][k] = max(dp[i - 1][j][k], dp[i][j - 1][k], dp[i][j][k - 1])

    return dp


print(LCS_len(input_().rstrip(), input_().rstrip(), input_().rstrip())[-1][-1][-1])
