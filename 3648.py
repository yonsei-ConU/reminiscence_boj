import sys
from algorithms import tarjan
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


def two_sat(N, clauses):
    g = [[] for _ in range(N << 1)]
    g[N].append(0)
    for a, b in clauses:
        if a < 0:
            a = N - a
        if b < 0:
            b = N - b
        a -= 1; b -= 1
        g[(a + N) % (2 * N)].append(b)
        g[(b + N) % (2 * N)].append(a)
    scc = tarjan(g)
    scc_rev = [0] * (N << 1)
    for i in range(len(scc)):
        for c in scc[i]:
            scc_rev[c] = i
    for i in range(N):
        if scc_rev[i] == scc_rev[i + N]:
            return 0
    return 1


while True:
    try:
        n, m = minput()
    except:
        break
    result = two_sat(n, [list(minput()) for _ in range(m)])
    print('yneos'[1 - result::2])
