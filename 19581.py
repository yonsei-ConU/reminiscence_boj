import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


def dijkstra(g, st, v):
    import heapq
    distances = [float('inf')] * v
    distances[st] = 0
    heap = []
    heapq.heappush(heap, (0, st))

    while heap:
        dist, cur = heapq.heappop(heap)
        if distances[cur] < dist:
            continue
        for nextnum, nextdist in g[cur]:
            t = dist + nextdist
            if distances[nextnum] > t:
                distances[nextnum] = t
                heapq.heappush(heap, (t, nextnum))

    return distances


def find_max(arr):
    max_idx = 0
    max_val = arr[0]
    for i in range(1, len(arr)):
        if arr[i] > max_val:
            max_idx = i
            max_val = arr[i]
    return max_idx, max_val


V = int(input_())
g = [[] for _ in range(V)]
for _ in range(V):
    l = list(minput())
    for i in range(1, len(l)-1, 2):
        g[l[0]-1].append((l[i]-1, l[i+1]))

d = find_max(dijkstra(g, 0, V))[0]
ans = find_max(dijkstra(g, d, V))[1]
print(ans)
