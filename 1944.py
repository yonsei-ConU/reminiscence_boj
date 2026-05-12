import sys
from collections import deque
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


class UnionFind:
    def __init__(self, size):
        self.parent = [i for i in range(size)]
        self.rank = [0] * size

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
            if self.rank[root_x] > self.rank[root_y]:
                self.parent[root_y] = root_x
            elif self.rank[root_x] < self.rank[root_y]:
                self.parent[root_x] = root_y
            else:
                self.parent[root_y] = root_x
                self.rank[root_x] += 1


def kruskal(v, edges):
    edges.sort()
    uf = UnionFind(v)
    mst_weight = 0
    for edge in edges:
        weight, s, e = edge
        if uf.find(s) != uf.find(e):
            mst_weight += weight
            uf.union(s, e)
    if len(set(uf.find(x) for x in range(v))) != 1:
        return 10 ** 18
    return mst_weight


def get_dist(y, x):
    q = deque([(y, x)])
    ret = [[10 ** 18] * N for _ in range(N)]
    ret[y][x] = 0
    while q:
        y, x = q.popleft()
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if (not (0 <= ny < N and 0 <= nx < N)) or ret[ny][nx] != 10 ** 18 or board[ny][nx] == '1':
                continue
            q.append((ny, nx))
            ret[ny][nx] = ret[y][x] + 1
    return ret


dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]
N, M = minput()
board = []
keys = []
for i in range(N):
    s = input_().rstrip()
    tmp = []
    for j in range(N):
        if s[j] == '1':
            tmp.append('1')
        else:
            if s[j] != '0':
                keys.append((i, j))
            tmp.append('0')
    board.append(tmp)

edges = []
for i in range(len(keys)):
    dist = get_dist(keys[i][0], keys[i][1])
    for j in range(i):
        y, x = keys[j]
        edges.append((dist[y][x], i, j))
ans = kruskal(len(keys), edges)
if ans >= 10 ** 18:
    print(-1)
else:
    print(ans)
