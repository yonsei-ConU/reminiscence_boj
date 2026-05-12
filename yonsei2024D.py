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
for i in range(N):
    a, b = minput()
    a -= 1; b -= 1
    g[i].append(a)
    g[i].append(b)

q = deque()
q.append((0, 0))
visited = [[False] * 100 for _ in range(N)]
current_time = 0
ans = -1
while q:
    cur, t = q.popleft()
    if t == 99:
        continue
    for nxt in g[cur]:
        if visited[nxt][t + 1]:
            continue
        q.append((nxt, t + 1))
        visited[nxt][t + 1] = True
    if current_time != q[0][1] and q:
        current_time += 1
        if current_time < 10:
            continue
        chk = True
        for person, time in q:
            if time > current_time:
                break
            elif not person:
                chk = False
                break
        if chk:
            ans = current_time
            break

output.append(str(ans))

os.write(1, '\n'.join(output).encode())
os._exit(0)
