import sys
sys.setrecursionlimit(1000010)
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


def dfs(cur, parent, depth):
    chk = False
    for nxt in g[cur]:
        if nxt == parent:
            continue
        chk = True
        dfs(nxt, cur, depth + 1)
    if not chk:
        cc.append(depth)


n, m, p = minput()
g = [[] for _ in range(n)]

for _ in range(m):
    a, b = minput()
    a -= 1; b -= 1
    g[a].append(b)
    g[b].append(a)

cc = []
visited = [False] * n
