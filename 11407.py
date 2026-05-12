import sys
from algorithms import MCMF, add_edge_mcmf
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


N, M = minput()
# 0: source, 1~M: bookstore, M+1~M+N: person, M+N+1: sink
g = [[] for _ in range(N + M + 2)]
A = list(minput())
B = list(minput())
C = [list(minput()) for _ in range(M)]
D = [list(minput()) for _ in range(M)]

for i in range(M):
    add_edge_mcmf(g, 0, i + 1, B[i], 0)

for i in range(M):
    for j in range(N):
        add_edge_mcmf(g, i + 1, j + M + 1, C[i][j], D[i][j])

for i in range(N):
    add_edge_mcmf(g, i + M + 1, N + M + 1, A[i], 0)

flow, cost = MCMF(g, 0, N + M + 1)
print(flow)
print(cost)
