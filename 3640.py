import sys
from algorithms import MCMF, add_edge_mcmf
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


while 1:
    try:
        v, e = minput()
    except:
        break
    # 0~n-1 in, n~2n-1 out
    g = [[] for _ in range(2 * v)]
    add_edge_mcmf(g, 0, v, 2, 0)
    for i in range(1, v - 1):
        add_edge_mcmf(g, i, i + v, 1, 0)
    add_edge_mcmf(g, v - 1, 2 * v - 1, 2, 0)
    for _ in range(e):
        a, b, c = minput()
        a -= 1
        b -= 1
        add_edge_mcmf(g, a + v, b, 1, c)
    print(MCMF(g, 0, 2 * v - 1))
