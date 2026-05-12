import sys
from algorithms import add_edge, dinitz
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


for _ in range(int(input_())):
    n, m = minput()
    # 0 source, 1~n left n+1~2n right 2n+1 sink
    g = [[] for _ in range(2 * n + 2)]
    for i in range(1, n + 1):
        add_edge(g, 0, i, 1)
        add_edge(g, i + n, 2 * n + 1, 1)
    for _ in range(m):
        u, v = minput()
        u += 1
        v += 1
        add_edge(g, u, v + n, 1)
    ans = dinitz(g, 0, 2 * n + 1)
    print(ans)
