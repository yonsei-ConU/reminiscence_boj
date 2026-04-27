import sys
sys.setrecursionlimit(100000)
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


def dfs(cur, parent):
    for nxt in g[cur]:
        if nxt == parent:
            continue
        dfs(nxt, cur)

    dp_in[cur] = weight[cur]
    for nxt in g[cur]:
        if nxt == parent:
            continue
        dp_ex[cur] += max(dp_ex[nxt], dp_in[nxt])
        dp_in[cur] += dp_ex[nxt]


n = int(input_())
weight = list(minput())
g = [[] for _ in range(n)]
for _ in range(n - 1):
    a, b = minput()
    a -= 1; b -= 1
    g[a].append(b); g[b].append(a)

dp_in = [0] * n
dp_ex = [0] * n
dfs(0, -1)

x = max(dp_in[0], dp_ex[0])
print(x)
