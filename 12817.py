import io, os, sys
sys.setrecursionlimit(1000001)
reader = io.BufferedReader(io.FileIO(0), buffer_size=131072)
text_reader = io.TextIOWrapper(reader, encoding='utf-8')
input_ = reader.readline
sinput = text_reader.readline
def minput(): return map(int, input_().split())


def dfs(begin, connect):
    visited = [False] * len(connect)
    child_count = [0] * len(connect)
    stack = [(begin, -1)]
    while stack:
        u, i = stack.pop()
        visited[u] = True
        if i < 0:
            ...
        else:
            v = connect[u][i]
            child_count[u] += dp[v]
        i += 1
        while i < len(connect[u]):
            v = connect[u][i]
            if visited[v]:
                i += 1
                continue
            par[v] = u
            stack.append((u, i))
            stack.append((v, -1))
            break
        else:
            dp[u] = child_count[u] + 1


output = []
N = int(input_())
g = [[] for _ in range(N)]
for _ in range(N - 1):
    a, b = minput()
    a -= 1; b -= 1
    g[a].append(b)
    g[b].append(a)
# dp[i]: the number of nodes in subtree rooted at i
dp = [0] * N
par = [0] * N
dfs(0, g)

for i in range(N):
    ans = N ** 2 - 1 - sum(dp[c] ** 2 for c in g[i] if c != par[i]) - (N - dp[i]) ** 2
    output.append(str(ans))

os.write(1, '\n'.join(output).encode())
os._exit(0)
