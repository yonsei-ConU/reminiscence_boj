import sys
from algorithms import LCA_query
from types import GeneratorType
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


def bootstrap(f, stack=[]):
    def wrappedfunc(*args, **kwargs):
        if stack:
            return f(*args, **kwargs)
        else:
            to = f(*args, **kwargs)
            while True:
                if type(to) is GeneratorType:
                    stack.append(to)
                    to = next(to)
                else:
                    stack.pop()
                    if not stack:
                        break
                    to = stack[-1].send(to)
            return to

    return wrappedfunc


def LCA_preprocess(g, root):
    v = len(g)
    d = [0] * v
    table = [[0] * v for _ in range(v.bit_length())]

    @bootstrap
    def LCA_dfs(cur, parent):
        table[0][cur] = parent
        for nxt in g[cur]:
            if nxt == parent:
                continue
            d[nxt] = d[cur] + 1
            yield LCA_dfs(nxt, cur)
        yield

    LCA_dfs(root, -1)

    for i in range(1, v.bit_length()):
        for j in range(v):
            table[i][j] = table[i-1][table[i-1][j]]

    return d, table


def LCA_preprocess2(g, root):
    v = len(g)
    D = [0] * v
    d = [0] * v
    table = [[0] * v for _ in range(v.bit_length())]

    @bootstrap
    def LCA_dfs(cur, parent):
        table[0][cur] = parent
        for nxt, weight in g[cur]:
            if nxt == parent:
                continue
            D[nxt] = D[cur] + weight
            d[nxt] = d[cur] + 1
            yield LCA_dfs(nxt, cur)
        yield

    LCA_dfs(root, -1)

    for i in range(1, v.bit_length()):
        for j in range(v):
            table[i][j] = table[i-1][table[i-1][j]]

    return D, d, table


def path_length(u, v, d, table):
    return d[u] + d[v] - 2 * d[LCA_query(u, v, d, table)]


def getMTE(u):
    if u >= N:
        u_MTE_num = (u // N) - 1
        u_MTE_up = u_MTE_num + N
        u_MTE_down = u_MTE_num + 2 * N - 1
        if D_MTE[u_MTE_up] > D_MTE[u_MTE_down]:
            u_MTE_up, u_MTE_down = u_MTE_down, u_MTE_up
    else:
        u_MTE_up = u_MTE_down = u
    return u_MTE_up, u_MTE_down


N, Q = minput()
edges = []
initial_tree = [[] for _ in range(N)]
for i in range(N - 1):
    a, b = minput()
    a -= 1; b -= 1
    edges.append((a, b))
    initial_tree[a].append(b)
    initial_tree[b].append(a)

D, table = LCA_preprocess(initial_tree, 0)

# i번 정점은 진짜 i번 정점
# N + i번 정점은 i번뭉탱이 in
# 2N + i - 1번 정점은 i번뭉탱이 out
tree_MTE = [[] for _ in range(3 * N - 2)]
connect = [{} for _ in range(N - 1)]
for i in range(N - 1):
    c, d = minput()
    c -= 1; d -= 1
    e, f = edges[i]
    connect[i][e] = N * (i + 1) + c
    connect[i][f] = N * (i + 1) + d
    dist = path_length(c, d, D, table)
    tree_MTE[N + i].append((2 * N - 1 + i, dist))
    tree_MTE[2 * N - 1 + i].append((N + i, dist))
    tree_MTE[e].append((N + i, 1))
    tree_MTE[N + i].append((e, 1))
    tree_MTE[f].append((2 * N - 1 + i, 1))
    tree_MTE[2 * N - 1 + i].append((f, 1))

D_MTE, d_MTE, table_MTE = LCA_preprocess2(tree_MTE, 0)

for _ in range(Q):
    u, v = minput()
    u -= 1; v -= 1
    # 우선 내가 몇 번 뭉탱이에서 몇 번 뭉탱이로 가야 하는지를 확인
    uUp, uDown = getMTE(u)
    vUp, vDown = getMTE(v)
    if uUp == vUp and uDown == vDown:
        # 같은 뭉탱이 안에 있다
        print(LCA_query(u & 3, v & 3, D, table))
    else:
        if d_MTE[LCA_query(uUp, vUp, d_MTE, table_MTE)] == d_MTE[uUp]:
            U = uDown
        else:
            U = uUp
        if d_MTE[LCA_query(uUp, vUp, d_MTE, table_MTE)] == d_MTE[vUp]:
            V = vDown
        else:
            V = vUp
        ans = path_length(U, V, D_MTE, table_MTE)
        if u >= N:
            ConU = connect[(u // N) - 1]
            up, down = ConU.keys()
            if d_MTE[up] > d_MTE[down]:
                up, down = down, up
            if U == uUp:
                ans += path_length(ConU[up] & 3, u & 3, D, table)
            else:
                ans += path_length(ConU[down] & 3, u & 3, D, table)
        if v >= N:
            ConV = connect[(v // N) - 1]
            up, down = ConV.keys()
            if d_MTE[up] > d_MTE[down]:
                up, down = down, up
            if V == vUp:
                ans += path_length(ConV[up] & 3, v & 3, D, table)
            else:
                ans += path_length(ConV[down] & 3, v & 3, D, table)
        print(ans)
