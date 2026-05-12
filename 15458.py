import io, os, sys
sys.setrecursionlimit(100001)
reader = io.BufferedReader(io.FileIO(0), buffer_size=131072)
text_reader = io.TextIOWrapper(reader, encoding='utf-8')
input_ = reader.readline
sys.stdin = open('data.txt')
input_ = sys.stdin.readline
sinput = text_reader.readline
def minput(): return map(int, input_().split())


def dfs(cur, parent):
    tmp = [1, 1, 1]
    for nxt in g[cur]:
        if nxt == parent:
            continue
        dfs(nxt, cur)
        tmp[0] = tmp[0] * (dp[nxt][1] + dp[nxt][2]) % MOD
        tmp[1] = tmp[1] * (dp[nxt][0] + dp[nxt][2]) % MOD
        tmp[2] = tmp[2] * (dp[nxt][0] + dp[nxt][1]) % MOD
    if colors[cur] == -1:
        dp[cur][0] = tmp[0]
        dp[cur][1] = tmp[1]
        dp[cur][2] = tmp[2]
    elif colors[cur] == 0:
        dp[cur][0] = tmp[0]
        dp[cur][1] = 0
        dp[cur][2] = 0
    elif colors[cur] == 2:
        dp[cur][0] = 0
        dp[cur][1] = tmp[1]
        dp[cur][2] = 0
    else:
        dp[cur][0] = 0
        dp[cur][1] = 0
        dp[cur][2] = tmp[2]


MOD = 10 ** 9 + 7
output = []
N, K = minput()
g = [[] for _ in range(N)]
for _ in range(N - 1):
    x, y = minput()
    x -= 1; y -= 1
    g[x].append(y)
    g[y].append(x)
colors = [-1] * N
for _ in range(K):
    b, c = minput()
    colors[b - 1] = c - 1

# dp[i][j]: i번 정점을 색 j로 칠했을 때 i번을 루트로 하는 서브트리에서 경우의 수
dp = [[1, 1, 1] for _ in range(N)]
dfs(0, 0)
output.append(str(sum(dp[0]) % MOD))
os.write(1, '\n'.join(output).encode())
os._exit(0)
