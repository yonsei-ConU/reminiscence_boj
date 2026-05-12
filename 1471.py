import sys
from algorithms import tarjan
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


N = int(input_())
f = list(range(N))
g = [[] for _ in range(N)]
for i in range(N):
    j = i + 1
    d = 0
    while j:
        d += j % 10
        j //= 10
    f[i] += d % N
    if f[i] >= N:
        f[i] -= N
    g[i].append(f[i])

scc = tarjan(g)
ans = [-1] * N

for component in scc:
    v = component[0]
    if ans[f[v]] == -1:
        # topological sort DAG에서 가장 마지막 위치에 있음
        for u in component:
            ans[u] = len(component)
    else:
        # 다른 scc로 이동할 수 있음
        assert len(component) == 1
        ans[v] = ans[f[v]] + 1

print(max(ans))
