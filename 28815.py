import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


n = int(input_())
b = list(minput())
g = list(minput())
B = []
G = []
for i in range(n):
    B.append((b[i], i + 1))
    G.append((g[i], i + 1))

B.sort()
G.sort()
for _ in range(n):
    p, q = B[_]
    r, s = G[_]
    print(q, s)
