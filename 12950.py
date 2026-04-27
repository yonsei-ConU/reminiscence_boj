import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


def dfs(start, end, length, visited):
    global ans
    for c in range(26):
        for ns in g[start][c]:
            for ne in g[end][c]:
                if ns == end and ne == start:
                    ans = min(ans, length + 1)
                    break
                elif visited & ((1 << ns) | (1 << ne)):
                    continue
                elif ns == ne:
                    ans = min(ans, length + 2)
                else:
                    dfs(ns, ne, length + 2, visited | (1 << ns) | (1 << ne))


N, M = minput()
g = [[[] for __ in range(26)] for _ in range(N)]
# g[v][alph]: v번 정점에서 값이 alph인 간선으로 갈 수 있는 정점들의 목록
for _ in range(M):
    a, b, c = input_().split()
    a = int(a)
    b = int(b)
    c = ord(c) - 97
    g[a][c].append(b)
    g[b][c].append(a)

ans = 100000
dfs(0, 1, 0, 3)
print(ans if ans != 100000 else -1)
