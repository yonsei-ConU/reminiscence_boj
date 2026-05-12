import io, os, sys
sys.setrecursionlimit(100001)
reader = io.BufferedReader(io.FileIO(0), buffer_size=131072)
text_reader = io.TextIOWrapper(reader, encoding='utf-8')
input_ = reader.readline
sinput = text_reader.readline
def minput(): return map(int, input_().split())


def dfs(cur, parent):
    dp[cur][a[cur]] += 1
    for nxt in g[cur]:
        if nxt == parent:
            continue
        dfs(nxt, cur)
        dp[cur][0] += dp[nxt][0]
        dp[cur][1] += dp[nxt][1]


output = []
N = int(input_())
a = list(minput())
g = [[] for _ in range(N)]
for _ in range(N - 1):
    a, b = minput()
    a -= 1; b -= 1
    g[a].append(b)
    g[b].append(a)
dp = [[0, 0] for _ in range(N)]
dfs(0, 0)

for _ in range(int(input_())):
    u = int(input_()) - 1

os.write(1, '\n'.join(output).encode())
os._exit(0)
