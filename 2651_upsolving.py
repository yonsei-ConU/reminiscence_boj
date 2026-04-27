import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


dist_safe = int(input_())
repair = int(input_())
dist_between_repair = list(minput())
repair_times = list(minput()) + [0]

# dp[i]: i번째 지점에서 마지막으로 정비를 받았을 때 걸리는 최소 시간
# 0은 시작지점, 마지막은 끝지점, 나머지는 정비소 1인덱스
dp = [float('inf') for _ in range(repair + 2)]
dp[0] = 0
last = [0 for _ in range(repair + 2)]

for i in range(1, repair + 2):
    cur_dist = 0
    for j in range(i - 1, -1, -1):
        cur_dist += dist_between_repair[j]
        if cur_dist > dist_safe:
            break
        if dp[j] + repair_times[i - 1] < dp[i]:
            dp[i] = dp[j] + repair_times[i - 1]
            last[i] = j

print(dp[-1])
cur = repair + 1
trace = []
while cur:
    cur = last[cur]
    trace.append(cur)

trace.pop()
print(len(trace))
if trace: print(*trace[::-1])
