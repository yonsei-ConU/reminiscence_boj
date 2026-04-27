import heapq, io, os, __pypy__
reader = io.BufferedReader(io.FileIO(0), buffer_size=131072)
input_ = reader.readline
def minput(): return map(int, input_().split())


def dijkstra(g, st):
    distances = [float('inf')] * len(g)
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


output = []
N, M, K, Q = minput()
g = [[] for _ in range(N)]
g_inv = [[] for _ in range(N)]
for _ in range(M):
    u, v, d = minput()
    g[u - 1].append((v - 1, d))
    g_inv[v - 1].append((u - 1, d))

pub = [int(input_()) - 1 for _ in range(K)]
pub_inv = [-1] * N
dist = __pypy__.newlist_hint(K)
for i in range(K):
    d = dijkstra(g, pub[i])
    dist.append([d[x] for x in pub])
    pub_inv[pub[i]] = i

ans1 = 0
ans2 = 0
for _ in range(Q):
    a, b = minput()
    a -= 1; b -= 1
    if pub_inv[a] != -1:
        near_a = [(a, 0)]
    else:
        near_a = g[a]
    if pub_inv[b] != -1:
        near_b = [(b, 0)]
    else:
        near_b = g_inv[b]
    tmp = 10 ** 18
    for u, c1 in near_a:
        for v, c2 in near_b:
            tmp = min(tmp, c1 + c2 + dist[pub_inv[u]][pub_inv[v]])
    if tmp != 10 ** 18:
        ans1 += 1
        ans2 += tmp

output.append(str(ans1))
output.append(str(ans2))
os.write(1, '\n'.join(output).encode())
os._exit(0)
