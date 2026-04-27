import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


def sieve(n):
    a = [False, False] + [True] * (n - 1)

    for i in range(2, n + 1):
        if a[i]:
            for j in range(i * i, n + 1, i):
                a[j] = False
    return a


def hopcroft_karp(adj, n, m):
    from collections import deque

    g_match = [-1] * n
    h_match = [-1] * m
    dist = [0] * n
    inf = float('inf')

    def hk_bfs():
        q = deque()
        for u in range(n):
            if g_match[u] == -1:
                dist[u] = 0
                q.append(u)
            else:
                dist[u] = inf

        ret = inf
        while q:
            u = q.popleft()
            if dist[u] >= ret:
                continue
            for v in adj[u]:
                if h_match[v] == -1:
                    ret = dist[u] + 1
                elif dist[h_match[v]] == inf:
                    dist[h_match[v]] = dist[u] + 1
                    q.append(h_match[v])

        return ret != inf

    def hk_dfs(u):
        for v in adj[u]:
            if h_match[v] == -1 or (dist[h_match[v]] == dist[u] + 1 and hk_dfs(h_match[v])):
                g_match[u] = v
                h_match[v] = u
                return True
        dist[u] = inf
        return False

    ret = 0
    while hk_bfs():
        for u in range(n):
            if g_match[u] == -1:
                ret += hk_dfs(u)

    return ret


N = int(input_())
l = list(minput())
odd = [i for i in l if i % 2]
even = [i for i in l if not i % 2]
isPrime = sieve(2000)
g = [[] for _ in range(N)]

for i in range(len(odd)):
    for j in range(len(even)):
        if isPrime[odd[i] + even[j]]:
            g[i].append(j)

ans = []
print(g)

if ans:
    print(*ans)
else:
    print(-1)
