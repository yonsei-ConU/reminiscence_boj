import io, os
from collections import deque
reader = io.BufferedReader(io.FileIO(0), buffer_size=131072)
text_reader = io.TextIOWrapper(reader, encoding='utf-8')
input_ = reader.readline
sinput = text_reader.readline
def minput(): return map(int, input_().split())


output = []
N = int(input_())
g = [[] for _ in range(N)]
for _ in range(N - 1):
    u, v = minput()
    u -= 1; v -= 1
    g[u].append(v)
    g[v].append(u)
leaf = [False] * N
for i in range(N):
    if len(g[i]) == 1:
        leaf[i] = True

start = tuple(map(lambda x: int(x) - 1, sinput().split()))
dist = [[-1] * N for _ in range(3)]
for i in range(3):
    dist[i][start[i]] = 0
    q = deque([start[i]])
    while q:
        cur = q.popleft()
        for nxt in g[cur]:
            if dist[i][nxt] == -1:
                dist[i][nxt] = dist[i][cur] + 1
                q.append(nxt)

for i in range(N):
    if leaf[i]:
        if min(dist[j][i] for j in range(3)) == dist[0][i] != dist[1][i] and dist[2][i] != dist[0][i]:
            output.append('YES')
            break
else:
    output.append('NO')
os.write(1, '\n'.join(output).encode())
os._exit(0)
