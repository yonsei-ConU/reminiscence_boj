import sys
from itertools import permutations
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


N, M = minput()
seq = [list(minput()) for _ in range(N)]
kadane = []
for s in seq:
    dp = [0] * M
    max_val = 0
    max_idx = []
    for i in range(N):
        dp[i] = max(dp[i - 1], 0) + s[i]
        if dp[i] > max_val:
            max_val = dp[i]
            max_idx = [i]
        elif dp[i] == max_val:
            max_idx.append(i)
    
