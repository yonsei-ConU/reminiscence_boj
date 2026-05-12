import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


def floyd_warshall(g, n):
    trace = [[-1] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if g[i][j] < 10 ** 18:
                trace[i][j] = i
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if i != j and g[i][k] + g[k][j] < g[i][j]:
                    trace[i][j] = trace[k][j]
                    g[i][j] = g[i][k] + g[k][j]
    return g, trace


n = int(input_())
m = int(input_())
g = [[10 ** 18] * n for _ in range(n)]
for _ in range(m):
    a, b, c = minput()
    g[a - 1][b - 1] = min(c, g[a - 1][b - 1])

dist, trace = floyd_warshall(g, n)
print(trace)
for i in range(n):
    for j in range(n):
        if dist[i][j] == 10 ** 18:
            dist[i][j] = 0

for d in dist:
    print(*d)

for i in range(n):
    for j in range(n):
        if i == j or not dist[i][j]:
            print(0)
        else:
            path = [j + 1]
            cur = j
            while cur != i:
                cur = trace[i][cur]
                path.append(cur + 1)
            print(len(path), *path[::-1])
