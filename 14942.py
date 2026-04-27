import sys
sys.setrecursionlimit(101010)
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


n = int(input_())
energy = [int(input_()) for _ in range(n)]
g = [[] for _ in range(n)]
for _ in range(n - 1):
    a, b, c = minput()
    a -= 1; b -= 1
    g[a].append((b, c))
    g[b].append((a, c))
