import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


def tarjan(g):
    v = len(g)
    disc_low = [None] * v
    stack = []
    t = 0
    ret = []

    for start in range(v):
        if disc_low[start] is None:
            dfs_stack = [(start, 0)]
            while dfs_stack:
                cur, i = dfs_stack[-1]
                if disc_low[cur] is None:
                    disc_low[cur] = [t, t]
                    t += 1
                    stack.append(cur)
                    dfs_stack[-1] = (cur, 0)
                elif i < len(g[cur]):
                    nxt = g[cur][i]
                    dfs_stack[-1] = (cur, i + 1)
                    if disc_low[nxt] is None:
                        dfs_stack.append((nxt, 0))
                    elif disc_low[nxt][1] != 10**9:
                        disc_low[cur][1] = min(disc_low[cur][1], disc_low[nxt][0])
                else:
                    dfs_stack.pop()
                    if dfs_stack:
                        parent, _ = dfs_stack[-1]
                        disc_low[parent][1] = min(disc_low[parent][1], disc_low[cur][1])
                    if disc_low[cur][0] == disc_low[cur][1]:
                        scc = []
                        while True:
                            node = stack.pop()
                            scc.append(node)
                            disc_low[node][1] = 10**9
                            if cur == node:
                                break
                        ret.append(scc)

    return ret


for _ in range(int(input_())):
    N, M = minput()
    g = [[] for _ in range(N)]
    for _ in range(M):
        a, b = minput()
        g[a - 1].append(b - 1)
    pass
