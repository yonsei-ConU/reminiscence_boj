import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


dist_safe = int(input_())
repair = int(input_())
dist_between_repair = list(minput())
repair_times = list(minput())
# i 번째 정비소에서 repair_times[i]만큼 시간 걸림
# i-1 번째에서 i 번째 정비소까지 가는 거리 dist_between_repair[i]

#dp[i][j]: i번째 정비소까지 지나 왔음, 마지막으로 j번째 정비소에서 정비를 받음.
dp = [[[10000000000, -1] for __ in range(repair + 1)] for _ in range(repair + 1)]
dp[0][0] = [0, -1]

for i in range(1, repair + 1):
    cur_sum = 0
    for j in range(i)[::-1]:
        dd = dist_between_repair[j]
        cur_sum += dd
        if cur_sum <= dist_safe:
            dp[i][j] = dp[i-1][j]
        else:
            cur_sum = 0
            break
    t = dp[i][i][0]
    for j in range(i)[::-1]:
        dd = dist_between_repair[j]
        cur_sum += dd
        if cur_sum <= dist_safe:
            t = min(t, dp[i-1][j][0] + repair_times[i])
        else:
            break
    dp[i][i] = [t, j]

print(dp)
