import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


def dist(car_num, w1, w2):
    x1, y1 = events[w1]
    x2, y2 = events[w2]
    if not w1:
        if not car_num:
            return x2 + y2
        else:
            return 2 * (N - 1) - x2 - y2
    else:
        return abs(x2 - x1) + abs(y2 - y1)


inf = float('inf')
N = int(input_())
W = int(input_())
# dp[i][j]: 1번 경찰차가 마지막으로 해결한 사건 번호 i, 2번 경찰차가 마지막으로 해결한 사건 번호 j (1-indexed)
# 일 때 두 경찰차의 이동 거리의 최솟값
dp = [[inf] * (W + 1) for _ in range(W + 1)]
dp[0][0] = 0
events = [[0, 0]] + [list(map(lambda x: int(x) - 1, input_().split())) for _ in range(W)]

for i in range(W):
    for j in range(W):
        nxt = max(i, j) + 1
        dp[nxt][j] = min(dp[nxt][j], dp[i][j] + dist(0, i, nxt))
        dp[i][nxt] = min(dp[i][nxt], dp[i][j] + dist(1, j, nxt))
# for d in dp: print(*d)

least = inf
trace = (W, W)
ans = []
for i in range(W):
    if dp[i][W] < least:
        least = dp[i][W]
        trace = (i, W)

flag = 2
for j in range(W):
    if dp[W][j] < least:
        least = dp[W][j]
        trace = (W, j)
        flag = 1

print(least)
# print(trace)
ans = [flag]
while trace[0] or trace[1]:
    next_trace = (0, 0)
    I, J = trace
    least = inf
    for i in range(I):
        if max(i, J) + 1 == max(I, J) and dp[i][J] <= least and dp[i][J] + dist(0, i, I) == dp[I][J]:
            least = dp[i][J]
            next_trace = (i, J)

    for j in range(J):
        if max(I, j) + 1 == max(I, J) and dp[I][j] <= least and dp[I][j] + dist(1, j, J) == dp[I][J]:
            least = dp[I][j]
            next_trace = (I, j)

    if trace[0] == next_trace[0]:
        ans.append(2)
    else:
        assert trace[1] == next_trace[1]
        ans.append(1)
    trace, next_trace = next_trace, trace
    # print(trace)

for i in range(trace[0]):
    ans.append(1)
for i in range(trace[1]):
    ans.append(2)

print(*ans[:0:-1], sep='\n')
