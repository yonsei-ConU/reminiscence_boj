import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


for tc in range(1, int(input_()) + 1):
    N = int(input_())
    g = [[] for _ in range(N)]
    g[0] = [1, 2]
    g[1] = [0, 2]
    g[2] = [0, 1]
    for c in range(N - 3):
        a, b = minput()
        a -= 1, b -= 1
        g[a].append(c)
        g[c].append(a)
        g[b].append(c)
        g[c].append(b)

    
