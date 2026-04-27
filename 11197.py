import sys, heapq
from types import GeneratorType
input_ = sys.stdin.readline
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


def bootstrap(f, stack=[]):
    def wrappedfunc(*args, **kwargs):
        if stack:
            return f(*args, **kwargs)
        else:
            to = f(*args, **kwargs)
            while True:
                if type(to) is GeneratorType:
                    stack.append(to)
                    to = next(to)
                else:
                    stack.pop()
                    if not stack:
                        break
                    to = stack[-1].send(to)
            return to

    return wrappedfunc


@bootstrap
def dfs(cur, parent):
    dp_in[cur] = 1 - lamp[cur]
    dp_ex[cur] = 0
    if dist[cur] * 2 >= S:
        yield
    chk = False
    for nxt, _ in g[cur]:
        if nxt == parent:
            continue
        chk = True
        yield dfs(nxt, cur)
        if not lamp[cur]:
            dp_ex[cur] += dp_in[nxt]
            dp_in[cur] += min(dp_in[nxt], dp_ex[nxt])
        else:
            dp_ex[cur] = float('inf')
            dp_in[cur] += min(dp_in[nxt], dp_ex[nxt])
    yield


N, S = minput()
g = [[] for _ in range(N)]
for i in range(N - 1):
    a, b, d = minput()
    a -= 1; b -= 1
    g[a].append((b, d))
    g[b].append((a, d))

L = int(input_())
lamp = [False] * N
for element in list(minput()):
    lamp[element - 1] = True

dist = dijkstra(g, 0)
# dp_in[i] = i번을 루트로 하는 서브트리에서 i번에 램프가 있을 때 ~
dp_in = [float('inf')] * N
dp_ex = [float('inf')] * N
dfs(0, 0)
print(min(dp_in[0], dp_ex[0]))
