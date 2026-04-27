import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


def floyd_warshall(g, n):
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if i != j:
                    g[i][j] = min(g[i][k] + g[k][j], g[i][j])
    return g


tc = 1
space = ' '
while True:
    if tc != 1:
        print()
    g = [[100] * 20 for _ in range(20)]
    for i in range(20):
        g[i][i] = 0
    for i in range(19):
        adj = list(minput())[1:]
        for a in adj:
            g[i][a - 1] = 1
            g[a - 1][i] = 1
    g = floyd_warshall(g, 20)
    try:
        X = int(input_())
    except:
        exit()
    print(f"Test Set #{tc}")
    for _ in range(X):
        s, e = minput()
        ans = g[s - 1][e - 1]
        print(f"{space * (s < 10)}{s} to {space * (e < 10)}{e}: {ans}")
    tc += 1
