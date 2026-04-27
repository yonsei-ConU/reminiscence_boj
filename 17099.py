import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


N = int(input_())
contests = []
distinct = set()
for i in range(N):
    S, E, C = minput()
    distinct.add(S)
    distinct.add(E)
    contests.append((S, E, C))

distinct = sorted(distinct)
rank = {distinct[i]: i for i in range(len(distinct))}
# dp[i] := (좌표압축된) 시간 i까지, 얻을 수 있는 최대 상금
dp = [0] * len(distinct)
contests.sort(key=lambda x: x[1])
last_time = 1
for start_time, cur_time, money in contests:
    start_time = rank[start_time]
    cur_time = rank[cur_time]
    if not start_time:
        last_val = 0
    else:
        last_val = dp[start_time - 1]
    dp[cur_time] = max(dp[cur_time], last_val + money)
    for t in range(last_time, cur_time + 1):
        dp[t] = max(dp[t], dp[t - 1])

print(dp[-1])
