import sys
from collections import defaultdict, deque
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


n, q = minput()
g = defaultdict(list)
for _ in range(n):
    data = input_().split()
    v1, n1, asdf, v2, n2 = data
    v1 = float(v1)
    v2 = float(v2)
    g[n1].append((n2, v2 / v1))
    g[n2].append((n1, v1 / v2))

for _ in range(q):
    v, n1, asf, n2 = input_().split()
    v = float(v)
    dq = deque([n1])
    weight = defaultdict(float)
    weight[n1] = v
    while dq:
        cur = dq.popleft()
        for nxt, mult in g[cur]:
            if not weight[nxt]:
                dq.append(nxt)
                weight[nxt] = weight[cur] * mult
    if weight[n2]:
        print(weight[n2])
    else:
        print("impossible")
