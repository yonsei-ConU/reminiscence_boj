import sys
from algorithms import MCMF, add_edge_mcmf
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


N, M = minput()
g = [[] for _ in range(N + M + 2)]

for i in range(1, N + 1):
    add_edge_mcmf(g, 0, i, 1, 0)

for i in range(1, N + 1):
    cnt, *works = minput()
    ptr = 0
    while ptr < len(works):
        work, cost = works[ptr], works[ptr + 1]
        add_edge_mcmf(g, i, work + N, 1000000, cost)
        ptr += 2

for i in range(N + 1, N + M + 1):
    add_edge_mcmf(g, i, N + M + 1, 1, 0)

flow, cost = MCMF(g, 0, N + M + 1)
print(flow)
print(cost)
