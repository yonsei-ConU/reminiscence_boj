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

q = deque([g[0][0]])
L = [-1] * N
L[0] = 0
chk = True

os.write(1, '\n'.join(output).encode())
os._exit(0)
