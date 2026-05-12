import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


B = int(input_())
data = [int(input_()) for _ in range(int(input_()))]
N = len(data)
ps_normal = [0]
ps_square = [0]

for i in range(N):
    ps_normal.append(data[i] + ps_normal[-1])
    ps_square.append(data[i] * data[i] + ps_square[-1])

# dp[i][j] = (checked until data[i], has j buckets)
dp = [[10 ** 18] * (B + 1) for _ in range(N + 1)]
dp[0][0] = 0
for i in range(1, N + 1):
    for j in range(1, B + 1):
        ...
