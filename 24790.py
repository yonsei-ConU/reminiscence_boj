import sys, heapq
from collections import defaultdict
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


def dijkstra_with_path(st):
    inf = float('inf')
    distances = defaultdict(lambda: inf)
    last = {}
    distances[st] = 0
    heap = []
    heapq.heappush(heap, (0, st))

    while heap:
        dist, cur = heapq.heappop(heap)
        y, x, direction = cur
        if distances[cur] < dist:
            continue
        # F
        ny, nx = y + dy[direction], x + dx[direction]
        if 0 <= ny < 8 and 0 <= nx < 8 and (g[ny][nx] == '.' or g[ny][nx] == 'D'):
            t = dist + 1
            if distances[(ny, nx, direction)] > t:
                distances[(ny, nx, direction)] = t
                last[(ny, nx, direction)] = ['F', cur]
                heapq.heappush(heap, (t, (ny, nx, direction)))
        # R, L
        for i in range(2):
            next_direction = [right[direction], left[direction]][i]
            t = dist + 1
            if distances[(y, x, next_direction)] > t:
                distances[(y, x, next_direction)] = t
                last[(y, x, next_direction)] = ['RL'[i], cur]
                heapq.heappush(heap, (t, (y, x, next_direction)))
        # XF
        if 0 <= ny < 8 and 0 <= nx < 8 and g[ny][nx] == 'I':
            t = dist + 2
            if distances[(ny, nx, direction)] > t:
                distances[(ny, nx, direction)] = t
                last[(ny, nx, direction)] = ['FX', cur]
                heapq.heappush(heap, (t, (ny, nx, direction)))

    return distances, last


dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]
right = [3, 2, 0, 1]
left = [2, 3, 1, 0]
g = []
for i in range(8):
    s = input_().rstrip()
    d = s.find('D')
    if d != -1:
        diamond = (i, d)
    g.append(s)

distances, last = dijkstra_with_path((7, 0, 2))
y, x = diamond
real_dist = min(distances[(y, x, i)] for i in range(4))
if real_dist == float('inf'): exit(print('no solution'))
for direction in range(4):
    y, x = diamond
    if distances[(y, x, direction)] != real_dist: continue
    ans = []
    while not (y == 7 and x == 0):
        if (y, x, direction) not in last:
            assert False
        trace, nxt = last[(y, x, direction)]
        ans.append(trace)
        ny, nx, nd = nxt
        y, x, direction = ny, nx, nd
    ans = ''.join(ans)
    break

print(ans[::-1])
