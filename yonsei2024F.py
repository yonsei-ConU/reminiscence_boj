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

a, b, x = minput()
a -= 1; b -= 1; x -= 1

q = deque()
candidate = [True] * N
visited = [False] * N
visited[x] = True

if a != x:
    q.append(a)
    visited[a] = True
    candidate[a] = False

if b != x:
    q.append(b)
    visited[b] = True
    candidate[b] = False

while q:
    cur = q.popleft()
    for nxt in g[cur]:
        if visited[nxt]:
            continue
        q.append(nxt)
        candidate[nxt] = False
        visited[nxt] = True

output.append(str(sum(candidate)))

os.write(1, '\n'.join(output).encode())
os._exit(0)
