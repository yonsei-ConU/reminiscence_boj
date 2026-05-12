import sys
from heapq import heappush, heappop
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


N = int(input_())
g = [[] for _ in range(N * N)]
d = list(minput())
for i in range(N - 1):
    g[i].append((i + 1, d[i]))
    g[i + 1].append((i, d[i]))

for i in range(1, N):
    x = i * N
    hori = list(minput())
    for j in range(N):
        g[x - N + j].append((x + j, hori[j]))
        g[x + j].append((x - N + j, hori[j]))
    vert = list(minput())
    for j in range(N - 1):
        g[x + j].append((x + j + 1, vert[j]))
        g[x + j + 1].append((x + j, vert[j]))

inf = float('inf')
# dp[i][j]: i번노드까지, j방향일때 최소 거리와 최대 턴수
# j=0이면 위아래, j=1이면 왼오른쪽
dp = [[[inf, -1], [inf, -1]] for _ in range(N * N)]
# i=0일때만 2번방향(null방향)정의
dp[0].append([0, -1])
heap = []
heappush(heap, (0, 0, 0, 2))
while heap:
    dist, turn, cur, direction = heappop(heap)
    turn = -turn
    if dist > dp[cur][direction][0] or dist == dp[cur][direction][0] and turn < dp[cur][direction][1]:
        continue
    elif cur == N * N - 1:
        exit(print(dist, turn))
    for nxt, nxtdist in g[cur]:
        new_dist = dist + nxtdist
        if abs(nxt - cur) == 1:
            nxt_direction = 0
        else:
            nxt_direction = 1
        if direction == 2:
            new_turn = 0
        else:
            new_turn = turn + (direction != nxt_direction)
        if new_dist < dp[nxt][nxt_direction][0] or (new_dist == dp[nxt][nxt_direction][0] and new_turn > dp[nxt][nxt_direction][1]):
            dp[nxt][nxt_direction] = [new_dist, new_turn]
            heappush(heap, (new_dist, -new_turn, nxt, nxt_direction))
assert False
