import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


l1 = int(input_())
dna1 = input_().rstrip()
l2 = int(input_())
dna2 = input_().rstrip()
# dp[i][j]: 1번째는 i번 글자까지, 2번째는 j번 글자까지 (1-index)
dp = [[0] * (l2 + 1) for _ in range(l1 + 1)]

max_val = -5000000
max_idx = (-1, -1)
for i in range(1, l1 + 1):
    for j in range(1, l2 + 1):
        dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]) - 2
        if dna1[i - 1] == dna2[j - 1]:
            dp[i][j] = max(dp[i][j], dp[i - 1][j - 1] + 3)
        else:
            dp[i][j] = max(dp[i][j], dp[i - 1][j - 1] - 2)
        dp[i][j] = max(0, dp[i][j])
        if dp[i][j] > max_val:
            max_val = dp[i][j]
            max_idx = (i, j)

print(max_val)
i, j = max_idx
cur_min = max_val
cur_val = max_val
min_idx = (-1, -1)
while i and j:
    if dp[i - 1][j - 1] == cur_val - 3:
        cur_val -= 3
        if cur_val < cur_min:
            cur_min = cur_val
            min_idx = (i - 1, j - 1)
        i -= 1; j -= 1
    elif dp[i - 1][j] == cur_val + 2:
        cur_val += 2
        i -= 1
    elif dp[i][j - 1] == cur_val + 2:
        cur_val += 2
        j -= 1
    elif dp[i - 1][j - 1] == cur_val + 2:
        cur_val += 2
        i -= 1
        j -= 1
    else:
        break

i, j = min_idx
p, q = max_idx
print(dna1[i:p])
print(dna2[j:q])
