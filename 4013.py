import sys
from algorithms import getSCC
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


N, M = minput()
g = [[] for _ in range(N)]
for _ in range(M):
    u, v = minput()
    u -= 1; v -= 1
    g[u].append(v)

node_cash = [int(input_()) for _ in range(N)]

S, P = minput()
S -= 1
final_state = set(map(lambda x: int(x) - 1, input_().split()))

scc = getSCC(g)[::-1]
scc_id = [-1] * N
for i in range(len(scc)):
    for v in scc[i]:
        scc_id[v] = i

scc_cash = [0] * len(scc)
scc_has_fin = [False] * len(scc)
for i in range(len(scc)):
    for v in scc[i]:
        scc_cash[i] += node_cash[v]
        if v in final_state:
            scc_has_fin[i] = True

dp = [-1] * len(scc)
start_id = scc_id[S]
dp[start_id] = scc_cash[start_id]

for i in range(len(scc)):
    if dp[i] == -1:
        continue
    for u in scc[i]:
        for v in g[u]:
            next_id = scc_id[v]
            if i != next_id:
                dp[next_id] = max(dp[next_id], dp[i] + scc_cash[next_id])

ans = 0
for i in range(len(scc)):
    if scc_has_fin[i] and dp[i] != -1:
        ans = max(ans, dp[i])

print(ans)