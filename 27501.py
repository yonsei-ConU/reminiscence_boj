import io, os, sys
from collections import deque
sys.setrecursionlimit(500000)
input_ = io.BufferedReader(io.FileIO(0), buffer_size=131072).readline
def minput(): return map(int, input_().split())


def dfs(cur, parent):
    for nxt in g[cur]:
        if nxt == parent:
            continue
        dfs(nxt, cur)
        dp[cur][0] += max(dp[nxt][1], dp[nxt][2])
        dp[cur][1] += max(dp[nxt][0], dp[nxt][2])
        dp[cur][2] += max(dp[nxt][0], dp[nxt][1])
    dp[cur][0] += dp_delta[cur][0]
    dp[cur][1] += dp_delta[cur][1]
    dp[cur][2] += dp_delta[cur][2]


N = int(input_())
g = [[] for _ in range(N)]
for i in range(N - 1):
    a, b = minput()
    a -= 1; b -= 1
    g[a].append(b)
    g[b].append(a)
dp_delta = [tuple(minput()) for _ in range(N)]
dp = [[0, 0, 0] for _ in range(N)]
dfs(0, 0)
m = max(dp[0])
print(m)
ans = [-1] * N
if m == dp[0][0]:
    ans[0] = 0
elif m == dp[0][1]:
    ans[0] = 1
else:
    ans[0] = 2
q = deque([0])
visited = [False] * N
visited[0] = True
while q:
    cur = q.popleft()
    for nxt in g[cur]:
        if visited[nxt]:
            continue
        visited[nxt] = True
        if ans[cur] == 0:
            if dp[nxt][1] >= dp[nxt][2]:
                ans[nxt] = 1
            else:
                ans[nxt] = 2
        elif ans[cur] == 1:
            if dp[nxt][0] >= dp[nxt][2]:
                ans[nxt] = 0
            else:
                ans[nxt] = 2
        else:
            if dp[nxt][0] >= dp[nxt][1]:
                ans[nxt] = 0
            else:
                ans[nxt] = 1
        q.append(nxt)
for i in range(N):
    if ans[i] == 0:
        ans[i] = 'R'
    elif ans[i] == 1:
        ans[i] = 'G'
    else:
        ans[i] = 'B'
print(''.join(ans))
os._exit(0)
