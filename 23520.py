import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


n = int(input_())
songs = list(minput())

# dp[i] = songs[i]를 포함하면서 가장 repetition이 많은 경우의 repetition
# trace[i] = 위의 최적인 경우의 실제 해 (n <= 50 :D)
dp = [0] * n
trace = [[] for _ in range(n)]
trace[0] = [songs[0]]
for i in range(1, n):
    ans_dp = -1
    ans_trace = []
    for j in range(i):
        if dp[j] + (songs[i] == songs[j]) >= ans_dp:
            ans_dp = dp[j] + (songs[i] == songs[j])
            ans_trace = trace[j] + [songs[i]]
    dp[i] = ans_dp
    trace[i] = ans_trace

ans = dp.index(max(dp))
print(len(trace[ans]), dp[ans])
print(*trace[ans])
