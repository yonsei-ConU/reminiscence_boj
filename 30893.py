import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


sys.setrecursionlimit(200000)
N, S, E = minput()
S -= 1; E -= 1
g = [[] for _ in range(N)]
for _ in range(N - 1):
    u, v = minput()
    g[u - 1].append(v - 1)
    g[v - 1].append(u - 1)

depth = [-1] * N
depth[S] = 0
par = [-1] * N


def dfs(cur, parent):
    for nxt in g[cur]:
        if nxt == parent:
            continue
        depth[nxt] = depth[cur] + 1
        par[nxt] = cur
        dfs(nxt, cur)


dfs(S, -1)

path = []
cur = E
while cur != -1:
    path.append(cur)
    cur = par[cur]
path = path[::-1]

ans = 1
for i in range(1, len(path) - 1, 2):
    for nxt in g[path[i]]:
        if nxt != path[i - 1] and nxt != path[i + 1]:
            ans = 0
            break
    if not ans: break

print('SFeicrosntd'[ans::2])
