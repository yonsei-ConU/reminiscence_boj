import sys
from collections import deque
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


n = int(input_())
g = [[] for _ in range(n)]
deg = [0] * n
for i in range(n):
    u, v, w = minput()
    u -= 1; v -= 1
    g[u].append((v, w, i))
    g[v].append((u, w, i))
    deg[u] += 1
    deg[v] += 1

ans = [-1] * n
deg1 = deque([i for i in range(n) if deg[i] == 1])
in_trans = [set() for _ in range(n)]
in_cycle = [True] * n
while deg1:
    cur = deg1.popleft()
    in_cycle[cur] = False
    nxt, weight, idx = g[cur][0]
    ans[idx] = cur + 1
    if weight in in_trans[nxt]:
        exit(print('impossible'))
    in_trans[nxt].add(weight)
    deg[nxt] -= 1
    if deg[nxt] == 1:
        deg1.append(nxt)

# 이시점에서 남은 건 사이클
cycle = []
for i in range(n):
    if in_cycle[i]:
        cycle.append(i)

start = -1
for u in cycle:
    problem = []
    for v, w, idx in g[u]:
        if w in in_trans[u] and in_cycle[v]:
            problem.append((v, idx))
            start = v
    if len(problem) == 2:
        exit(print('impossible'))
    elif len(problem) == 1:
        v, idx = problem[0]
        if ans[idx] == -1 or ans[idx] == v:
            ans[idx] = v
        else:
            exit(print('impossible'))

if start == -1:
    start = cycle[0]
    flag = False
else:
    flag = True

cur = start
visited = [False] * n
visited[cur] = True
for i in range(len(cycle) - flag):
    for nxt, weight, idx in g[cur]:
        if not visited[nxt]:
            visited[nxt] = True
            if ans[idx] != -1 and ans[idx] != cur + 1:
                exit(print('impossible'))
            ans[idx] = cur + 1
            cur = nxt
            break

ans[g[start][1][2]] = g[start][1][0] + 1
for v in ans:
    print(v)
