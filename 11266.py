import sys
sys.setrecursionlimit(10000)
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


def find_articulation_point(g):
    time = -1
    disc = [-1] * len(g)
    low = [-1] * len(g)
    par = [-1] * len(g)
    ret = [False] * len(g)

    def dfs(cur):
        nonlocal time
        time += 1
        disc[cur] = time
        low[cur] = time
        children_count = 0
        for nxt in g[cur]:
            if disc[nxt] == -1:
                children_count += 1
                par[nxt] = cur
                dfs(nxt)
                low[cur] = min(low[cur], low[nxt])
                if par[cur] != -1 and low[nxt] >= disc[cur]:
                    ret[cur] = True
            elif nxt != par[cur]:
                low[cur] = min(low[cur], disc[nxt])
        if par[cur] == -1 and children_count > 1:
            ret[cur] = True

    for root in range(len(g)):
        if disc[root] == -1:
            dfs(root)

    return ret


V, E = minput()
g = [[] for _ in range(V)]
for _ in range(E):
    a, b = minput()
    a -= 1; b -= 1
    g[a].append(b)
    g[b].append(a)

articulation = find_articulation_point(g)
articulation = [i + 1 for i in range(V) if articulation[i]]
print(len(articulation))
if articulation: print(*articulation)
