import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


N, M = minput()
g_real = [{} for _ in range(N)]
for _ in range(M):
    S, E, L = minput()
    S -= 1; E -= 1
    g_real[S][E] = L
    g_real[E][S] = L

for start in range(N):
    ans = 0
    g = []
    for d in g_real: g.append(d)
