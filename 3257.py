import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


S = input_().rstrip()
T = input_().rstrip()
ST = input_().rstrip()

dp = [[False] * (len(T) + 1) for _ in range(len(S) + 1)]
dp[0][0] = True
for i in range(1, len(S) + 1):
    if S[i - 1] == ST[i - 1]:
        dp[i][0] = True
for j in range(1, len(T) + 1):
    if T[j - 1] == ST[j - 1]:
        dp[0][j] = True

for i in range(1, len(S) + 1):
    for j in range(1, len(T) + 1):
        if (dp[i - 1][j] and S[i - 1] == ST[i + j - 1]) or (dp[i][j - 1] and T[j - 1] == ST[i + j - 1]):
            dp[i][j] = True

assert dp[-1][-1]
i = len(S)
j = len(T)
ans = []
while i | j:
    if i and dp[i - 1][j]:
        ans.append('1')
        i -= 1
    elif j and dp[i][j - 1]:
        ans.append('2')
        j -= 1

ans.append('1' * i)
ans.append('2' * j)

print(''.join(ans[::-1]))
