import sys, heapq
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


def dijkstra_with_path(g, st):
    v = len(g)
    distances = [float('inf')] * v
    last = [0] * v
    distances[st] = 0
    heap = []
    heapq.heappush(heap, (0, st))

    while heap:
        dist, cur = heapq.heappop(heap)
        if distances[cur] < dist:
            continue
        for nextnum in g[cur]:
            nextdist = g[cur][nextnum]
            t = dist + nextdist
            if distances[nextnum] > t:
                distances[nextnum] = t
                last[nextnum] = cur
                heapq.heappush(heap, (t, nextnum))

    return distances, last


N, M = minput()
g = [{} for _ in range(N)]
for _ in range(M):
    A, B, L = minput()
    A -= 1; B -= 1
    g[A][B] = L
    g[B][A] = L

distances, last = dijkstra_with_path(g, 0)
original_dist = distances[N - 1]
cur = N - 1
path = [N - 1]
while cur:
    cur = last[cur]
    path.append(cur)

path = path[::-1]
ans = 0
for i in range(len(path) - 1):
    g[path[i]][path[i + 1]] <<= 1
    distances, _ = dijkstra_with_path(g, 0)
    ans = max(ans, distances[N - 1] - original_dist)
    g[path[i]][path[i + 1]] >>= 1

print(ans)
