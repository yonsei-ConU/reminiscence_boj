import sys
from algorithms import kruskal
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


N, M, t = minput()
edges = []
for _ in range(M):
    A, B, C = minput()
    edges.append((C, A - 1, B - 1))

weight = kruskal(N, edges)
print(weight + t * (N - 2) * (N - 1) // 2)
