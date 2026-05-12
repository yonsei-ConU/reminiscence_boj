import sys
from collections import deque
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


def sum_n_dimensional_array(arr):
    if isinstance(arr, list):
        return sum(sum_n_dimensional_array(x) for x in arr)
    else:
        return arr


def adjust(a):
    if a < 0:
        return 0
    elif a >= N:
        assert a == N
        return N - 1
    return a


dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]
INF = 9876543

N = int(input_())
board = [input_().rstrip() for _ in range(N)]
# 방향: 위 0, 오른쪽 1, 아래 2, 왼쪽 3
# 오른쪽 방향을 보고 시작하는 애가 먼저 있는 두 개의 원소
# 오른쪽 방향을 보고 시작하는 애가 높은 비트 (4 * 오른쪽시작 + 위시작)
q = deque([(N - 1, 0, N - 1, 0, 4)])
dist = [[[[[INF] * 16 for _ in range(N)] for __ in range(N)] for ___ in range(N)] for ____ in range(N)]
dist[N - 1][0][N - 1][0][4] = 0

while q:
    # print(sum_n_dimensional_array(dist))
    y1, x1, y2, x2, direction = q.popleft()
    d1, d2 = direction // 4, direction % 4
    # 전진
    ny1, nx1, ny2, nx2 = y1 + dy[d1], x1 + dx[d1], y2 + dy[d2], x2 + dx[d2]
    if not (0 <= ny1 < N and 0 <= nx1 < N and board[ny1][nx1] == 'E') or (y1 == 0 and x1 == N - 1):
        ny1, nx1 = y1, x1
    if not (0 <= ny2 < N and 0 <= nx2 < N and board[ny2][nx2] == 'E') or (y2 == 0 and x2 == N - 1):
        ny2, nx2 = y2, x2
    if dist[ny1][nx1][ny2][nx2][direction] == INF:
        q.append((ny1, nx1, ny2, nx2, direction))
        dist[ny1][nx1][ny2][nx2][direction] = dist[y1][x1][y2][x2][direction] + 1
    # 좌회전
    nd1, nd2 = (d1 - 1) % 4, (d2 - 1) % 4
    if dist[y1][x1][y2][x2][nd1 * 4 + nd2] == INF:
        q.append((y1, x1, y2, x2, nd1 * 4 + nd2))
        dist[y1][x1][y2][x2][nd1 * 4 + nd2] = dist[y1][x1][y2][x2][direction] + 1
    # 우회전
    nd1, nd2 = (d1 + 1) % 4, (d2 + 1) % 4
    if dist[y1][x1][y2][x2][nd1 * 4 + nd2] == INF:
        q.append((y1, x1, y2, x2, nd1 * 4 + nd2))
        dist[y1][x1][y2][x2][nd1 * 4 + nd2] = dist[y1][x1][y2][x2][direction] + 1

print(min(dist[0][N - 1][0][N - 1]))
