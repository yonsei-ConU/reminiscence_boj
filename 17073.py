import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


N, W = minput()
g = [[] for _ in range(N)]
for i in range(N - 1):
    U, V = minput()
    U -= 1; V -= 1
    g[U].append(V)
    g[V].append(U)

leaf = sum(1 for i in range(1, N) if len(g[i]) == 1)
print(W / leaf)
