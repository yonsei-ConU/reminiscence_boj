import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())

s = input()
dp = [1] + [3000] * (len(s) - 1)
pal = set()
for i in range(1, len(s)):
    next_pal = set()
    for j in range(i):
        if s[j] == s[i]:
            if i - j == 1:
                next_pal.add(j)
                if not j:
                    dp[i] = 1
                else:
                    dp[i] = min(dp[i], dp[j - 1] + 1)
            else:
                if j + 1 in pal or i - j == 2:
                    next_pal.add(j)
                    if not j:
                        dp[i] = 1
                    else:
                        dp[i] = min(dp[i], dp[j - 1] + 1)
    pal = next_pal
    next_pal = set()
    dp[i] = min(dp[i], dp[i-1] + 1)

print(dp[-1])
