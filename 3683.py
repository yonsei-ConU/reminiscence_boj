import sys
from algorithms import add_edge, dinitz
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


for _ in range(int(input_())):
    c, d, v = minput()
    cd = []
    dc = []
    for __ in range(v):
        data = input_().split()
        if data[0][0] == 'C':
            cd.append((int(data[0][1:]), int(data[1][1:])))
        else:
            dc.append((int(data[0][1:]), int(data[1][1:])))
    # 0 source, v + 1 sink
    g = [[] for _ in range(v + 2)]
    for i in range(1, len(cd) + 1):
        add_edge(g, 0, i, 1)
    for i in range(len(cd) + 1, v + 1):
        add_edge(g, i, v + 1, 1)
    for i in range(len(cd)):
        for j in range(len(dc)):
            if cd[i][0] == dc[j][1] or cd[i][1] == dc[j][0]:
                add_edge(g, i + 1, len(cd) + j + 1, 1)
    print(v - dinitz(g, 0, v + 1))
