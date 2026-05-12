import sys
from collections import deque
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


INF = 100000000
n, k = minput()
transitions = [list(map(lambda x: int(x) - 1, input_().split())) for _ in range(n)]
dist = [[[[INF] * 4 for _ in range(3)] for __ in range(k + 1)] for ___ in range(n)]
dist[0][k][0] = [0, 0, 0, 0]
q = deque([(0, k, 0, 0), (0, k, 0, 1), (0, k, 0, 2), (0, k, 0, 3)])
while q:
    cur, blinker_left, cur_blinker, direction = q.popleft()
    cur_dist = dist[cur][blinker_left][cur_blinker][direction]
    # 이동
    ndirec = (direction + cur_blinker) % 4
    nxt = transitions[cur][ndirec]
    if nxt != -1:
        ndirec2 = (transitions[nxt].index(cur) + 2) & 3
    else:
        ndirec2 = 998244353
    if nxt != -1 and cur_dist + 1 < dist[nxt][blinker_left][cur_blinker][ndirec2]:
        q.append((nxt, blinker_left, cur_blinker, ndirec2))
        dist[nxt][blinker_left][cur_blinker][ndirec2] = cur_dist + 1
    # blinker을 끄는 경우
    if cur_blinker:
        if cur_dist < dist[cur][blinker_left][0][direction]:
            q.appendleft((cur, blinker_left, 0, direction))
            dist[cur][blinker_left][0][direction] = cur_dist
    # 왼쪽 blinker을 켜는 경우
    if cur_blinker != -1 and blinker_left:
        nuses = blinker_left - 1
        if cur_dist < dist[cur][nuses][-1][direction]:
            q.appendleft((cur, nuses, -1, direction))
            dist[cur][nuses][-1][direction] = cur_dist
    # 오른쪽 blinker을 켜는 경우
    if cur_blinker != 1 and blinker_left:
        nuses = blinker_left - 1
        if cur_dist < dist[cur][nuses][1][direction]:
            q.appendleft((cur, nuses, 1, direction))
            dist[cur][nuses][1][direction] = cur_dist

ans = INF
for j in range(k + 1):
    for kk in range(3):
        for l in range(4):
            ans = min(ans, dist[n - 1][j][kk][l])

if ans == INF:
    print("impossible")
else:
    print(ans)
