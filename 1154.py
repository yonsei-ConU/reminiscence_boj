import sys
from collections import deque
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


N = int(input_())
f = [[False] * N for _ in range(N)]
for i in range(N): f[i][i] = True

while True:
    a, b = minput()
    if a == b == -1:
        break
    a -= 1; b -= 1
    f[a][b] = f[b][a] = True

g = [[j for j in range(N) if not f[i][j]] for i in range(N)]
color = [-1] * N

for i in range(N):
    if color[i] == -1:
        color[i] = 0
        q = deque([i])
        while q:
            cur = q.popleft()
            for nxt in g[cur]:
                if color[nxt] == -1:
                    q.append(nxt)
                    color[nxt] = color[cur] ^ 1
                elif color[nxt] == color[cur]:
                    exit(print(-1))

print(1)
team0 = [i + 1 for i in range(N) if not color[i]]
team1 = [i + 1 for i in range(N) if color[i]]
print(*team0, -1)
print(*team1, -1)
