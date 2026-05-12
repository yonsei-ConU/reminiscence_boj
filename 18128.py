import io, os
from heapq import heappop, heappush
from collections import deque
reader = io.BufferedReader(io.FileIO(0), buffer_size=131072)
text_reader = io.TextIOWrapper(reader, encoding='utf-8')
input_ = reader.readline
sinput = text_reader.readline
def minput(): return map(int, input_().split())


def dijkstra(y, x):
    distances = [[float('inf')] * N for _ in range(N)]
    distances[y][x] = 0
    heap = []
    heappush(heap, (0, y, x))
    while heap:
        dist, y, x = heappop(heap)
        if distances[y][x] < dist:
            continue
        for i in range(8):
            ny, nx = y + dy[i], x + dx[i]
            if (not (0 <= ny < N and 0 <= nx < N)) or g[ny][nx] == '0':
                continue
            t = max(distances[y][x], water_dist[ny][nx])
            if distances[ny][nx] > t:
                distances[ny][nx] = t
                heappush(heap, (t, ny, nx))

    return distances


output = []
dy = [1, -1, 0, 0, 1, 1, -1, -1]
dx = [0, 0, 1, -1, 1, -1, 1, -1]
N, W = minput()
q = deque()
water_dist = [[None] * N for _ in range(N)]
for _ in range(W):
    y, x = minput()
    q.append((y - 1, x - 1))
    water_dist[y - 1][x - 1] = 0
while q:
    y, x = q.popleft()
    for i in range(4):
        ny, nx = y + dy[i], x + dx[i]
        if (not (0 <= ny < N and 0 <= nx < N)) or water_dist[ny][nx] is not None:
            continue
        water_dist[ny][nx] = water_dist[y][x] + 1
        q.append((ny, nx))

g = [sinput().rstrip() for _ in range(N)]
distances = dijkstra(0, 0)
ans = 10 ** 18
for y, x in ((N - 2, N - 2), (N - 2, N - 1), (N - 1, N - 2)):
    ans = min(ans, distances[y][x])
output.append(str(ans) if ans != 10 ** 18 else '-1')
os.write(1, '\n'.join(output).encode())
os._exit(0)
