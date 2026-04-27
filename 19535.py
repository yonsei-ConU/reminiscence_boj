import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


N = int(input_())
g = [[] for _ in range(N)]
for _ in range(N - 1):
    u, v = minput()
    g[u - 1].append(v - 1)
    g[v - 1].append(u - 1)

D = 0
for u in range(N):
    for v in g[u]:
        if u > v:
            continue
        D += (len(g[u]) - 1) * (len(g[v]) - 1)

G = 0
for u in range(N):
    d = len(g[u])
    G += d * (d - 1) * (d - 2) // 6

if D > G * 3:
    print("D")
elif D < G * 3:
    print("G")
else:
    print("DUDUDUNGA")
