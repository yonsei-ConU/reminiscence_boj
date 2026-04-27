import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


N, M, K = minput()
g = [[] for _ in  range(N)]
indegree = [0] * N
for _ in range(M):
    X, Y = minput()
    X -= 1
    Y -= 1
    g[X].append(Y)
    indegree[Y] += 1

build_check = [0] * N
built = [0] * N
ans = True
for _ in range(K):
    q, a = minput()
    a -= 1
    if q == 1:
        if build_check[a] < indegree[a]:
            print('Lier!')
            exit()
        else:
            if not built[a]:
                for nxt in g[a]:
                    build_check[nxt] += 1
            built[a] += 1
    else:
        if not built[a]:
            print('Lier!')
            exit()
        elif built[a] == 1:
            for nxt in g[a]:
                build_check[nxt] -= 1
        built[a] -= 1
else:
    print('King-God-Emperor')
