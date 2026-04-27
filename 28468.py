import sys
from collections import defaultdict
from math import comb
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


N, M = minput()
g = [set() for _ in range(N)]
for _ in range(M):
    a, b = minput()
    a -= 1; b -= 1
    g[a].add(b)
    g[b].add(a)

ans = 0
for v in range(N):
    deg = len(g[v])
    if deg < 6:
        continue
    # deg가 6 이상인 정점들에 대해서만 찾아도됨
    # 우선 해당 정점이 들어간 모든 3사이클을 탐지 O(deg**2)
    cycles = []
    in_cycle = defaultdict(int)
    adj = tuple(g[v])
    for i in range(deg):
        for j in range(i):
            if adj[j] in g[adj[i]] and adj[i] in g[adj[j]]:
                cycles.append((adj[i], adj[j]))
                in_cycle[adj[i]] += 1
                in_cycle[adj[j]] += 1
    not_disjoint_count = 0
    for p, q in cycles:
        not_disjoint_count += in_cycle[p] + in_cycle[q] - 2
    assert not not_disjoint_count & 1
    disjoint_count = comb(len(cycles), 2) - (not_disjoint_count >> 1)
    ans += disjoint_count * comb(deg - 4, 2)

print(ans)
