import io, os
reader = io.BufferedReader(io.FileIO(0), buffer_size=131072)
text_reader = io.TextIOWrapper(reader, encoding='utf-8')
input_ = reader.readline
sinput = text_reader.readline
def minput(): return map(int, input_().split())


def dijkstra(g, st):
    '''
    g: graph, g[start] = (end, dist)
    st: start node
    '''
    import heapq
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
N, M, K = minput()
g = [[] for _ in range(N)]
for _ in range(M):
    a, b, c = minput()
    a -= 1; b -= 1
    g[a].append((b, c))
    g[b].append((a, c))

X = int(input_())
E = list(map(lambda x: int(x) - 1, input_().split()))
dist = dijkstra(g, 0)
ans = 10 ** 18

for i in range(X):
    # E[i]번 출구가 처음 열리는 때는 K * i + K * X * z (z>=0인정수)
    start_time = K * i
    distance = dist[E[i]]
    t = distance % (K * X)
    cycle = distance - t
    if t < K * i:
        ans = min(ans, K * i + cycle)
    elif t < K * (i + 1):
        ans = min(ans, distance)
    else:
        ans = min(ans, K * i + cycle + K * X)

output.append(str(ans))

os.write(1, '\n'.join(output).encode())
os._exit(0)
