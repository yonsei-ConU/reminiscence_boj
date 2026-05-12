import sys
sys.setrecursionlimit(1010101)
input_ = sys.stdin.readline
def minput(): return map(lambda x: int(x) - 1, input_().split())


def dfs(cur, parent):
    for nxt in g[cur]:
        if nxt == parent:
            continue
        dfs(nxt, cur)
    dp1_new = 1
    dp2_new = 0
    for nxt in g[cur]:
        if nxt == parent:
            continue
        dp1_new += min(dp1[nxt], dp2[nxt])
        dp2_new += dp1[nxt]
    dp1[cur] = dp1_new
    dp2[cur] = dp2_new


N = int(input_())
g = [[] for _ in range(N)]

for i in range(N - 1):
    u, v = minput()
    g[u].append(v)
    g[v].append(u)

dp1 = [0] * N
dp2 = [0] * N
dfs(0, -1)
print(min(dp1[0], dp2[0]))
