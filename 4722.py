import sys
import heapq
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


def prim():
    total_cost = 0.0
    min_heap = [(0, 0)]
    visited = [False] * N
    edges_used = 0

    while min_heap and edges_used < N:
        cost, u = heapq.heappop(min_heap)
        if visited[u]:
            continue

        visited[u] = True
        total_cost += cost
        edges_used += 1

        for next_cost, v in g[u]:
            if not visited[v]:
                heapq.heappush(min_heap, (next_cost, v))

    return total_cost


while True:
    N = int(input_())
    if not N:
        break
    g = [[] for _ in range(N)]
    points = [tuple(minput()) for _ in range(N)]
    for i in range(N):
        for j in range(i):
            g[i].append((((points[i][0] - points[j][0]) ** 2 + (points[i][1] - points[j][1]) ** 2) ** 0.5, j))
            g[j].append((((points[i][0] - points[j][0]) ** 2 + (points[i][1] - points[j][1]) ** 2) ** 0.5, i))
    mst_weight = prim()
    print(f"{mst_weight:.2f}")
